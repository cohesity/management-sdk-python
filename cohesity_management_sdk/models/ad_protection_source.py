# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_domain_controller

class AdProtectionSource(object):

    """Implementation of the 'AdProtectionSource' model.

    Specifies an object representing an AD entity.

    Attributes:
        domain_controller (AdDomainController): Specifies information about an
            AD domain controller.
        domain_name (string): Specifies the domain name corresponding to the
            domain controller.
        name (string): Specifies the domain name of the AD entity.
        owner_id (long|int): Specifies the entity id of the owner entity.
        mtype (TypeAdProtectionSourceEnum): Specifies the type of the managed
            object in AD Protection Source. Specifies the kind of AD
            protection source. 'kRootContainer' indicates the entity is a root
            container to an AD domain controller. 'kDomainController'
            indicates the domain controller hosted in this physical server.
        uuid (string): Specifies the UUID for the AD entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain_controller":'domainController',
        "domain_name":'domainName',
        "name":'name',
        "owner_id":'ownerId',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 domain_controller=None,
                 domain_name=None,
                 name=None,
                 owner_id=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the AdProtectionSource class"""

        # Initialize members of the class
        self.domain_controller = domain_controller
        self.domain_name = domain_name
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
        domain_name = dictionary.get('domainName')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(domain_controller,
                   domain_name,
                   name,
                   owner_id,
                   mtype,
                   uuid)


