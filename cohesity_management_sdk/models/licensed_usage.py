# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class LicensedUsage(object):

    """Implementation of the 'LicensedUsage' model.

    Structure to hold feature usage on cluster side.

    Attributes:
        capacity_gb (int|long): Feature usage by the cluster.
        expiry_time (int|long): Expiry time(epoch) of each feature.
            There could be multiple expiry time for the given SKU.
        feature_name (string): Name of feature.
        license_type (string): Type of License
        num_vm (int|long): Number of VM spinned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capacity_gb": 'capacityGB',
        "expiry_time": 'expiryTime',
        "feature_name": 'featureName',
        "license_type": 'licenseType',
        "num_vm":'numVm'
    }

    def __init__(self,
                 capacity_gb=None,
                 expiry_time=None,
                 feature_name=None,
                 license_type=None,
                 num_vm=None):
        """Constructor for the LicensedUsage class"""

        # Initialize members of the class
        self.capacity_gb = capacity_gb
        self.expiry_time = expiry_time
        self.feature_name = feature_name
        self.license_type = license_type
        self.num_vm = num_vm

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
        capacity_gb = dictionary.get('capacityGB')
        expiry_time = dictionary.get('expiryTime')
        feature_name = dictionary.get('featureName')
        license_type = dictionary.get('licenseType')
        num_vm = dictionary.get('numVm')

        # Return an object of this model
        return cls(capacity_gb,
                   expiry_time,
                   feature_name,
                   license_type,
                   num_vm)


