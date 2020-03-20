# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.ad_domain_controller

class AdProtectionSource(object):

    """Implementation of the 'AdProtectionSource' model.

    Specifies an object representing an AD entity.

    Attributes:
        domain_controller (AdDomainController): Specifies information about an
            AD domain controller.
        name (string): Specifies the domain name of the AD entity.
        owner_id (long|int): Specifies the entity id of the owner entity.
        mtype (int): Specifies the type of the managed object in AD Protection
            Source.
        uuid (string): Specifies the UUID for the AD entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain_controller":'domainController',
        "name":'name',
        "owner_id":'ownerId',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 domain_controller=None,
                 name=None,
                 owner_id=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the AdProtectionSource class"""

        # Initialize members of the class
        self.domain_controller = domain_controller
        self.name = name
        self.owner_id = owner_id
        self.mtype = mtype
        self.uuid = uuid


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
        domain_controller = cohesity_management_sdk.models.ad_domain_controller.AdDomainController.from_dictionary(dictionary.get('domainController')) if dictionary.get('domainController') else None
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(domain_controller,
                   name,
                   owner_id,
                   mtype,
                   uuid)


