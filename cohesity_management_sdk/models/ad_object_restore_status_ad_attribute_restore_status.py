# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class ADObjectRestoreStatusADAttributeRestoreStatus(object):

    """Implementation of the 'ADObjectRestoreStatus_ADAttributeRestoreStatus' model.

    TODO: type model description here.

    Attributes:
        attrstatus_vec (list of ErrorProto): Error status. If the
            'attrstatus_vec' is empty or contains kNoError, treat the
            attribute restore as success. For multi-valued properties such as
            'memberOf', this vector may contain failure to add or remove
            specific value within the multi-value set.
        ldap_name (string): LDAP name of the attribute.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attrstatus_vec":'attrstatusVec',
        "ldap_name":'ldapName'
    }

    def __init__(self,
                 attrstatus_vec=None,
                 ldap_name=None):
        """Constructor for the ADObjectRestoreStatusADAttributeRestoreStatus class"""

        # Initialize members of the class
        self.attrstatus_vec = attrstatus_vec
        self.ldap_name = ldap_name


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
        attrstatus_vec = None
        if dictionary.get('attrstatusVec') != None:
            attrstatus_vec = list()
            for structure in dictionary.get('attrstatusVec'):
                attrstatus_vec.append(cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(structure))
        ldap_name = dictionary.get('ldapName')

        # Return an object of this model
        return cls(attrstatus_vec,
                   ldap_name)


