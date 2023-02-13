# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sample

class IopsTile(object):

    """Implementation of the 'IopsTile' model.

    IOPs information for dashboard.

    Attributes:
        max_read_iops (long|int): Maximum Read IOs per second in last 24
            hours.
        max_write_iops (long|int): Maximum number of Write IOs per second in
            last 24 hours.
        read_iops_samples (list of Sample): Read IOs per second samples taken
            for the past 24 hours at 10 minutes interval given in descending
            order of time.
        write_iops_samples (list of Sample): Write IOs per second samples
            taken for the past 24 hours at 10 minutes interval given in
            descending order of time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "max_read_iops":'maxReadIops',
        "max_write_iops":'maxWriteIops',
        "read_iops_samples":'readIopsSamples',
        "write_iops_samples":'writeIopsSamples'
    }

    def __init__(self,
                 max_read_iops=None,
                 max_write_iops=None,
                 read_iops_samples=None,
                 write_iops_samples=None):
        """Constructor for the IopsTile class"""

        # Initialize members of the class
        self.max_read_iops = max_read_iops
        self.max_write_iops = max_write_iops
        self.read_iops_samples = read_iops_samples
        self.write_iops_samples = write_iops_samples


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
        max_read_iops = dictionary.get('maxReadIops')
        max_write_iops = dictionary.get('maxWriteIops')
        read_iops_samples = None
        if dictionary.get('readIopsSamples') != None:
            read_iops_samples = list()
            for structure in dictionary.get('readIopsSamples'):
                read_iops_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))
        write_iops_samples = None
        if dictionary.get('writeIopsSamples') != None:
            write_iops_samples = list()
            for structure in dictionary.get('writeIopsSamples'):
                write_iops_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))

        # Return an object of this model
        return cls(max_read_iops,
                   max_write_iops,
                   read_iops_samples,
                   write_iops_samples)


