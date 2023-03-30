# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CloudDomainList(object):

    """Implementation of the 'CloudDomainList' model.

    CloudDomainList specfies the cloud domain information associated with the
    vault.


    Attributes:

        domain_id (long|int): Specifies the Id of the cloud domain.
        view_box_id (long|int): Specifies the Id of the ViewBox related to the
            cloud domain.
        view_box_name (string): Specifies the Name of the ViewBox related to
            the cloud domain.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "domain_id":'domainId',
        "view_box_id":'viewBoxId',
        "view_box_name":'viewBoxName',
    }
    def __init__(self,
                 domain_id=None,
                 view_box_id=None,
                 view_box_name=None,
            ):

        """Constructor for the CloudDomainList class"""

        # Initialize members of the class
        self.domain_id = domain_id
        self.view_box_id = view_box_id
        self.view_box_name = view_box_name

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
        domain_id = dictionary.get('domainId')
        view_box_id = dictionary.get('viewBoxId')
        view_box_name = dictionary.get('viewBoxName')

        # Return an object of this model
        return cls(
            domain_id,
            view_box_id,
            view_box_name
)