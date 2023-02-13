# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SiteProperty(object):

    """Implementation of the 'SiteProperty' model.

    Generic site Property structure to store site properties. Some of these
    site properties are not captured by Get-PnpProvisioningTemplate cmdlet. So
    they may need to be set outside of Appy-PnPProvisoningTemplate cmdlet.

    Attributes:
        datatype (string): PnP data type of the property ('string',
            'mvstring', 'bool', 'guid','<enumname>','int', 'int64', etc.)
        name (string): Name of the property returned by Get-PnPSite,
            Get-PnPTenantSite, Get-PnPWeb, or other cmdlets.
        value (string): Property value represented as string.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "datatype":'datatype',
        "name":'name',
        "value":'value'
    }

    def __init__(self,
                 datatype=None,
                 name=None,
                 value=None):
        """Constructor for the SiteProperty class"""

        # Initialize members of the class
        self.datatype = datatype
        self.name = name
        self.value = value


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
        datatype = dictionary.get('datatype')
        name = dictionary.get('name')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(datatype,
                   name,
                   value)


