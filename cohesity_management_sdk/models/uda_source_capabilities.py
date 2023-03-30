# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UdaSourceCapabilities(object):

    """Implementation of the 'UdaSourceCapabilities' model.

    TODO: type description here.


    Attributes:

        auto_log_backup (bool): TODO: Type description here.
        dynamic_config (bool): Specifies whether the source supports the
            'Dynamic Configuration' capability.
        entity_support (bool): Indicates if source has entity capability.
        full_backup (bool): TODO: Type description here.
        incr_backup (bool): TODO: Type description here.
        log_backup (bool): TODO: Type description here.
        multi_object_restore (bool): Whether the source supports restore of
            multiple objects.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "auto_log_backup":'autoLogBackup',
        "dynamic_config":'dynamicConfig',
        "entity_support":'entitySupport',
        "full_backup":'fullBackup',
        "incr_backup":'incrBackup',
        "log_backup":'logBackup',
        "multi_object_restore":'multiObjectRestore',
    }
    def __init__(self,
                 auto_log_backup=None,
                 dynamic_config=None,
                 entity_support=None,
                 full_backup=None,
                 incr_backup=None,
                 log_backup=None,
                 multi_object_restore=None,
            ):

        """Constructor for the UdaSourceCapabilities class"""

        # Initialize members of the class
        self.auto_log_backup = auto_log_backup
        self.dynamic_config = dynamic_config
        self.entity_support = entity_support
        self.full_backup = full_backup
        self.incr_backup = incr_backup
        self.log_backup = log_backup
        self.multi_object_restore = multi_object_restore

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
        dynamic_config = dictionary.get('dynamicConfig')
        entity_support = dictionary.get('entitySupport')
        full_backup = dictionary.get('fullBackup')
        incr_backup = dictionary.get('incrBackup')
        log_backup = dictionary.get('logBackup')
        multi_object_restore = dictionary.get('multiObjectRestore')

        # Return an object of this model
        return cls(
            auto_log_backup,
            dynamic_config,
            entity_support,
            full_backup,
            incr_backup,
            log_backup,
            multi_object_restore
)