# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AwsSnapshotManagerParameters(object):

    """Implementation of the 'AwsSnapshotManagerParameters' model.

    Protection Job parameters applicable to 'kAWSSnapshotManager' Environment
    type.
    Specifies additional job parameters applicable for 'kAWSSnapshotManager'
    Environment type Protection Sources in a Protection Job.

    Attributes:
        ami_creation_frequency (int): Specifies the frequency of AMI creation.
            This should be set if the option to create AMI is set. A value of
            n creates an AMI from the snapshots after every n runs. eg. n = 2
            implies every alternate backup run starting from the first will
            create an AMI.
        create_ami (bool): If true, creates an AMI after taking snapshots of
            the instance. It should be set only while backing up EC2
            instances. CreateAmi creates AMI for the protection job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ami_creation_frequency":'amiCreationFrequency',
        "create_ami":'createAmi'
    }

    def __init__(self,
                 ami_creation_frequency=None,
                 create_ami=None):
        """Constructor for the AwsSnapshotManagerParameters class"""

        # Initialize members of the class
        self.ami_creation_frequency = ami_creation_frequency
        self.create_ami = create_ami


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
        create_ami = dictionary.get('createAmi')

        # Return an object of this model
        return cls(ami_creation_frequency,
                   create_ami)


