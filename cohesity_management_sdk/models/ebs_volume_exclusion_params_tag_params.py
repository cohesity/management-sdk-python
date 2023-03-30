# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ebs_volume_exclusion_params_tag


class EBSVolumeExclusionParams_TagParams(object):

    """Implementation of the 'EBSVolumeExclusionParams_TagParams' model.

    Specifies the tag vectors used to exclude EBS volumes attached to EC2
    instances at global and object level. Contains two vectors: exclusion and
    inclusion. E.g., {exclusion_tag_vec: [(K1, V1),  (K2, V2)],
    inclusion_tag_vec: [(K3, V3)]}. => This will exclude a particular volume
    iff it has all the tags in exclusion_tag_vec((K1, V1),  (K2, V2)) and has
    none of the tags in the inclusion_tag_vec((K3, V3)).


    Attributes:

        exclusion_tag_vec (list of EBSVolumeExclusionParams_Tag): TODO: Type
            description here.
        inclusion_tag_vec (list of EBSVolumeExclusionParams_Tag): TODO: Type
            description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "exclusion_tag_vec":'exclusionTagVec',
        "inclusion_tag_vec":'inclusionTagVec',
    }
    def __init__(self,
                 exclusion_tag_vec=None,
                 inclusion_tag_vec=None,
            ):

        """Constructor for the EBSVolumeExclusionParams_TagParams class"""

        # Initialize members of the class
        self.exclusion_tag_vec = exclusion_tag_vec
        self.inclusion_tag_vec = inclusion_tag_vec

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        exclusion_tag_vec = None
        if dictionary.get('exclusionTagVec') != None:
            exclusion_tag_vec = list()
            for structure in dictionary.get('exclusionTagVec'):
                exclusion_tag_vec.append(cohesity_management_sdk.models.ebs_volume_exclusion_params_tag.EBSVolumeExclusionParams_Tag.from_dictionary(structure))
        inclusion_tag_vec = None
        if dictionary.get('inclusionTagVec') != None:
            inclusion_tag_vec = list()
            for structure in dictionary.get('inclusionTagVec'):
                inclusion_tag_vec.append(cohesity_management_sdk.models.ebs_volume_exclusion_params_tag.EBSVolumeExclusionParams_Tag.from_dictionary(structure))

        # Return an object of this model
        return cls(
            exclusion_tag_vec,
            inclusion_tag_vec
)