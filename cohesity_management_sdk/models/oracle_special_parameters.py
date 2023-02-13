# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_app_params

class OracleSpecialParameters(object):

    """Implementation of the 'OracleSpecialParameters' model.

    Specifies special settings applicable for 'kOracle' environment.

    Attributes:
        app_params_list (list of OracleAppParams): Array of application
            parameters i.e. database parameters for standalone/RAC and DG
            parameters for data guard.  Specifies the list of parameters
            required at app entity level.
        application_entity_ids (list of long|int): Array of Ids of Application
            Entities like Oracle instances, and databases that should be
            protected in a Protection Source.  Specifies the subset of
            application entities like Oracle instances, and databases to
            protect in a Protection Source of type kOracle'. If not specified,
            all application entities on the Protection Source.
        persist_mountpoints (bool): Specifies if the mountpoints for Oracle
            view for the current host are to be persisted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_params_list":'appParamsList',
        "application_entity_ids":'applicationEntityIds',
        "persist_mountpoints":'persistMountpoints'
    }

    def __init__(self,
                 app_params_list=None,
                 application_entity_ids=None,
                 persist_mountpoints=None):
        """Constructor for the OracleSpecialParameters class"""

        # Initialize members of the class
        self.app_params_list = app_params_list
        self.application_entity_ids = application_entity_ids
        self.persist_mountpoints = persist_mountpoints


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
        app_params_list = None
        if dictionary.get('appParamsList') != None:
            app_params_list = list()
            for structure in dictionary.get('appParamsList'):
                app_params_list.append(cohesity_management_sdk.models.oracle_app_params.OracleAppParams.from_dictionary(structure))
        application_entity_ids = dictionary.get('applicationEntityIds')
        persist_mountpoints = dictionary.get('persistMountpoints')

        # Return an object of this model
        return cls(app_params_list,
                   application_entity_ids,
                   persist_mountpoints)


