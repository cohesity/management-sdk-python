# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.condition
import cohesity_management_sdk.models.principal


class Statement(object):

    """Implementation of the 'Statement' model.

    TODO: type description here.


    Attributes:

        action_vec (list of string): This field includes keyword which map to
            permission for each S3 operation. We support wildcard('*' and '?')
            for this field. Some of the valid formats are : "*", "s3:*",
            "s3:*Object"
        condition_vec (list of Condition): The field specified the conditions
            for when a policy is in effect.
        is_allow (bool): This field specifies whether the statement results in
            an allow or an explicit deny.
        negate_action_vec (bool): If set, actions except the ones specified in
            action_vec would be considered valid for evaluating the statement.
            This is set if JSON has "NotAction" element.
        negate_principal (bool): If set, users except the specified principal
            would be considered valid for evaluating the statement. This is set
            if JSON has "NotPrincipal" element.
        negate_resource_vec (bool): If set, resources except the ones specified
            in resource_vec would be considered valid for evaluating the
            statement. This is set if JSON has "NotResource" element.
        principal (Principal): This field indicates the user entities allowed
            to access the resource(s).
        resource_vec (list of string): This field indicates the resource for
            which the statement is applied. The format we will be using is
            "urn:csf:s3:::bucket_name/key_name". 'csf' stands for Cohesity
            SmartFiles. We support wildcard('*' and '?') in the key name. Some
            of the valid formats are : "urn:csf:s3:::bucket_name",
            "urn:csf:s3:::bucket_name/*", "urn:csf:s3:::bucket_name/*/ab?"
        sid (string): Statement identifier.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "action_vec":'actionVec',
        "condition_vec":'conditionVec',
        "is_allow":'isAllow',
        "negate_action_vec":'negateActionVec',
        "negate_principal":'negatePrincipal',
        "negate_resource_vec":'negateResourceVec',
        "principal":'principal',
        "resource_vec":'resourceVec',
        "sid":'sid',
    }
    def __init__(self,
                 action_vec=None,
                 condition_vec=None,
                 is_allow=None,
                 negate_action_vec=None,
                 negate_principal=None,
                 negate_resource_vec=None,
                 principal=None,
                 resource_vec=None,
                 sid=None,
            ):

        """Constructor for the Statement class"""

        # Initialize members of the class
        self.action_vec = action_vec
        self.condition_vec = condition_vec
        self.is_allow = is_allow
        self.negate_action_vec = negate_action_vec
        self.negate_principal = negate_principal
        self.negate_resource_vec = negate_resource_vec
        self.principal = principal
        self.resource_vec = resource_vec
        self.sid = sid

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
        action_vec = dictionary.get("actionVec")
        condition_vec = None
        if dictionary.get('conditionVec') != None:
            condition_vec = list()
            for structure in dictionary.get('conditionVec'):
                condition_vec.append(cohesity_management_sdk.models.condition.Condition.from_dictionary(structure))
        is_allow = dictionary.get('isAllow')
        negate_action_vec = dictionary.get('negateActionVec')
        negate_principal = dictionary.get('negatePrincipal')
        negate_resource_vec = dictionary.get('negateResourceVec')
        principal = cohesity_management_sdk.models.principal.Principal.from_dictionary(dictionary.get('principal')) if dictionary.get('principal') else None
        resource_vec = dictionary.get("resourceVec")
        sid = dictionary.get('sid')

        # Return an object of this model
        return cls(
            action_vec,
            condition_vec,
            is_allow,
            negate_action_vec,
            negate_principal,
            negate_resource_vec,
            principal,
            resource_vec,
            sid
)