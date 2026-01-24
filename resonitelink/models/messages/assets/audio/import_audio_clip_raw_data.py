from resonitelink.models.messages import Message, BinaryPayloadMessage
from resonitelink.json import json_model, json_property
from dataclasses import dataclass
from typing import Optional


@json_model("importAudioClipRawData", Message)
@dataclass(slots=True)
class ImportAudioClipRawData(BinaryPayloadMessage):
    _data : Optional[bytes] = None

    # Number of audio samples in this audio clip. This does NOT account for channel count and will be the same
    # regardless of mono/stereo/5.1 etc.
    sample_count : int = json_property("sampleCount", int)
    
    # Sample rate of the audio data.
    sample_rate : int = json_property("sampleRate", int)

    # Number of audio channels. 1 mono, 2 stereo, 6 is 5.1 surround.
    # It's your responsibility to make sure that Resonite supports given audio channel count.
    # The actual audio sample data is interleaved in the buffer.
    channel_count : int = json_property("channelCount", int)
    
    @property
    def duration(self) -> float:
        """
        The duration of the audio clip in seconds, computed from the sample count and sample rate.
        This is just convenience property, setting it will update AudioSampleCount accordingly.

        Returns
        -------
        The computed duration from sample_count and sample_rate.

        """
        return float(self.sample_count) / float(self.sample_rate)
    
    @duration.setter
    def duration(self, value : float):
        """
        The duration of the audio clip in seconds, computed from the sample count and sample rate.
        This is just convenience property, setting it will update AudioSampleCount accordingly.

        Parameters
        ----------
        value : float
            The duration value.

        """
        if self.sample_rate <= 0:
            raise ValueError("You must set sample_rate before setting duration.")
        
        self.sample_count = int(value * self.sample_rate)
    
    @property
    def raw_binary_payload(self) -> bytes:
        if not self._data:
            raise ValueError("Binary data was never provided!")
        
        return self._data

    @raw_binary_payload.setter
    def raw_binary_payload(self, data : bytes):
        if self.sample_count <= 0:
            raise ValueError("Sample count was never provided!")
        
        if self.sample_rate <= 0:
            raise ValueError("Sample rate was never provided!")
        
        if self.channel_count <= 0:
            raise ValueError("Channel count was never provided!")
        
        num_elements = self.sample_count * self.channel_count
        len_bytes = num_elements * 4 # sizeof(float) -> 4 bytes
        if len_bytes != len(data):
            raise ValueError(f"Data size mismatch: Expected: {len_bytes} bytes, Provided: {len(data)} bytes!")
        
        self._data = data
