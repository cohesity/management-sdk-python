# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_domain_identity

class AdDomain(object):

    """Implementation of the 'AdDomain' model.

    Specifies information about an AD Domain.

    Attributes:
        dns_root (string): Specifies DNS root.
        forest (string): Specifies AD forest name.
        identity (AdDomainIdentity): AD domain identity information.
        netbios_name (string): Specifies AD NetBIOS name.
        parent_domain (string): Specifies parent domain name.
        tombstone_days (int): Specifies tombstone time in days.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns_root":'dnsRoot',
        "forest":'forest',
        "identity":'identity',
        "netbios_name":'netbiosName',
        "parent_domain":'parentDomain',
        "tombstone_days":'tombstoneDays'
    }

    def __init__(self,
                 dns_root=None,
                 forest=None,
                 identity=None,
                 netbios_name=None,
                 parent_domain=None,
                 tombstone_days=None):
        """Constructor for the AdDomain class"""

        # Initialize members of the class
        self.dns_root = dns_root
        self.forest = forest
        self.identity = identity
        self.netbios_name = netbios_name
        self.parent_domain = parent_domain
        self.tombstone_days = tombstone_days


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
        dns_root = dictionary.get('dnsRoot')
        forest = dictionary.get('forest')
        identity = cohesity_management_sdk.models.ad_domain_identity.AdDomainIdentity.from_dictionary(dictionary.get('identity')) if dictionary.get('identity') else None
        netbios_name = dictionary.get('netbiosName')
        parent_domain = dictionary.get('parentDomain')
        tombstone_days = dictionary.get('tombstoneDays')

        # Return an object of this model
        return cls(dns_root,
                   forest,
                   identity,
                   netbios_name,
                   parent_domain,
                   tombstone_days)


