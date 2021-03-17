# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.


class UdaSourceCapabilities(object):

    """Implementation of the 'UdaSourceCapabilities' model.

    Attributes:
        auto_log_backup (bool): TODO: Type description here.
        full_backup (bool): TODO: Type description here.
        incr_backup (bool): TODO: Type description here.
        log_backup (bool): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_log_backup":'autoLogBackup',
        "full_backup":'fullBackup',
        "incr_backup":'incrBackup',
        "log_backup":'logBackup'
    }

    def __init__(self,
                 auto_log_backup=None,
                 full_backup=None,
                 incr_backup=None,
                 log_backup=None):
        """Constructor for the UdaSourceCapabilities class"""

        # Initialize members of the class
        self.auto_log_backup = auto_log_backup
        self.full_backup = full_backup
        self.incr_backup = incr_backup
        self.log_backup = log_backup


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
        auto_log_backup = dictionary.get('autoLogBackup')
        full_backup = dictionary.get('fullBackup')
        incr_backup = dictionary.get('incrBackup')
        log_backup = dictionary.get('logBackup')

        # Return an object of this model
        return cls(auto_log_backup,
                   full_backup,
                   incr_backup,
                   log_backup)


