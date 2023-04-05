# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.gcp_job_disk_exclusion_rule_label


class GCPJobDiskExclusionRule(object):

    """Implementation of the 'GCPJobDiskExclusionRule' model.

    Message defining the different criteria to exclude GCP disks from job-level
    backup. The values set will be used for AND operation. For
    E.g:(Balanced-Persistant && instance1-disk)


    Attributes:

        disk_name (string): Disk name to exclude. Eg - instance1-disk
        disk_type (string): Disk types to exclude. Eg - Balanced-Persistant
            etc.
        label_vec (list of GCPJobDiskExclusionRule_Label): Specifies the label
            vectors used to exclude GCP disks attached to GCP instances at
            global and object level. E.g., {label_vec: [(K1, V1),  (K2, V2)],
            => This will exclude a particular disk if it has all the tags in
            label_vec((K1, V1),  (K2, V2))
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "disk_name":'diskName',
        "disk_type":'diskType',
        "label_vec":'labelVec',
    }
    def __init__(self,
                 disk_name=None,
                 disk_type=None,
                 label_vec=None,
            ):

        """Constructor for the GCPJobDiskExclusionRule class"""

        # Initialize members of the class
        self.disk_name = disk_name
        self.disk_type = disk_type
        self.label_vec = label_vec

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
        disk_name = dictionary.get('diskName')
        disk_type = dictionary.get('diskType')
        label_vec = None
        if dictionary.get('labelVec') != None:
            label_vec = list()
            for structure in dictionary.get('labelVec'):
                label_vec.append(cohesity_management_sdk.models.gcp_job_disk_exclusion_rule_label.GCPJobDiskExclusionRule_Label.from_dictionary(structure))

        # Return an object of this model
        return cls(
            disk_name,
            disk_type,
            label_vec
)