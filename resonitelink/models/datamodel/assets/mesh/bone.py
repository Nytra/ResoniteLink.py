from resonitelink.models.datamodel import Float4x4
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model()
@dataclass(slots=True)
class Bone():
    """
    Represents a bone of a mesh.
    NOTE: This is separate from the sub-folders because it's used in both JSON and RawData meshes.
    
    """
    # Name of the bone.
    # This generally doesn't have much actual function for mesh data, but is useful for references and debugging.
    name : str = json_property("name", str)

    # The bind pose of the bone - its default transform in model space.
    #This is essentially the pose of the bone relative to the vertices where the vertices bound to it will be in their original spot. 
    bind_pose : Float4x4 = json_property("bindPose", Float4x4)
