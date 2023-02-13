# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.antivirus_service_config_params

class UpdateAntivirusServiceGroupParams(object):

    """Implementation of the 'UpdateAntivirusServiceGroupParams' model.

    TODO: type model description here.

    Attributes:
        antivirus_services (list of AntivirusServiceConfigParams): Specifies
            the Antivirus services for this provider.
        description (string): Specifies the description of the Antivirus
            service group.
        id (long|int): Specifies the Id of the Antivirus service group.
        is_enabled (bool): Specifies whether the antivirus service group is
            enabled or not.
        name (string): Specifies the name of the Antivirus service group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "antivirus_services":'antivirusServices',
        "description":'description',
        "is_enabled":'isEnabled'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 antivirus_services=None,
                 description=None,
                 is_enabled=None):
        """Constructor for the UpdateAntivirusServiceGroupParams class"""

        # Initialize members of the class
        self.antivirus_services = antivirus_services
        self.description = description
        self.id = id
        self.is_enabled = is_enabled
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
        id = dictionary.get('id')
        name = dictionary.get('name')
        antivirus_services = None
        if dictionary.get('antivirusServices') != None:
            antivirus_services = list()
            for structure in dictionary.get('antivirusServices'):
                antivirus_services.append(cohesity_management_sdk.models.antivirus_service_config_params.AntivirusServiceConfigParams.from_dictionary(structure))
        description = dictionary.get('description')
        is_enabled = dictionary.get('isEnabled')

        # Return an object of this model
        return cls(id,
                   name,
                   antivirus_services,
                   description,
                   is_enabled)


