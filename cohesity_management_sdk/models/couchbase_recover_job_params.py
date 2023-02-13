# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CouchbaseRecoverJobParams(object):

    """Implementation of the 'CouchbaseRecoverJobParams' model.

    Contains any additional couchbase environment specific params for the
    recover job.

    Attributes:
        append_documents (bool): Whether to append documents into the bucket
            at the destination
        ddl_only_recovery (bool): Whether to recover only the bucket
            configuration
        documents_filter_type (int): Specify the document type recovery option.
        filter_expression (string): A filter expression to match Documents
            content to be restored.
        id_regex (string): A regular expression to match Documents ID's to be
            restored.
        overwrite_users (bool): Whether to replace existing users with users
            from the bucket
        suffix (string): A suffix that is to be applied to all recovered
            entities

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "append_documents": 'appendDocuments',
        "ddl_only_recovery": 'ddlOnlyRecovery',
        "documents_filter_type": 'documentsFilterType',
        "filter_expression":'filterExpression',
        "id_regex":'idRegex',
        "overwrite_users":'overwriteUsers',
        "suffix":'suffix'
    }

    def __init__(self,
                 append_documents=None,
                 ddl_only_recovery=None,
                 documents_filter_type=None,
                 filter_expression=None,
                 id_regex=None,
                 overwrite_users=None,
                 suffix=None
                 ):
        """Constructor for the CouchbaseRecoverJobParams class"""

        # Initialize members of the class
        self.append_documents = append_documents
        self.ddl_only_recovery = ddl_only_recovery
        self.documents_filter_type = documents_filter_type
        self.filter_expression = filter_expression
        self.id_regex = id_regex
        self.overwrite_users = overwrite_users
        self.suffix = suffix

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
        append_documents = dictionary.get('appendDocuments')
        ddl_only_recovery = dictionary.get('ddlOnlyRecovery')
        documents_filter_type = dictionary.get('documentsFilterType')
        filter_expression = dictionary.get('filterExpression')
        id_regex = dictionary.get('idRegex')
        overwrite_users = dictionary.get('overwriteUsers')
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(append_documents,
                   ddl_only_recovery,
                   documents_filter_type,
                   filter_expression,
                   id_regex,
                   overwrite_users,
                   suffix)


