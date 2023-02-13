# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sequence_number

class Sequencer(object):

    """Implementation of the 'Sequencer' model.

    Sequencer used to identify pieces of data sent to Atom. It is expected that
    different enviroment protos will be added to this  to define their own
    sequencers like one is added for VMware below.

    Attributes:
        mongodb_sequencer (SequenceNumber): TODO: Type description here.
        vmware_sequencer (SequenceNumber): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mongodb_sequencer": 'mongodbSequencer',
        "vmware_sequencer": 'vmwareSequencer'
    }

    def __init__(self,
                 mongodb_sequencer=None,
                 vmware_sequencer=None):
        """Constructor for the Sequencer class"""

        # Initialize members of the class
        self.mongodb_sequencer = mongodb_sequencer
        self.vmware_sequencer = vmware_sequencer


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
        mongodb_sequencer = cohesity_management_sdk.models.sequence_number.SequenceNumber.from_dictionary(dictionary.get('mongodbSequencer')) if dictionary.get('mongodbSequencer') else None
        vmware_sequencer = cohesity_management_sdk.models.sequence_number.SequenceNumber.from_dictionary(dictionary.get('vmwareSequencer')) if dictionary.get('vmwareSequencer') else None

        # Return an object of this model
        return cls(mongodb_sequencer,
                   vmware_sequencer)


