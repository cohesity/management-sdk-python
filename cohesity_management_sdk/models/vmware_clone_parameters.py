# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.network_mapping
import cohesity_management_sdk.models.org_vdc_network

class VmwareCloneParameters(object):

    """Implementation of the 'VmwareCloneParameters' model.

    Specifies the information required for recovering or cloning VmWare VMs.

    Attributes:
        attempt_differential_restore (bool): Specifies whether to attempt
            differential restore.
        datastore_folder_id (long|int): Specifies the folder where the restore
            datastore should be created. This is applicable only when the VMs
            are being cloned.
        detach_network (bool): Specifies whether the network should be
            detached from the recovered or cloned VMs.
        disable_network (bool): Specifies whether the network should be left
            in disabled state. Attached network is enabled by default. Set
            this flag to true to disable it.
        network_id (long|int): Specifies a network configuration to be
            attached to the cloned or recovered object. For kCloneVMs and
            kRecoverVMs tasks, original network configuration is detached if
            the cloned or recovered object is kept under a different parent
            Protection Source or a different Resource Pool. By default, for
            kRecoverVMs task, original network configuration is preserved if
            the recovered object is kept under the same parent Protection
            Source and the same Resource Pool. Specify this field to override
            the preserved network configuration or to attach a new network
            configuration to the cloned or recovered objects. You can get the
            networkId of the kNetwork object by setting includeNetworks to
            'true' in the GET /public/protectionSources operation. In the
            response, get the id of the desired kNetwork object, the resource
            pool, and the registered parent Protection Source.
        network_mappings (list of NetworkMapping): Specifies the parameters
            for mapping the source and target networks. This field can be used
            if restoring to a different parent source. This will replace the
            NetworkId and DisableNetwork that are used to provide
            configuration for a single network. Unless the support for mapping
            is available for all the entities old keys can be used to attach a
            new network. Supports 'kVMware' for now.
        org_vdc_network (OrgVdcNetwork): Specifies the Org VDC Network to be
            used for this recovery.
        overwrite_existing_vm (bool): Specifies whether to overwrite the
            existing VM for a recovery when rename parameters are not given.
        power_off_and_rename_existing_vm (bool): Specifies whether to power off
            and rename the existing VM as deprecated for recovery when rename
            parameters are not given.
        powered_on (bool): Specifies the power state of the cloned or
            recovered objects. By default, the cloned or recovered objects are
            powered off.
        prefix (string): Specifies a prefix to prepended to the source object
            name to derive a new name for the recovered or cloned object. By
            default, cloned or recovered objects retain their original name.
            Length of this field is limited to 8 characters.
        preserve_custom_attributes_during_clone (bool): Specifies whether or
            not to preserve the custom attributes during the clone operation.
            The default behavior is 'true'.
        preserve_tags (bool): Specifies whether or not to preserve tags during
            the clone operation. The default behavior is 'true'.
        recovery_process_type (RecoveryProcessTypeEnum): Specifies the type of
            recovery process to be performed. If unspecified, then an instant
            recovery will be performed. Specifies the recovery process type to
            be used.. 'kInstantRecovery' indicates that an instant recovery
            should be performed. 'kCopyRecovery' indicates that a copy
            recovery should be performed.
        resource_pool_id (long|int): Specifies the resource pool where the
            cloned or recovered objects are attached. This field is mandatory
            for kCloneVMs Restore Tasks always. For kRecoverVMs Restore Tasks,
            this field is mandatory only if newParentId field is specified. If
            this field is not specified, recovered objects are attached to the
            original resource pool under the original parent.
        storage_profile_name (string): Specifies the name of the destination
            storage profile while restoring to an alternate VCD location.
        storage_profile_vcd_uuid (string): Specifies the UUID of the storage
            profile while restoring to an alternate VCD location.
        suffix (string): Specifies a suffix to appended to the original source
            object name to derive a new name for the recovered or cloned
            object. By default, cloned or recovered objects retain their
            original name. Length of this field is limited to 8 characters.
        v_app_id (long|int): Specifies the ID of the vApp to which a VM should
            be restored.
        vdc_id (long|int): Specifies the ID of the VDC to which a VM should be
            restored.
        vm_folder_id (long|int): Specifies a folder where the VMs should be
            restored. This is applicable only when the VMs are being restored
            to an alternate location or if clone is being performed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attempt_differential_restore":'attemptDifferentialRestore',
        "datastore_folder_id":'datastoreFolderId',
        "detach_network":'detachNetwork',
        "disable_network":'disableNetwork',
        "network_id":'networkId',
        "network_mappings":'networkMappings',
        "org_vdc_network":'orgVdcNetwork',
        "overwrite_existing_vm":'overwriteExistingVm',
        "power_off_and_rename_existing_vm":'powerOffAndRenameExistingVm',
        "powered_on":'poweredOn',
        "prefix":'prefix',
        "preserve_custom_attributes_during_clone":'preserveCustomAttributesDuringClone',
        "preserve_tags":'preserveTags',
        "recovery_process_type":'recoveryProcessType',
        "resource_pool_id":'resourcePoolId',
        "storage_profile_name":'storageProfileName',
        "storage_profile_vcd_uuid":'storageProfileVcdUuid',
        "suffix":'suffix',
        "v_app_id":'vAppId',
        "vdc_id":'vdcId',
        "vm_folder_id":'vmFolderId'
    }

    def __init__(self,
                 attempt_differential_restore=None,
                 datastore_folder_id=None,
                 detach_network=None,
                 disable_network=None,
                 network_id=None,
                 network_mappings=None,
                 org_vdc_network=None,
                 overwrite_existing_vm=None,
                 power_off_and_rename_existing_vm=None,
                 powered_on=None,
                 prefix=None,
                 preserve_custom_attributes_during_clone=None,
                 preserve_tags=None,
                 recovery_process_type=None,
                 resource_pool_id=None,
                 storage_profile_name=None,
                 storage_profile_vcd_uuid=None,
                 suffix=None,
                 v_app_id=None,
                 vdc_id=None,
                 vm_folder_id=None):
        """Constructor for the VmwareCloneParameters class"""

        # Initialize members of the class
        self.attempt_differential_restore = attempt_differential_restore
        self.datastore_folder_id = datastore_folder_id
        self.detach_network = detach_network
        self.disable_network = disable_network
        self.network_id = network_id
        self.network_mappings = network_mappings
        self.org_vdc_network = org_vdc_network
        self.overwrite_existing_vm = overwrite_existing_vm
        self.power_off_and_rename_existing_vm = power_off_and_rename_existing_vm
        self.powered_on = powered_on
        self.prefix = prefix
        self.preserve_custom_attributes_during_clone = preserve_custom_attributes_during_clone
        self.preserve_tags = preserve_tags
        self.recovery_process_type = recovery_process_type
        self.resource_pool_id = resource_pool_id
        self.storage_profile_name = storage_profile_name
        self.storage_profile_vcd_uuid = storage_profile_vcd_uuid
        self.suffix = suffix
        self.v_app_id = v_app_id
        self.vdc_id = vdc_id
        self.vm_folder_id = vm_folder_id


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
        attempt_differential_restore = dictionary.get('attemptDifferentialRestore')
        datastore_folder_id = dictionary.get('datastoreFolderId')
        detach_network = dictionary.get('detachNetwork')
        disable_network = dictionary.get('disableNetwork')
        network_id = dictionary.get('networkId')
        network_mappings = None
        if dictionary.get('networkMappings') != None:
            network_mappings = list()
            for structure in dictionary.get('networkMappings'):
                network_mappings.append(cohesity_management_sdk.models.network_mapping.NetworkMapping.from_dictionary(structure))
        org_vdc_network = cohesity_management_sdk.models.org_vdc_network.OrgVdcNetwork.from_dictionary(dictionary.get('orgVdcNetwork')) if dictionary.get('orgVdcNetwork') else None
        overwrite_existing_vm = dictionary.get('overwriteExistingVm')
        power_off_and_rename_existing_vm = dictionary.get('powerOffAndRenameExistingVm')
        powered_on = dictionary.get('poweredOn')
        prefix = dictionary.get('prefix')
        preserve_custom_attributes_during_clone = dictionary.get('preserveCustomAttributesDuringClone')
        preserve_tags = dictionary.get('preserveTags')
        recovery_process_type = dictionary.get('recoveryProcessType')
        resource_pool_id = dictionary.get('resourcePoolId')
        storage_profile_name = dictionary.get('storageProfileName')
        storage_profile_vcd_uuid = dictionary.get('storageProfileVcdUuid')
        suffix = dictionary.get('suffix')
        v_app_id = dictionary.get('vAppId')
        vdc_id = dictionary.get('vdcId')
        vm_folder_id = dictionary.get('vmFolderId')

        # Return an object of this model
        return cls(attempt_differential_restore,
                   datastore_folder_id,
                   detach_network,
                   disable_network,
                   network_id,
                   network_mappings,
                   org_vdc_network,
                   overwrite_existing_vm,
                   power_off_and_rename_existing_vm,
                   powered_on,
                   prefix,
                   preserve_custom_attributes_during_clone,
                   preserve_tags,
                   recovery_process_type,
                   resource_pool_id,
                   storage_profile_name,
                   storage_profile_vcd_uuid,
                   suffix,
                   v_app_id,
                   vdc_id,
                   vm_folder_id)


