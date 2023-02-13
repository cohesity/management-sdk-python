# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.infected_file_id

class UpdateInfectedFileResponse(object):

    """Implementation of the 'UpdateInfectedFileResponse' model.

    TODO: type model description here.

    Attributes:
        update_failed_infected_files (list of InfectedFileId): Specifies the
            failed update infected files.
        update_succeeded_infected_files (list of InfectedFileId): Specifies
            the successfully updated infected files.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "update_failed_infected_files":'updateFailedInfectedFiles',
        "update_succeeded_infected_files":'updateSucceededInfectedFiles'
    }

    def __init__(self,
                 update_failed_infected_files=None,
                 update_succeeded_infected_files=None):
        """Constructor for the UpdateInfectedFileResponse class"""

        # Initialize members of the class
        self.update_failed_infected_files = update_failed_infected_files
        self.update_succeeded_infected_files = update_succeeded_infected_files


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
        update_failed_infected_files = None
        if dictionary.get('updateFailedInfectedFiles') != None:
            update_failed_infected_files = list()
            for structure in dictionary.get('updateFailedInfectedFiles'):
                update_failed_infected_files.append(cohesity_management_sdk.models.infected_file_id.InfectedFileId.from_dictionary(structure))
        update_succeeded_infected_files = None
        if dictionary.get('updateSucceededInfectedFiles') != None:
            update_succeeded_infected_files = list()
            for structure in dictionary.get('updateSucceededInfectedFiles'):
                update_succeeded_infected_files.append(cohesity_management_sdk.models.infected_file_id.InfectedFileId.from_dictionary(structure))

        # Return an object of this model
        return cls(update_failed_infected_files,
                   update_succeeded_infected_files)


