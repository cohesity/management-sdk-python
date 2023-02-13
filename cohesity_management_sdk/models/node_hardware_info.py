# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NodeHardwareInfo(object):

    """Implementation of the 'NodeHardwareInfo' model.

    NodeHardwareInfo provides the information regarding the hardware.

    Attributes:
        cpu (string): Cpu provides the information regarding the CPU.
        memory_size_bytes (long|int): MemorySizeBytes provides the memory size
            in bytes.
        network (string): Network provides the information regarding the
            network cards.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cpu":'cpu',
        "memory_size_bytes":'memorySizeBytes',
        "network":'network'
    }

    def __init__(self,
                 cpu=None,
                 memory_size_bytes=None,
                 network=None):
        """Constructor for the NodeHardwareInfo class"""

        # Initialize members of the class
        self.cpu = cpu
        self.memory_size_bytes = memory_size_bytes
        self.network = network


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
        cpu = dictionary.get('cpu')
        memory_size_bytes = dictionary.get('memorySizeBytes')
        network = dictionary.get('network')

        # Return an object of this model
        return cls(cpu,
                   memory_size_bytes,
                   network)


