# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.network_mapping

class VmwareRestoreParameters(object):

    """Implementation of the 'VmwareRestoreParameters' model.

    Specifies the information required for recovering or cloning VmWare VMs.

    Attributes:
        additional_datastore_ids (list of long|int): Specifies additional
            datastores where the object should be recovered to.
        datastore_folder_id (long|int): Specifies the folder where the restore
            datastore should be created. This is applicable only when the VMs
            are being cloned.
        datastore_id (long|int): Specifies the datastore where the object's
            files should be recovered to. This field is mandatory to recover
            objects to a different resource pool or to a different parent
            source. If not specified, objects are recovered to their original
            datastore locations in the parent source.
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
        resource_pool_id (long|int): Specifies the resource pool where the
            cloned or recovered objects are attached. This field is mandatory
            for kCloneVMs Restore Tasks always. For kRecoverVMs Restore Tasks,
            this field is mandatory only if newParentId field is specified. If
            this field is not specified, recovered objects are attached to the
            original resource pool under the original parent.
        suffix (string): Specifies a suffix to appended to the original source
            object name to derive a new name for the recovered or cloned
            object. By default, cloned or recovered objects retain their
            original name. Length of this field is limited to 8 characters.
        vm_folder_id (long|int): Specifies a folder where the VMs should be
            restored. This is applicable only when the VMs are being restored
            to an alternate location or if clone is being performed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_datastore_ids":'additionalDatastoreIds',
        "datastore_folder_id":'datastoreFolderId',
        "datastore_id":'datastoreId',
        "detach_network":'detachNetwork',
        "disable_network":'disableNetwork',
        "network_id":'networkId',
        "network_mappings":'networkMappings',
        "powered_on":'poweredOn',
        "prefix":'prefix',
        "preserve_custom_attributes_during_clone":'preserveCustomAttributesDuringClone',
        "preserve_tags":'preserveTags',
        "resource_pool_id":'resourcePoolId',
        "suffix":'suffix',
        "vm_folder_id":'vmFolderId'
    }

    def __init__(self,
                 additional_datastore_ids=None,
                 datastore_folder_id=None,
                 datastore_id=None,
                 detach_network=None,
                 disable_network=None,
                 network_id=None,
                 network_mappings=None,
                 powered_on=None,
                 prefix=None,
                 preserve_custom_attributes_during_clone=None,
                 preserve_tags=None,
                 resource_pool_id=None,
                 suffix=None,
                 vm_folder_id=None):
        """Constructor for the VmwareRestoreParameters class"""

        # Initialize members of the class
        self.additional_datastore_ids = additional_datastore_ids
        self.datastore_folder_id = datastore_folder_id
        self.datastore_id = datastore_id
        self.detach_network = detach_network
        self.disable_network = disable_network
        self.network_id = network_id
        self.network_mappings = network_mappings
        self.powered_on = powered_on
        self.prefix = prefix
        self.preserve_custom_attributes_during_clone = preserve_custom_attributes_during_clone
        self.preserve_tags = preserve_tags
        self.resource_pool_id = resource_pool_id
        self.suffix = suffix
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
        additional_datastore_ids = dictionary.get('additionalDatastoreIds')
        datastore_folder_id = dictionary.get('datastoreFolderId')
        datastore_id = dictionary.get('datastoreId')
        detach_network = dictionary.get('detachNetwork')
        disable_network = dictionary.get('disableNetwork')
        network_id = dictionary.get('networkId')
        network_mappings = None
        if dictionary.get('networkMappings') != None:
            network_mappings = list()
            for structure in dictionary.get('networkMappings'):
                network_mappings.append(cohesity_management_sdk.models.network_mapping.NetworkMapping.from_dictionary(structure))
        powered_on = dictionary.get('poweredOn')
        prefix = dictionary.get('prefix')
        preserve_custom_attributes_during_clone = dictionary.get('preserveCustomAttributesDuringClone')
        preserve_tags = dictionary.get('preserveTags')
        resource_pool_id = dictionary.get('resourcePoolId')
        suffix = dictionary.get('suffix')
        vm_folder_id = dictionary.get('vmFolderId')

        # Return an object of this model
        return cls(additional_datastore_ids,
                   datastore_folder_id,
                   datastore_id,
                   detach_network,
                   disable_network,
                   network_id,
                   network_mappings,
                   powered_on,
                   prefix,
                   preserve_custom_attributes_during_clone,
                   preserve_tags,
                   resource_pool_id,
                   suffix,
                   vm_folder_id)


