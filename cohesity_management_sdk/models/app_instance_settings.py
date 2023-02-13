# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protected_object_privileges
import cohesity_management_sdk.models.view_privileges
import cohesity_management_sdk.models.external_network_info
import cohesity_management_sdk.models.vm_num_replicas

class AppInstanceSettings(object):

    """Implementation of the 'AppInstanceSettings' model.

    AppInstanceSettings provides settings used while launching an app
    instance.
    Current settings include QoSTier to be used for the instance and views
    allowed to be accessed by the instance.

    Attributes:
        external_network_info (ExternalNetworkInfo): External network
            information of the app instance.
        instance_size (string): Instance size specification (e.g.
            small/medium/large). Used to determine container resources.
        protected_object_privileges (ProtectedObjectPrivileges): Specifies
            which protected objects are allowed to be accessed by an app
            instance.
        qos_tier (QosTierAppInstanceSettingsEnum):  Specifies QoSTier of the
            app instance.
            Specifies QoS Tier for an app instance. App instances are
            allocated resources such as memory, CPU and IO based on their QoS
            Tier.
            kLow - Low QoS Tier.
            kMedium - Medium QoS Tier.
            kHigh - High QoS Tier.
            kMax - Max QoS Tier.
        read_view_privileges (ViewPrivileges): Specifies views allowed to be
            accessed in read only mode by the app instance.
        read_write_view_privileges (ViewPrivileges): Specifies views allowed
            to be accessed in read/write mode by the app instance.
        vm_num_replicas_list(list of VmNumReplicas): List of vm-name,
            replica count pairs to be used at the time of app instance launch.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "external_network_info":'externalNetworkInfo',
        "instance_size":'instanceSize',
        "protected_object_privileges":'protectedObjectPrivileges',
        "qos_tier":'qosTier',
        "read_view_privileges":'readViewPrivileges',
        "read_write_view_privileges":'readWriteViewPrivileges',
        "vm_num_replicas_list":'vmNumReplicasList'
    }

    def __init__(self,
                 external_network_info=None,
                 instance_size=None,
                 protected_object_privileges=None,
                 qos_tier=None,
                 read_view_privileges=None,
                 read_write_view_privileges=None,
                 vm_num_replicas_list=None):
        """Constructor for the AppInstanceSettings class"""

        # Initialize members of the class
        self.external_network_info = external_network_info
        self.instance_size = instance_size
        self.protected_object_privileges = protected_object_privileges
        self.qos_tier = qos_tier
        self.read_view_privileges = read_view_privileges
        self.read_write_view_privileges = read_write_view_privileges
        self.vm_num_replicas_list = vm_num_replicas_list


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
        external_network_info = cohesity_management_sdk.models.external_network_info.ExternalNetworkInfo.from_dictionary(dictionary.get('externalNetworkInfo')) if dictionary.get('externalNetworkInfo') else None
        instance_size = dictionary.get('instanceSize')
        protected_object_privileges = cohesity_management_sdk.models.protected_object_privileges.ProtectedObjectPrivileges.from_dictionary(dictionary.get('protectedObjectPrivileges')) if dictionary.get('protectedObjectPrivileges') else None
        qos_tier = dictionary.get('qosTier')
        read_view_privileges = cohesity_management_sdk.models.view_privileges.ViewPrivileges.from_dictionary(dictionary.get('readViewPrivileges')) if dictionary.get('readViewPrivileges') else None
        read_write_view_privileges = cohesity_management_sdk.models.view_privileges.ViewPrivileges.from_dictionary(dictionary.get('readWriteViewPrivileges')) if dictionary.get('readWriteViewPrivileges') else None
        vm_num_replicas_list = None
        if dictionary.get('vmNumReplicasList') != None:
            vm_num_replicas_list = list()
            for structure in dictionary.get('vmNumReplicasList'):
                vm_num_replicas_list.append(cohesity_management_sdk.models.vm_num_replicas.VmNumReplicas.from_dictionary(structure))

        # Return an object of this model
        return cls(external_network_info,
                   instance_size,
                   protected_object_privileges,
                   qos_tier,
                   read_view_privileges,
                   read_write_view_privileges,
                   vm_num_replicas_list)


