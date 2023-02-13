# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sample

class ThroughputTile(object):

    """Implementation of the 'ThroughputTile' model.

    Throughput information for dashboard.

    Attributes:
        max_read_throughput (long|int): Maxium Read throughput in last 24
            hours.
        max_write_throughput (long|int): Maximum Write throughput in last 24
            hours.
        read_throughput_samples (list of Sample): Read throughput samples
            taken for the past 24 hours at 10 minutes interval given in
            descending order of time.
        write_throughput_samples (list of Sample): Write throughput samples
            taken for the past 24 hours at 10 minutes interval given in
            descending order of time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "max_read_throughput":'maxReadThroughput',
        "max_write_throughput":'maxWriteThroughput',
        "read_throughput_samples":'readThroughputSamples',
        "write_throughput_samples":'writeThroughputSamples'
    }

    def __init__(self,
                 max_read_throughput=None,
                 max_write_throughput=None,
                 read_throughput_samples=None,
                 write_throughput_samples=None):
        """Constructor for the ThroughputTile class"""

        # Initialize members of the class
        self.max_read_throughput = max_read_throughput
        self.max_write_throughput = max_write_throughput
        self.read_throughput_samples = read_throughput_samples
        self.write_throughput_samples = write_throughput_samples


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
        max_read_throughput = dictionary.get('maxReadThroughput')
        max_write_throughput = dictionary.get('maxWriteThroughput')
        read_throughput_samples = None
        if dictionary.get('readThroughputSamples') != None:
            read_throughput_samples = list()
            for structure in dictionary.get('readThroughputSamples'):
                read_throughput_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))
        write_throughput_samples = None
        if dictionary.get('writeThroughputSamples') != None:
            write_throughput_samples = list()
            for structure in dictionary.get('writeThroughputSamples'):
                write_throughput_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))

        # Return an object of this model
        return cls(max_read_throughput,
                   max_write_throughput,
                   read_throughput_samples,
                   write_throughput_samples)


