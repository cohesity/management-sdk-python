# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterConfigProtoQoSMappingQoSContext(object):

    """Implementation of the 'ClusterConfigProto_QoSMapping_QoSContext' model.

    QoSContext captures the properties that are relevant for QoS in a
    request. If a new field is added to QoSContext, cluster_config.h should
    be changed to enhance the hasher (QoSContextHash) and comparator
    (QoSContextEqual) for QoSContext.

    Attributes:
        component (int): Component from which request is coming.
        priority (int): Priority of a request.
        mtype (int): TODO: type description here.
        view_box_id (long|int): View box id of a request.
        view_id (long|int): View id of a request.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component":'component',
        "priority":'priority',
        "mtype":'type',
        "view_box_id":'viewBoxId',
        "view_id":'viewId'
    }

    def __init__(self,
                 component=None,
                 priority=None,
                 mtype=None,
                 view_box_id=None,
                 view_id=None):
        """Constructor for the ClusterConfigProtoQoSMappingQoSContext class"""

        # Initialize members of the class
        self.component = component
        self.priority = priority
        self.mtype = mtype
        self.view_box_id = view_box_id
        self.view_id = view_id


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
        component = dictionary.get('component')
        priority = dictionary.get('priority')
        mtype = dictionary.get('type')
        view_box_id = dictionary.get('viewBoxId')
        view_id = dictionary.get('viewId')

        # Return an object of this model
        return cls(component,
                   priority,
                   mtype,
                   view_box_id,
                   view_id)


