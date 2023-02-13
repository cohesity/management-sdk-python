# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AcropolisRestoreParameters(object):

    """Implementation of the 'AcropolisRestoreParameters' model.

    This field defines the Acropolis specific params for restore tasks of
    type
    kRecoverVMs.

    Attributes:
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
        powered_on (bool): Specifies the power state of the cloned or
            recovered objects. By default, the cloned or recovered objects are
            powered off.
        prefix (string): Specifies a prefix to prepended to the source object
            name to derive a new name for the recovered or cloned object. By
            default, cloned or recovered objects retain their original name.
            Length of this field is limited to 8 characters.
        storage_container_id (long|int): A storage container where the VM's
            files should be restored to. This field is optional if the VM is
            being restored to its original parent source. If not specified,
            the VM's files will be restored to their original storage
            container(s). This field is mandatory if the VMs are being
            restored to a different parent source.
        suffix (string): Specifies a suffix to appended to the original source
            object name to derive a new name for the recovered or cloned
            object. By default, cloned or recovered objects retain their
            original name. Length of this field is limited to 8 characters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_network":'disableNetwork',
        "network_id":'networkId',
        "powered_on":'poweredOn',
        "prefix":'prefix',
        "storage_container_id":'storageContainerId',
        "suffix":'suffix'
    }

    def __init__(self,
                 disable_network=None,
                 network_id=None,
                 powered_on=None,
                 prefix=None,
                 storage_container_id=None,
                 suffix=None):
        """Constructor for the AcropolisRestoreParameters class"""

        # Initialize members of the class
        self.disable_network = disable_network
        self.network_id = network_id
        self.powered_on = powered_on
        self.prefix = prefix
        self.storage_container_id = storage_container_id
        self.suffix = suffix


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
        disable_network = dictionary.get('disableNetwork')
        network_id = dictionary.get('networkId')
        powered_on = dictionary.get('poweredOn')
        prefix = dictionary.get('prefix')
        storage_container_id = dictionary.get('storageContainerId')
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(disable_network,
                   network_id,
                   powered_on,
                   prefix,
                   storage_container_id,
                   suffix)


