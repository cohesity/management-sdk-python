# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.statement


class BucketPolicy(object):

    """Implementation of the 'BucketPolicy' model.

    TODO: type description here.


    Attributes:

        id (string): The identifier for the bucket policy.
        raw_policy_str (string): Raw JSON string of the stored policy.
        statement_vec (list of Statement): This field defines the statement to
            execute for each request.
        version (string): This field specifies the language syntax rules that
            are to be used to process the policy.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "raw_policy_str":'rawPolicyStr',
        "statement_vec":'statementVec',
        "version":'version',
    }
    def __init__(self,
                 id=None,
                 raw_policy_str=None,
                 statement_vec=None,
                 version=None,
            ):

        """Constructor for the BucketPolicy class"""

        # Initialize members of the class
        self.id = id
        self.raw_policy_str = raw_policy_str
        self.statement_vec = statement_vec
        self.version = version

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
        id = dictionary.get('id')
        raw_policy_str = dictionary.get('rawPolicyStr')
        statement_vec = None
        if dictionary.get('statementVec') != None:
            statement_vec = list()
            for structure in dictionary.get('statementVec'):
                statement_vec.append(cohesity_management_sdk.models.statement.Statement.from_dictionary(structure))
        version = dictionary.get('version')

        # Return an object of this model
        return cls(
            id,
            raw_policy_str,
            statement_vec,
            version
)