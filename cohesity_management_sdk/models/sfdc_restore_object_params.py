# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SfdcRestoreObjectParams(object):

    """Implementation of the 'SfdcRestoreObjectParams' model.

    TODO: type description here.


    Attributes:

        filter_query (string): Restore subset of records. Query to filter the
            records. populated if restore_type is kRestoreFilter.
        include_deleted_records (bool): Include deleted records.
        new_object_name (string): The new name of the object, if it is going to
            be renamed.
        record_id_vec (list of string): Restore selected records populated if
            restore_type is kRestoreRecords
        restore_type (int): TODO: Type description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "filter_query":'filterQuery',
        "include_deleted_records":'includeDeletedRecords',
        "new_object_name":'newObjectName',
        "record_id_vec":'recordIdVec',
        "restore_type":'restoreType',
    }
    def __init__(self,
                 filter_query=None,
                 include_deleted_records=None,
                 new_object_name=None,
                 record_id_vec=None,
                 restore_type=None,
            ):

        """Constructor for the SfdcRestoreObjectParams class"""

        # Initialize members of the class
        self.filter_query = filter_query
        self.include_deleted_records = include_deleted_records
        self.new_object_name = new_object_name
        self.record_id_vec = record_id_vec
        self.restore_type = restore_type

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
        filter_query = dictionary.get('filterQuery')
        include_deleted_records = dictionary.get('includeDeletedRecords')
        new_object_name = dictionary.get('newObjectName')
        record_id_vec = dictionary.get("recordIdVec")
        restore_type = dictionary.get('restoreType')

        # Return an object of this model
        return cls(
            filter_query,
            include_deleted_records,
            new_object_name,
            record_id_vec,
            restore_type
)