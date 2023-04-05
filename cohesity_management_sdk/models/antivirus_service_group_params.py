# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.antivirus_service_config_params


class AntivirusServiceGroupParams(object):

    """Implementation of the 'AntivirusServiceGroupParams' model.

    TODO: type description here.


    Attributes:

        antivirus_services (list of AntivirusServiceConfigParams): Specifies
            the Antivirus services for this provider.
        description (string): Specifies the description of the Antivirus
            service group.
        name (string, required): Specifies the name of the Antivirus service
            group.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "antivirus_services":'antivirusServices',
        "description":'description',
        "name":'name',
    }
    def __init__(self,
                 antivirus_services=None,
                 description=None,
                 name=None,
            ):

        """Constructor for the AntivirusServiceGroupParams class"""

        # Initialize members of the class
        self.antivirus_services = antivirus_services
        self.description = description
        self.name = name

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
        antivirus_services = None
        if dictionary.get('antivirusServices') != None:
            antivirus_services = list()
            for structure in dictionary.get('antivirusServices'):
                antivirus_services.append(cohesity_management_sdk.models.antivirus_service_config_params.AntivirusServiceConfigParams.from_dictionary(structure))
        description = dictionary.get('description')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            antivirus_services,
            description,
            name
)