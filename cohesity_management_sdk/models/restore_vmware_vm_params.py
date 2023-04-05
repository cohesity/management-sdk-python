# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto


class RestoreVMwareVMParams(object):

    """Implementation of the 'RestoreVMwareVMParams' model.

    TODO: type description here.


    Attributes:

        allow_nbdssl_transport_fallback (bool): Whether to fallback to use
            NBDSSL transport for recovery in case using SAN transport recovery
            fails.
        attempt_differential_restore (bool): This field is only applicable when
            overwrite_existing_vm is set to true. If this field is true, as
            part of overwrite existing vm, differential restore will be
            attempted.
        catalog_uuid (string): Specifies the name of the catalog for vapp
            template recovery. This is applicable for recovery to a VCD.
        copy_recovery (bool): Whether to perform copy recovery instead of
            instant recovery.
        datastore_entity_vec (list of EntityProto): Datastore entities if the
            restore is to alternate location.
        disk_provision_type (int): This specifies vmware virtual disk
            provisioning policies
        is_on_prem_deploy (bool): This will be true if this is on prem deploy
            task. attempt_differential_restore should also be set to true in
            case of doing on prem deploy.
        org_vdc_network_name (string): Specifies the name of the org VDC
            network to be used for the recovery. This is applicable for
            recovery to a VCD.
        org_vdc_network_vcd_uuid (string): Specifies the VCD UUID of the org
            VDC network to be used for the recovery. This is applicable for
            recovery to a VCD.
        overwrite_existing_vm (bool): This option is only potentially populated
            in the case that there are no rename parameters specified for a
            recovery. Note that this option is mutually exclusive with
            power_off_and_rename_existing_vm.
        power_off_and_rename_existing_vm (bool): This option is only
            potentially populated in the case that there are no rename
            parameters specified for a recovery. Note that this option is
            mutually exclusive with overwrite_existing_vm.
        preserve_custom_attributes_during_clone (bool): Whether to preserve
            custom attributes for the clone op.
        preserve_tags_during_clone (bool): Whether to preserve tags for the
            clone op.
        resource_pool_entity (EntityProto): Resource pool entity if the restore
            is to alternate location.
        storage_profile_name (string): This is only populated for VCD restore
            to alternate location. It contains the name of the destination
            storage profile.
        storage_profile_vcd_uuid (string): This is only populated for VCD
            restore to alternate location. It contains the vcd uuid of the
            destination storage profile.
        target_datastore_folder (EntityProto): Folder where the restore
            datastore should be created. This is applicable only when the VMs
            are being cloned.
        target_vm_folder (EntityProto): Folder where the VMs should be created.
            This is applicable only when the VMs are being restored to an
            alternate location or if clone is being performed.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "allow_nbdssl_transport_fallback":'allowNbdsslTransportFallback',
        "attempt_differential_restore":'attemptDifferentialRestore',
        "catalog_uuid":'catalogUuid',
        "copy_recovery":'copyRecovery',
        "datastore_entity_vec":'datastoreEntityVec',
        "disk_provision_type":'diskProvisionType',
        "is_on_prem_deploy":'isOnPremDeploy',
        "org_vdc_network_name":'orgVdcNetworkName',
        "org_vdc_network_vcd_uuid":'orgVdcNetworkVcdUuid',
        "overwrite_existing_vm":'overwriteExistingVm',
        "power_off_and_rename_existing_vm":'powerOffAndRenameExistingVm',
        "preserve_custom_attributes_during_clone":'preserveCustomAttributesDuringClone',
        "preserve_tags_during_clone":'preserveTagsDuringClone',
        "resource_pool_entity":'resourcePoolEntity',
        "storage_profile_name":'storageProfileName',
        "storage_profile_vcd_uuid":'storageProfileVcdUuid',
        "target_datastore_folder":'targetDatastoreFolder',
        "target_vm_folder":'targetVmFolder',
    }
    def __init__(self,
                 allow_nbdssl_transport_fallback=None,
                 attempt_differential_restore=None,
                 catalog_uuid=None,
                 copy_recovery=None,
                 datastore_entity_vec=None,
                 disk_provision_type=None,
                 is_on_prem_deploy=None,
                 org_vdc_network_name=None,
                 org_vdc_network_vcd_uuid=None,
                 overwrite_existing_vm=None,
                 power_off_and_rename_existing_vm=None,
                 preserve_custom_attributes_during_clone=None,
                 preserve_tags_during_clone=None,
                 resource_pool_entity=None,
                 storage_profile_name=None,
                 storage_profile_vcd_uuid=None,
                 target_datastore_folder=None,
                 target_vm_folder=None,
            ):

        """Constructor for the RestoreVMwareVMParams class"""

        # Initialize members of the class
        self.allow_nbdssl_transport_fallback = allow_nbdssl_transport_fallback
        self.attempt_differential_restore = attempt_differential_restore
        self.catalog_uuid = catalog_uuid
        self.copy_recovery = copy_recovery
        self.datastore_entity_vec = datastore_entity_vec
        self.disk_provision_type = disk_provision_type
        self.is_on_prem_deploy = is_on_prem_deploy
        self.org_vdc_network_name = org_vdc_network_name
        self.org_vdc_network_vcd_uuid = org_vdc_network_vcd_uuid
        self.overwrite_existing_vm = overwrite_existing_vm
        self.power_off_and_rename_existing_vm = power_off_and_rename_existing_vm
        self.preserve_custom_attributes_during_clone = preserve_custom_attributes_during_clone
        self.preserve_tags_during_clone = preserve_tags_during_clone
        self.resource_pool_entity = resource_pool_entity
        self.storage_profile_name = storage_profile_name
        self.storage_profile_vcd_uuid = storage_profile_vcd_uuid
        self.target_datastore_folder = target_datastore_folder
        self.target_vm_folder = target_vm_folder

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
        allow_nbdssl_transport_fallback = dictionary.get('allowNbdsslTransportFallback')
        attempt_differential_restore = dictionary.get('attemptDifferentialRestore')
        catalog_uuid = dictionary.get('catalogUuid')
        copy_recovery = dictionary.get('copyRecovery')
        datastore_entity_vec = None
        if dictionary.get('datastoreEntityVec') != None:
            datastore_entity_vec = list()
            for structure in dictionary.get('datastoreEntityVec'):
                datastore_entity_vec.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))
        disk_provision_type = dictionary.get('diskProvisionType')
        is_on_prem_deploy = dictionary.get('isOnPremDeploy')
        org_vdc_network_name = dictionary.get('orgVdcNetworkName')
        org_vdc_network_vcd_uuid = dictionary.get('orgVdcNetworkVcdUuid')
        overwrite_existing_vm = dictionary.get('overwriteExistingVm')
        power_off_and_rename_existing_vm = dictionary.get('powerOffAndRenameExistingVm')
        preserve_custom_attributes_during_clone = dictionary.get('preserveCustomAttributesDuringClone')
        preserve_tags_during_clone = dictionary.get('preserveTagsDuringClone')
        resource_pool_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourcePoolEntity')) if dictionary.get('resourcePoolEntity') else None
        storage_profile_name = dictionary.get('storageProfileName')
        storage_profile_vcd_uuid = dictionary.get('storageProfileVcdUuid')
        target_datastore_folder = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetDatastoreFolder')) if dictionary.get('targetDatastoreFolder') else None
        target_vm_folder = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetVmFolder')) if dictionary.get('targetVmFolder') else None

        # Return an object of this model
        return cls(
            allow_nbdssl_transport_fallback,
            attempt_differential_restore,
            catalog_uuid,
            copy_recovery,
            datastore_entity_vec,
            disk_provision_type,
            is_on_prem_deploy,
            org_vdc_network_name,
            org_vdc_network_vcd_uuid,
            overwrite_existing_vm,
            power_off_and_rename_existing_vm,
            preserve_custom_attributes_during_clone,
            preserve_tags_during_clone,
            resource_pool_entity,
            storage_profile_name,
            storage_profile_vcd_uuid,
            target_datastore_folder,
            target_vm_folder
)