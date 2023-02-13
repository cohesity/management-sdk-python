# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LicensedUsage(object):

    """Implementation of the 'LicensedUsage' model.

    Structure to hold feature usage on cluster side.

    Attributes:
        capacity_gib (int|long): Feature usage by the cluster.
        expiry_time (int|long): Expiry time(epoch) of each feature.
            There could be multiple expiry time for the given SKU.
        feature_name (string): Name of feature.
        license_type (string): Type of License
        num_vm (int|long): Number of VM spinned.
        product_description (string): Detail description of entitlement
        product_info (string): Short description of entitlement

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capacity_gib": 'capacityGiB',
        "expiry_time": 'expiryTime',
        "feature_name": 'featureName',
        "license_type": 'licenseType',
        "num_vm":'numVm',
        "product_description":'productDescription',
        "product_info":'productInfo'
    }

    def __init__(self,
                 capacity_gib=None,
                 expiry_time=None,
                 feature_name=None,
                 license_type=None,
                 num_vm=None,
                 product_description=None,
                 product_info=None):
        """Constructor for the LicensedUsage class"""

        # Initialize members of the class
        self.capacity_gib = capacity_gib
        self.expiry_time = expiry_time
        self.feature_name = feature_name
        self.license_type = license_type
        self.num_vm = num_vm
        self.product_description = product_description
        self.product_info = product_info

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
        capacity_gib = dictionary.get('capacityGiB')
        expiry_time = dictionary.get('expiryTime')
        feature_name = dictionary.get('featureName')
        license_type = dictionary.get('licenseType')
        num_vm = dictionary.get('numVm')
        product_description = dictionary.get('productDescription')
        product_info = dictionary.get('productInfo')

        # Return an object of this model
        return cls(capacity_gib,
                   expiry_time,
                   feature_name,
                   license_type,
                   num_vm,
                   product_description,
                   product_info)


