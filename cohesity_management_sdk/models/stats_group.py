# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.consumer

class StatsGroup(object):

    """Implementation of the 'StatsGroup' model.

    StatsGroup describes the details of a stats group. A stats group is a
    basic
    group of usage stats, it is the usage of a tenant within a storage domain
    may also for a specific consumer type.

    Attributes:
        consumer (Consumer): Consumer is the storage consumer of a group.
        entity_id (string): Specifies the entity id of the group.
        id (long|int): Specifies the id of the group.
        name (string): Specifies the name of the group.
        tenant_id (string): Specifies the id of the organization (tenant) with
            respect to this group.
        tenant_name (string): Specifies the name of the organization (tenant)
            with respect to this group.
        view_box_id (long|int): Specifies the id of the view box (storage
            domain) with respect to this group.
        view_box_name (string): Specifies the name of the view box (storage
            domain) with respect to this group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "consumer":'consumer',
        "entity_id":'entityId',
        "id":'id',
        "name":'name',
        "tenant_id":'tenantId',
        "tenant_name":'tenantName',
        "view_box_id":'viewBoxId',
        "view_box_name":'viewBoxName'
    }

    def __init__(self,
                 consumer=None,
                 entity_id=None,
                 id=None,
                 name=None,
                 tenant_id=None,
                 tenant_name=None,
                 view_box_id=None,
                 view_box_name=None):
        """Constructor for the StatsGroup class"""

        # Initialize members of the class
        self.consumer = consumer
        self.entity_id = entity_id
        self.id = id
        self.name = name
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.view_box_id = view_box_id
        self.view_box_name = view_box_name


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
        consumer = cohesity_management_sdk.models.consumer.Consumer.from_dictionary(dictionary.get('consumer')) if dictionary.get('consumer') else None
        entity_id = dictionary.get('entityId')
        id = dictionary.get('id')
        name = dictionary.get('name')
        tenant_id = dictionary.get('tenantId')
        tenant_name = dictionary.get('tenantName')
        view_box_id = dictionary.get('viewBoxId')
        view_box_name = dictionary.get('viewBoxName')

        # Return an object of this model
        return cls(consumer,
                   entity_id,
                   id,
                   name,
                   tenant_id,
                   tenant_name,
                   view_box_id,
                   view_box_name)


