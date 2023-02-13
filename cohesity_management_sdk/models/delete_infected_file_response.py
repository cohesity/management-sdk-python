# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.infected_file_id

class DeleteInfectedFileResponse(object):

    """Implementation of the 'DeleteInfectedFileResponse' model.

    TODO: type model description here.

    Attributes:
        delete_failed_infected_files (list of InfectedFileId): Specifies the
            failed delete infected files.
        delete_succeeded_infected_files (list of InfectedFileId): Specifies
            the successfully deleted infected files.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delete_failed_infected_files":'deleteFailedInfectedFiles',
        "delete_succeeded_infected_files":'deleteSucceededInfectedFiles'
    }

    def __init__(self,
                 delete_failed_infected_files=None,
                 delete_succeeded_infected_files=None):
        """Constructor for the DeleteInfectedFileResponse class"""

        # Initialize members of the class
        self.delete_failed_infected_files = delete_failed_infected_files
        self.delete_succeeded_infected_files = delete_succeeded_infected_files


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
        delete_failed_infected_files = None
        if dictionary.get('deleteFailedInfectedFiles') != None:
            delete_failed_infected_files = list()
            for structure in dictionary.get('deleteFailedInfectedFiles'):
                delete_failed_infected_files.append(cohesity_management_sdk.models.infected_file_id.InfectedFileId.from_dictionary(structure))
        delete_succeeded_infected_files = None
        if dictionary.get('deleteSucceededInfectedFiles') != None:
            delete_succeeded_infected_files = list()
            for structure in dictionary.get('deleteSucceededInfectedFiles'):
                delete_succeeded_infected_files.append(cohesity_management_sdk.models.infected_file_id.InfectedFileId.from_dictionary(structure))

        # Return an object of this model
        return cls(delete_failed_infected_files,
                   delete_succeeded_infected_files)


