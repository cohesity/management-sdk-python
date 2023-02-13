# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_restore_status
import cohesity_management_sdk.models.ad_update_restore_task_options
import cohesity_management_sdk.models.credentials

class RestoreADAppObjectParams(object):

    """Implementation of the 'RestoreADAppObjectParams' model.

    TODO: type model description here.

    Attributes:
        ad_restore_status_vec (list of ADRestoreStatus): Status of the AD
            object/attribute restore operation.
        ad_update_options (ADUpdateRestoreTaskOptions): TODO: type description
            here.
        credentials (Credentials): Specifies credentials to access a target
            source.
        ldap_port (int): The ldap port on which the AD domain controller's
            NTDS database will be mounted.
        num_failed (int): Number of AD objects whose restore failed. Includes
            both AD object and attribute restored.
        num_running (int): Number of AD objects whose restores are currently
            running. Includes both AD object and attribute recoveries.
        num_successfull (int): Number of AD objects restored successfully.
            Includes both AD object and attribute restored.
        should_mount_and_restore (bool): The following field is set if user
            wants to mount AD, restore AD objects and destory AD mount in
            single task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_restore_status_vec":'adRestoreStatusVec',
        "ad_update_options":'adUpdateOptions',
        "credentials":'credentials',
        "ldap_port":'ldapPort',
        "num_failed":'numFailed',
        "num_running":'numRunning',
        "num_successfull":'numSuccessfull',
        "should_mount_and_restore":'shouldMountAndRestore'
    }

    def __init__(self,
                 ad_restore_status_vec=None,
                 ad_update_options=None,
                 credentials=None,
                 ldap_port=None,
                 num_failed=None,
                 num_running=None,
                 num_successfull=None,
                 should_mount_and_restore=None):
        """Constructor for the RestoreADAppObjectParams class"""

        # Initialize members of the class
        self.ad_restore_status_vec = ad_restore_status_vec
        self.ad_update_options = ad_update_options
        self.credentials = credentials
        self.ldap_port = ldap_port
        self.num_failed = num_failed
        self.num_running = num_running
        self.num_successfull = num_successfull
        self.should_mount_and_restore = should_mount_and_restore


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
        ad_restore_status_vec = None
        if dictionary.get('adRestoreStatusVec') != None:
            ad_restore_status_vec = list()
            for structure in dictionary.get('adRestoreStatusVec'):
                ad_restore_status_vec.append(cohesity_management_sdk.models.ad_restore_status.ADRestoreStatus.from_dictionary(structure))
        ad_update_options = cohesity_management_sdk.models.ad_update_restore_task_options.ADUpdateRestoreTaskOptions.from_dictionary(dictionary.get('adUpdateOptions')) if dictionary.get('adUpdateOptions') else None
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        ldap_port = dictionary.get('ldapPort')
        num_failed = dictionary.get('numFailed')
        num_running = dictionary.get('numRunning')
        num_successfull = dictionary.get('numSuccessfull')
        should_mount_and_restore = dictionary.get('shouldMountAndRestore')

        # Return an object of this model
        return cls(ad_restore_status_vec,
                   ad_update_options,
                   credentials,
                   ldap_port,
                   num_failed,
                   num_running,
                   num_successfull,
                   should_mount_and_restore)


