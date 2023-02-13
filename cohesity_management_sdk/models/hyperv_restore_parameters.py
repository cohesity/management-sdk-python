# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HypervRestoreParameters(object):

    """Implementation of the 'HypervRestoreParameters' model.

    Specifies information needed when restoring VMs in HyperV enviroment.
    This field defines the HyperV specific params for restore tasks of type
    kRecoverVMs.

    Attributes:
        datastore_id (long|int): A datastore entity where the object's files
            should be restored to. This field is optional if object is being
            restored to its original parent source. If not specified, the
            object's files will be restored to their original datastore
            locations. This field is mandatory if object is being restored to
            a different resource entity or to a different parent source.
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
        preserve_tags (bool): Specifies whether or not to preserve tags during
            the operation.
        resource_id (long|int): The resource (HyperV host) to which the
            restored VM will be attached.  This field is optional for a
            kRecoverVMs task if the VMs are being restored to its original
            parent source. If not specified, restored VMs will be attached to
            its original host. This field is mandatory if the VMs are being
            restored to a different parent source.
        suffix (string): Specifies a suffix to appended to the original source
            object name to derive a new name for the recovered or cloned
            object. By default, cloned or recovered objects retain their
            original name. Length of this field is limited to 8 characters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "datastore_id":'datastoreId',
        "disable_network":'disableNetwork',
        "network_id":'networkId',
        "powered_on":'poweredOn',
        "prefix":'prefix',
        "preserve_tags":'preserveTags',
        "resource_id":'resourceId',
        "suffix":'suffix'
    }

    def __init__(self,
                 datastore_id=None,
                 disable_network=None,
                 network_id=None,
                 powered_on=None,
                 prefix=None,
                 preserve_tags=None,
                 resource_id=None,
                 suffix=None):
        """Constructor for the HypervRestoreParameters class"""

        # Initialize members of the class
        self.datastore_id = datastore_id
        self.disable_network = disable_network
        self.network_id = network_id
        self.powered_on = powered_on
        self.prefix = prefix
        self.preserve_tags = preserve_tags
        self.resource_id = resource_id
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
        datastore_id = dictionary.get('datastoreId')
        disable_network = dictionary.get('disableNetwork')
        network_id = dictionary.get('networkId')
        powered_on = dictionary.get('poweredOn')
        prefix = dictionary.get('prefix')
        preserve_tags = dictionary.get('preserveTags', None)
        resource_id = dictionary.get('resourceId')
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(datastore_id,
                   disable_network,
                   network_id,
                   powered_on,
                   prefix,
                   preserve_tags,
                   resource_id,
                   suffix)


