# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantProtectionJobUpdateParameters(object):

    """Implementation of the 'TenantProtectionJobUpdateParameters' model.

    Specifies protection job update details about a tenant.

    Attributes:
        protection_job_ids (list of long|int): Specifies the ProtectionJobIds
            vec for respective tenant.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_job_ids":'protectionJobIds',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 protection_job_ids=None,
                 tenant_id=None):
        """Constructor for the TenantProtectionJobUpdateParameters class"""

        # Initialize members of the class
        self.protection_job_ids = protection_job_ids
        self.tenant_id = tenant_id


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
        protection_job_ids = dictionary.get('protectionJobIds')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(protection_job_ids,
                   tenant_id)


