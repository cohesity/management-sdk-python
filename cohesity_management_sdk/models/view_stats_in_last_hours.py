# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ViewStatsInLastHours(object):

    """Implementation of the 'ViewStatsInLastHours' model.

    Specifies the View stats for last hours.


    Attributes:

        last_hours (long|int): Specifies the time range.
        nfs_protocol_value (long|int): Specifies the stats value for NFS
            protocol.
        s3_protocol_value (long|int): Specifies the stats value for S3
            protocol.
        smb_protocol_value (long|int): Specifies the stats value for SMB
            protocol.
        value (long|int): Specifies the stats value for any protocols.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "last_hours":'lastHours',
        "nfs_protocol_value":'nfsProtocolValue',
        "s3_protocol_value":'s3ProtocolValue',
        "smb_protocol_value":'smbProtocolValue',
        "value":'value',
    }
    def __init__(self,
                 last_hours=None,
                 nfs_protocol_value=None,
                 s3_protocol_value=None,
                 smb_protocol_value=None,
                 value=None,
            ):

        """Constructor for the ViewStatsInLastHours class"""

        # Initialize members of the class
        self.last_hours = last_hours
        self.nfs_protocol_value = nfs_protocol_value
        self.s3_protocol_value = s3_protocol_value
        self.smb_protocol_value = smb_protocol_value
        self.value = value

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
        last_hours = dictionary.get('lastHours')
        nfs_protocol_value = dictionary.get('nfsProtocolValue')
        s3_protocol_value = dictionary.get('s3ProtocolValue')
        smb_protocol_value = dictionary.get('smbProtocolValue')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(
            last_hours,
            nfs_protocol_value,
            s3_protocol_value,
            smb_protocol_value,
            value
)