# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class QoSPolicy(object):

    """Implementation of the 'QoSPolicy' model.

    Specifies the Quality of Service (QoS) Policy details.

    Attributes:
        always_use_ssd (bool): Specifies whether to always write to SSD even
            if SeqWriteSsdPct is 0.
        id (long|int): Specifies Id of the QoS Policy.
        min_requests (int): Specifies minimum number of requests,
            corresponding to this Policy, executed in the QoS queue.
        name (string): Specifies Name of the Qos Policy.
        priority (PriorityQoSPolicyEnum): Specifies Priority of the Qos
            Policy. Priority of QoS Policy as defined in cluster config
            proto.
        random_write_hydra_pct (int): Specifies percentage of a random write
            request belonging to this Policy that hits hydra.
        random_write_ssd_pct (int): Specifies percentage of a random write
            request belonging to this Policy that hits SSD.
        seq_write_hydra_pct (int): Specifies percentage of a sequential write
            request belonging to this Policy that hits hydra.
        seq_write_ssd_pct (int): Specifies percentage of a sequential write
            request belonging to this Policy that hits SSD.
        weight (int): Specifies Weight of the QoS Policy used in QoS queue.
        work_load_type (string): Specifies Workload type attribute associated
            with this Policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "always_use_ssd":'alwaysUseSsd',
        "id":'id',
        "min_requests":'minRequests',
        "name":'name',
        "priority":'priority',
        "random_write_hydra_pct":'randomWriteHydraPct',
        "random_write_ssd_pct":'randomWriteSsdPct',
        "seq_write_hydra_pct":'seqWriteHydraPct',
        "seq_write_ssd_pct":'seqWriteSsdPct',
        "weight":'weight',
        "work_load_type":'workLoadType'
    }

    def __init__(self,
                 always_use_ssd=None,
                 id=None,
                 min_requests=None,
                 name=None,
                 priority=None,
                 random_write_hydra_pct=None,
                 random_write_ssd_pct=None,
                 seq_write_hydra_pct=None,
                 seq_write_ssd_pct=None,
                 weight=None,
                 work_load_type=None):
        """Constructor for the QoSPolicy class"""

        # Initialize members of the class
        self.always_use_ssd = always_use_ssd
        self.id = id
        self.min_requests = min_requests
        self.name = name
        self.priority = priority
        self.random_write_hydra_pct = random_write_hydra_pct
        self.random_write_ssd_pct = random_write_ssd_pct
        self.seq_write_hydra_pct = seq_write_hydra_pct
        self.seq_write_ssd_pct = seq_write_ssd_pct
        self.weight = weight
        self.work_load_type = work_load_type


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
        always_use_ssd = dictionary.get('alwaysUseSsd')
        id = dictionary.get('id')
        min_requests = dictionary.get('minRequests')
        name = dictionary.get('name')
        priority = dictionary.get('priority')
        random_write_hydra_pct = dictionary.get('randomWriteHydraPct')
        random_write_ssd_pct = dictionary.get('randomWriteSsdPct')
        seq_write_hydra_pct = dictionary.get('seqWriteHydraPct')
        seq_write_ssd_pct = dictionary.get('seqWriteSsdPct')
        weight = dictionary.get('weight')
        work_load_type = dictionary.get('workLoadType')

        # Return an object of this model
        return cls(always_use_ssd,
                   id,
                   min_requests,
                   name,
                   priority,
                   random_write_hydra_pct,
                   random_write_ssd_pct,
                   seq_write_hydra_pct,
                   seq_write_ssd_pct,
                   weight,
                   work_load_type)


