# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class QoS(object):

    """Implementation of the 'QoS' model.

    Specifies the Quality of Service (QoS) Policy for the View.

    Attributes:
        principal_id (long|int): Specifies the name of the QoS Policy used for
            the View.
        principal_name (string): Specifies the name of the QoS Policy used for
            the View such as 'TestAndDev High', 'Backup Target SSD', 'Backup
            Target High' 'TestAndDev Low' and 'Backup Target Low'. For a
            complete list and descriptions, see the 'Create or Edit Views'
            topic in the documentation. If not specified, the default is
            'Backup Target Low'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "principal_id":'principalId',
        "principal_name":'principalName'
    }

    def __init__(self,
                 principal_id=None,
                 principal_name=None):
        """Constructor for the QoS class"""

        # Initialize members of the class
        self.principal_id = principal_id
        self.principal_name = principal_name


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
        principal_id = dictionary.get('principalId')
        principal_name = dictionary.get('principalName')

        # Return an object of this model
        return cls(principal_id,
                   principal_name)


