# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GCPDiskExclusionObjectParams(object):

    """Implementation of the 'GCPDiskExclusionObjectParams' model.

    Message defining the different criteria to exclude GCP disks from
    object-level backup. All the disk name present here will be excluded.


    Attributes:

        disk_name_vec (list of string): List of disk name to exclude. Eg -
            [instance1-disk, instance2-disk]
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "disk_name_vec":'diskNameVec',
    }
    def __init__(self,
                 disk_name_vec=None,
            ):

        """Constructor for the GCPDiskExclusionObjectParams class"""

        # Initialize members of the class
        self.disk_name_vec = disk_name_vec

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
        disk_name_vec = dictionary.get("diskNameVec")

        # Return an object of this model
        return cls(
            disk_name_vec
)