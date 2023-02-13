# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CentrifyZone(object):

    """Implementation of the 'CentrifyZone' model.

    Specifies the properties associated to a Centrify zone of an Active
    Directory domain.

    Attributes:
        centrify_schema (CentrifySchemaEnum): Specifies the schema of this
            Centrify zone. The below list of schemas and their values are
            taken from the document Centrify Server Suite 2016 Windows API
            Programmer's Guide
            https://docs.centrify.com/en/css/suite2016/centrify-win-progguide.p
            df 'kCentrifyDynamicSchema_1_0' specifies dynamic schema, version
            1.0. 'kCentrifyDynamicSchema_2_0' specifies dynamic schema,
            version 2.0. 'kCentrifyDynamicSchema_3_0' specifies dynamic
            schema, version 3.0. 'kCentrifyDynamicSchema_5_0' specifies
            dynamic schema, version 5.0. 'kCentrifySfu_3_0' specifies sfu
            schema, version 3.0. 'kCentrifySfu_3_0_V5' specifies sfu schema,
            3.0.5. 'kCentrifySfu_4_0' specifies sfu schema, version 4.0.
            'kCentrifyCdcRfc2307' specifies cdcrfc2307 schema.
            'kCentrifyCdcRfc2307_2' specifies cdcrfc2307, version 2.
            'kCentrifyCdcRfc2307_3' specifies cdcrfc2307, version 3.
        description (string): Specifies a description of the Centrify zone.
        distinguished_name (string): Specifies the distinguished name of the
            Centrify zone.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "centrify_schema":'centrifySchema',
        "description":'description',
        "distinguished_name":'distinguishedName'
    }

    def __init__(self,
                 centrify_schema=None,
                 description=None,
                 distinguished_name=None):
        """Constructor for the CentrifyZone class"""

        # Initialize members of the class
        self.centrify_schema = centrify_schema
        self.description = description
        self.distinguished_name = distinguished_name


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
        centrify_schema = dictionary.get('centrifySchema')
        description = dictionary.get('description')
        distinguished_name = dictionary.get('distinguishedName')

        # Return an object of this model
        return cls(centrify_schema,
                   description,
                   distinguished_name)


