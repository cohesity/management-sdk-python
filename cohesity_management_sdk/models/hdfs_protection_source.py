# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HdfsProtectionSource(object):

    """Implementation of the 'HdfsProtectionSource' model.

    Specifies an Object representing Hdfs.

    Attributes:
        name (string): Specifies the instance name of the Hdfs entity.
        mtype (TypeHdfsProtectionSourceEnum): Specifies the type of the
            managed Object in Hdfs Protection Source.
            Specifies the type of an Hdfs source entity.
            'kCluster' indicates a Hdfs cluster distributed over several physical
            nodes.
        uuid (string):  Specifies the UUID for the Hdfs entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the HdfsProtectionSource class"""

        # Initialize members of the class
        self.name = name
        self.mtype = mtype
        self.uuid = uuid


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
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(name,
                   mtype,
                   uuid)


