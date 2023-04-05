# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SfdcRestoreObjectParams(object):

    """Implementation of the 'SfdcRestoreObjectParams' model.

    TODO: type description here.


    Attributes:

        filter_query (string): This field contains the user provided query to
            select only subset of records in an object for recovery. This field
            is set only if restore_type is 'kRestoreFilter;.
        include_deleted_records (bool): This field specifies whether to include
            the records in user selected object, that were marked as deleted in
            the user selected snapshot. This is applicable for restore types
            'kRestoreObject' and 'kRestoreOrg'.
        mutation_type (int): The type of records to be returned. This is only
            applicable for restore type 'kRestoreFilter'.
        new_object_name (string): The new name of the object, if it is going to
            be renamed.
        record_id_vec (list of string): Restore selected records from user
            selected object. This field is set only if restore_type is
            'kRestoreRecords'.
        sfdc_restore_type (int): Please note that this restore_type is
            applicable only for the restore of Sfdc adapter. It is different
            from the Magneto infra field 'restore_type' that is applicable for
            all the Recovery tasks.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "filter_query":'filterQuery',
        "include_deleted_records":'includeDeletedRecords',
        "mutation_type":'mutationType',
        "new_object_name":'newObjectName',
        "record_id_vec":'recordIdVec',
        "sfdc_restore_type":'sfdcRestoreType',
    }
    def __init__(self,
                 filter_query=None,
                 include_deleted_records=None,
                 mutation_type=None,
                 new_object_name=None,
                 record_id_vec=None,
                 sfdc_restore_type=None,
            ):

        """Constructor for the SfdcRestoreObjectParams class"""

        # Initialize members of the class
        self.filter_query = filter_query
        self.include_deleted_records = include_deleted_records
        self.mutation_type = mutation_type
        self.new_object_name = new_object_name
        self.record_id_vec = record_id_vec
        self.sfdc_restore_type = sfdc_restore_type

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
        mutation_type = dictionary.get('mutationType')
        new_object_name = dictionary.get('newObjectName')
        record_id_vec = dictionary.get("recordIdVec")
        sfdc_restore_type = dictionary.get('sfdcRestoreType')

        # Return an object of this model
        return cls(
            filter_query,
            include_deleted_records,
            mutation_type,
            new_object_name,
            record_id_vec,
            sfdc_restore_type
)