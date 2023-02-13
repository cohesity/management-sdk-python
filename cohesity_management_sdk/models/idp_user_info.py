# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IdpUserInfo(object):

    """Implementation of the 'IdpUserInfo' model.

    Specifies an IdP User's information logged in using an IdP.
    This information is not stored on the Cluster.

    Attributes:
        groups (list of string): Specifies the Idp groups that the user is
            part of. As the user may not be registered on the cluster, we may
            have to capture the idp group membership. This way, if a group is
            created on the cluster later, users will instantly have access to
            tenantIds from that group as well.
        idp_id (long|int): Specifies the unique Id assigned by the Cluster for
            the IdP.
        issuer_id (string): Specifies the unique identifier assigned by the
            vendor for this Cluster.
        user_id (string): Specifies the unique identifier assigned by the
            vendor for the user.
        vendor (string): Specifies the vendor providing the IdP service.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "groups":'groups',
        "idp_id":'idpId',
        "issuer_id":'issuerId',
        "user_id":'userId',
        "vendor":'vendor'
    }

    def __init__(self,
                 groups=None,
                 idp_id=None,
                 issuer_id=None,
                 user_id=None,
                 vendor=None):
        """Constructor for the IdpUserInfo class"""

        # Initialize members of the class
        self.groups = groups
        self.idp_id = idp_id
        self.issuer_id = issuer_id
        self.user_id = user_id
        self.vendor = vendor


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
        groups = dictionary.get('groups')
        idp_id = dictionary.get('idpId')
        issuer_id = dictionary.get('issuerId')
        user_id = dictionary.get('userId')
        vendor = dictionary.get('vendor')

        # Return an object of this model
        return cls(groups,
                   idp_id,
                   issuer_id,
                   user_id,
                   vendor)


