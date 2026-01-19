from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model()
@dataclass(slots=True)
class BoneWeight():
    """
    Maps vertex to a specific bone with specific weight.
    
    """
    # Index of the bone this maps too in the Bones list of the mesh.
    bone_index : int = json_property("boneIndex", int)

    # Weight from 0...1 that influences how much is this vertex affected by the bone.
    weight : float = json_property("weight", float)
