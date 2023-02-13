# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class ViewProtectionSource(object):

    """Implementation of the 'ViewProtectionSource' model.

    Specifies a Protection Source in a View environment.

    Attributes:
        id (UniversalId): Specifies a unique id of a Protection Source for a
            View. The id is unique across Cohesity Clusters.
        name (string): Specifies a human readable name of the Protection
            Source of a View.
        mtype (TypeViewProtectionSourceEnum): Specifies the type of managed
            Object in a View Protection Source environment. Examples of View
            Objects include 'kViewBox' or 'kView'. 'kViewBox' indicates
            Storage Domain as a Protection Source type. 'kView' indicates View
            as a Protection Source type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "mtype":'type'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 mtype=None):
        """Constructor for the ViewProtectionSource class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.mtype = mtype


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
        id = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('id')) if dictionary.get('id') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(id,
                   name,
                   mtype)


