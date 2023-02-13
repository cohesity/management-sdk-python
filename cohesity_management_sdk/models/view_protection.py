# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_job_info

class ViewProtection(object):

    """Implementation of the 'ViewProtection' model.

    Specifies information about the Protection Jobs that are protecting the
    View.

    Attributes:
        inactive (bool): Specifies if this View is an inactive View that was
            created on this Remote Cluster to store the Snapshots created by
            replication. This inactive View cannot be NFS or SMB mounted.
        magneto_entity_id (long|int): Specifies the id of the Protection
            Source that is using this View.
        protection_jobs (list of ProtectionJobInfo): Array of Protection Jobs.
            Specifies the Protection Jobs that are protecting the View.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "inactive":'inactive',
        "magneto_entity_id":'magnetoEntityId',
        "protection_jobs":'protectionJobs'
    }

    def __init__(self,
                 inactive=None,
                 magneto_entity_id=None,
                 protection_jobs=None):
        """Constructor for the ViewProtection class"""

        # Initialize members of the class
        self.inactive = inactive
        self.magneto_entity_id = magneto_entity_id
        self.protection_jobs = protection_jobs


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
        inactive = dictionary.get('inactive')
        magneto_entity_id = dictionary.get('magnetoEntityId')
        protection_jobs = None
        if dictionary.get('protectionJobs') != None:
            protection_jobs = list()
            for structure in dictionary.get('protectionJobs'):
                protection_jobs.append(cohesity_management_sdk.models.protection_job_info.ProtectionJobInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(inactive,
                   magneto_entity_id,
                   protection_jobs)


