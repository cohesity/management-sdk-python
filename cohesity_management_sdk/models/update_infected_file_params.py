# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.infected_file_param

class UpdateInfectedFileParams(object):

    """Implementation of the 'UpdateInfectedFileParams' model.

    TODO: type model description here.

    Attributes:
        infected_file_ids (list of InfectedFileParam): Specifies the list of
            infected file identifiers.
        remediation_state (RemediationStateUpdateInfectedFileParamsEnum):
            Specifies the remediation state of the file. Not setting any value
            to remediation state will reset the infected file. Remediation
            State. 'kQuarantine' indicates 'Quarantine' state of the file.
            This state blocks the client access. The administrator will have
            to manually delete, rescan or unquarantine the file.
            'kUnquarantine' indicates 'Unquarantine' state of the file. The
            administrator has manually moved files from quarantined to the
            unquarantined state to allow client access. Unquarantined files
            are not scanned for virus until manually reset.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "infected_file_ids":'infectedFileIds',
        "remediation_state":'remediationState'
    }

    def __init__(self,
                 infected_file_ids=None,
                 remediation_state=None):
        """Constructor for the UpdateInfectedFileParams class"""

        # Initialize members of the class
        self.infected_file_ids = infected_file_ids
        self.remediation_state = remediation_state


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
        infected_file_ids = None
        if dictionary.get('infectedFileIds') != None:
            infected_file_ids = list()
            for structure in dictionary.get('infectedFileIds'):
                infected_file_ids.append(cohesity_management_sdk.models.infected_file_param.InfectedFileParam.from_dictionary(structure))
        remediation_state = dictionary.get('remediationState')

        # Return an object of this model
        return cls(infected_file_ids,
                   remediation_state)


