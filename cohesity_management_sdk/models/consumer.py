# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Consumer(object):

    """Implementation of the 'Consumer' model.

    Consumer is the storage consumer of a group.

    Attributes:
        id (long|int): Specifies the id of the consumer.
        name (string): Specifies the name of the consumer.
        mtype (TypeConsumerEnum): Specifies the type of the consumer. Type of
            the consumer can be one of the following three,  'kViews',
            indicates the stats info of Views used per organization (tenant)
            per view box (storage domain). 'kProtectionRuns', indicates the
            stats info of Protection Runs used per organization (tenant) per
            view box (storage domain). 'kReplicationRuns', indicates the stats
            info of Replication In used per organization (tenant) per view box
            (storage domain). 'kViewProtectionRuns', indicates the stats info
            of View Protection Runs used per organization (tenant) per view
            box (storage domain).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "mtype":'type'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 mtype=None):
        """Constructor for the Consumer class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.mtype = mtype


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
        id = dictionary.get('id')
        name = dictionary.get('name')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(id,
                   name,
                   mtype)


