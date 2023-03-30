# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ebs_volume_exclusion_params


class AWSSnapshotManagerParams(object):

    """Implementation of the 'AWSSnapshotManagerParams' model.

    TODO: type description here.


    Attributes:

        ami_creation_frequency (int): The frequency of AMI creation. This
            should be set if the option to create AMI is set. A value of n
            creates an AMI from the snapshots after every n runs. eg. n = 2
            implies every alternate backup run starting from the first will
            create an AMI.
        create_ami_for_run (bool): Whether we need to create an AMI for this
            run.
        should_create_ami (bool): Whether we need to create an AMI after taking
            snapshots of the instance.
        volume_exclusion_params (EBSVolumeExclusionParams): Specifies the
            different criteria to exclude volumes from backup.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "ami_creation_frequency":'amiCreationFrequency',
        "create_ami_for_run":'createAmiForRun',
        "should_create_ami":'shouldCreateAmi',
        "volume_exclusion_params":'volumeExclusionParams',
    }
    def __init__(self,
                 ami_creation_frequency=None,
                 create_ami_for_run=None,
                 should_create_ami=None,
                 volume_exclusion_params=None,
            ):

        """Constructor for the AWSSnapshotManagerParams class"""

        # Initialize members of the class
        self.ami_creation_frequency = ami_creation_frequency
        self.create_ami_for_run = create_ami_for_run
        self.should_create_ami = should_create_ami
        self.volume_exclusion_params = volume_exclusion_params

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
        ami_creation_frequency = dictionary.get('amiCreationFrequency')
        create_ami_for_run = dictionary.get('createAmiForRun')
        should_create_ami = dictionary.get('shouldCreateAmi')
        volume_exclusion_params = cohesity_management_sdk.models.ebs_volume_exclusion_params.EBSVolumeExclusionParams.from_dictionary(dictionary.get('volumeExclusionParams')) if dictionary.get('volumeExclusionParams') else None

        # Return an object of this model
        return cls(
            ami_creation_frequency,
            create_ami_for_run,
            should_create_ami,
            volume_exclusion_params
)