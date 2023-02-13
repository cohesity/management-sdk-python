# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IsilonSmbMountPoint(object):

    """Implementation of the 'IsilonSmbMountPoint' model.

    Specifies information specific to SMB shares exposed by Isilon
    file system.

    Attributes:
        access_zone_id (long|int): Specifies the Access Zone Id.
        description (string): Specifies the description of the NFS mount
            point.
        share_name (string): Specifies the name of the SMB/CIFS share.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_zone_id":'accessZoneId',
        "description":'description',
        "share_name":'shareName'
    }

    def __init__(self,
                 access_zone_id=None,
                 description=None,
                 share_name=None):
        """Constructor for the IsilonSmbMountPoint class"""

        # Initialize members of the class
        self.access_zone_id = access_zone_id
        self.description = description
        self.share_name = share_name


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
        access_zone_id = dictionary.get('accessZoneId')
        description = dictionary.get('description')
        share_name = dictionary.get('shareName')

        # Return an object of this model
        return cls(access_zone_id,
                   description,
                   share_name)


