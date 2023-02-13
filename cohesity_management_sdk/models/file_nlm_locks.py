# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_id
import cohesity_management_sdk.models.nlm_lock

class FileNlmLocks(object):

    """Implementation of the 'FileNlmLocks' model.

    Specifies per-file NLM locks

    Attributes:
        file_id (FileId): TODO: type description here.
        nlm_locks (list of NlmLock): Specifies the list of NLM locks in a
            view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_id":'fileId',
        "nlm_locks":'nlmLocks'
    }

    def __init__(self,
                 file_id=None,
                 nlm_locks=None):
        """Constructor for the FileNlmLocks class"""

        # Initialize members of the class
        self.file_id = file_id
        self.nlm_locks = nlm_locks


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
        file_id = cohesity_management_sdk.models.file_id.FileId.from_dictionary(dictionary.get('fileId')) if dictionary.get('fileId') else None
        nlm_locks = None
        if dictionary.get('nlmLocks') != None:
            nlm_locks = list()
            for structure in dictionary.get('nlmLocks'):
                nlm_locks.append(cohesity_management_sdk.models.nlm_lock.NlmLock.from_dictionary(structure))

        # Return an object of this model
        return cls(file_id,
                   nlm_locks)


