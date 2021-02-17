# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class UdaRecoverJobParams(object):

    """Implementation of the 'UdaRecoverJobParams' model.

    Specifies an Object representing Universal Data Adapter.

    Attributes:
        concurrency (int): Number of parallel streams to use for the restore.
        local_mount_dir (string): Directory on the host where views will be
            mounted.
        mounts (int): Max number of view mounts to use for the restore.
        restore_args (string): Custom arguments which are applicable to the
            objects to be restored.
        script_dir (string): Path where the source scripts will be located.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "concurrency":'concurrency',
        "local_mount_dir":'localMountDir',
        "mounts":'mounts',
        "restore_args":'restoreArgs',
        "script_dir":'scriptDir'
    }

    def __init__(self,
                 concurrency=None,
                 local_mount_dir=None,
                 mounts=None,
                 restore_args=None,
                 script_dir=None):
        """Constructor for the UdaRecoverJobParams class"""

        # Initialize members of the class
        self.concurrency = concurrency
        self.local_mount_dir = local_mount_dir
        self.mounts = mounts
        self.restore_args = restore_args
        self.script_dir = script_dir


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
        concurrency = dictionary.get('concurrency')
        local_mount_dir = dictionary.get('localMountDir')
        mounts = dictionary.get('mounts')
        restore_args = dictionary.get('restoreArgs')
        script_dir = dictionary.get('scriptDir')

        # Return an object of this model
        return cls(concurrency,
                   local_mount_dir,
                   mounts,
                   restore_args,
                   script_dir)


