# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_qo_s_mapping_qo_s_context

class ClusterConfigProtoQoSMapping(object):

    """Implementation of the 'ClusterConfigProto_QoSMapping' model.

    If a new enum value is added to either QoSMapping.Type or
    QoSPrincipal.Priority in a future version, direct upgrades must be
    disallowed from a pre-2.5 version to that version (without upgrading to
    2.5 first). Contact nexus team for getting an appropriate restriction
    into
    the upgrade compatibility list.

    Attributes:
        principal_id (long|int): Principal id of the QoS principal to which
            qos_context maps to.
        qos_context (ClusterConfigProtoQoSMappingQoSContext): QoSContext
            captures the properties that are relevant for QoS in a request. If
            a new field is added to QoSContext, cluster_config.h should be
            changed to enhance the hasher (QoSContextHash) and comparator
            (QoSContextEqual) for QoSContext.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "principal_id":'principalId',
        "qos_context":'qosContext'
    }

    def __init__(self,
                 principal_id=None,
                 qos_context=None):
        """Constructor for the ClusterConfigProtoQoSMapping class"""

        # Initialize members of the class
        self.principal_id = principal_id
        self.qos_context = qos_context


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
        principal_id = dictionary.get('principalId')
        qos_context = cohesity_management_sdk.models.cluster_config_proto_qo_s_mapping_qo_s_context.ClusterConfigProtoQoSMappingQoSContext.from_dictionary(dictionary.get('qosContext')) if dictionary.get('qosContext') else None

        # Return an object of this model
        return cls(principal_id,
                   qos_context)


