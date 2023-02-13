# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IsilonNfsMountPoint(object):

    """Implementation of the 'IsilonNfsMountPoint' model.

    Specifies NFS Mount Point exposed by Isilon Protection Source.

    Attributes:
        access_zone_name (string): Specifies the Access Zone name.
        description (string): Specifies the description of the NFS mount
            point.
        id (long|int): Specifies the Id of the NFS export.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_zone_name":'accessZoneName',
        "description":'description',
        "id":'id'
    }

    def __init__(self,
                 access_zone_name=None,
                 description=None,
                 id=None):
        """Constructor for the IsilonNfsMountPoint class"""

        # Initialize members of the class
        self.access_zone_name = access_zone_name
        self.description = description
        self.id = id


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
        access_zone_name = dictionary.get('accessZoneName')
        description = dictionary.get('description')
        id = dictionary.get('id')

        # Return an object of this model
        return cls(access_zone_name,
                   description,
                   id)


