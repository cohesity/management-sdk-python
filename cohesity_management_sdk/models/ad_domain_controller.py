# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_domain

class AdDomainController(object):

    """Implementation of the 'AdDomainController' model.

    Specifies information about an AD domain controller.

    Attributes:
        backup_supported (bool): Specifies whether backup of this domain
            controller is supported.
        backup_unsupported_reasons (list of string): Specifies any reason(s)
            for domain controller backup not supported.
        domain (AdDomain): Specifies information about an AD Domain.
        host_name (string): Specifies FQDN host name of the domain
            controller.
        is_global_catalog (bool): Specifies whether this domain controller is
            a global catalog server.
        is_read_only (bool): Specifies whether this domain controller is read
            only.
        utc_offset_min (int): Specifies UTC time offset of this domain
            controller in minutes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_supported":'backupSupported',
        "backup_unsupported_reasons":'backupUnsupportedReasons',
        "domain":'domain',
        "host_name":'hostName',
        "is_global_catalog":'isGlobalCatalog',
        "is_read_only":'isReadOnly',
        "utc_offset_min":'utcOffsetMin'
    }

    def __init__(self,
                 backup_supported=None,
                 backup_unsupported_reasons=None,
                 domain=None,
                 host_name=None,
                 is_global_catalog=None,
                 is_read_only=None,
                 utc_offset_min=None):
        """Constructor for the AdDomainController class"""

        # Initialize members of the class
        self.backup_supported = backup_supported
        self.backup_unsupported_reasons = backup_unsupported_reasons
        self.domain = domain
        self.host_name = host_name
        self.is_global_catalog = is_global_catalog
        self.is_read_only = is_read_only
        self.utc_offset_min = utc_offset_min


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
        backup_supported = dictionary.get('backupSupported')
        backup_unsupported_reasons = dictionary.get('backupUnsupportedReasons')
        domain = cohesity_management_sdk.models.ad_domain.AdDomain.from_dictionary(dictionary.get('domain')) if dictionary.get('domain') else None
        host_name = dictionary.get('hostName')
        is_global_catalog = dictionary.get('isGlobalCatalog')
        is_read_only = dictionary.get('isReadOnly')
        utc_offset_min = dictionary.get('utcOffsetMin')

        # Return an object of this model
        return cls(backup_supported,
                   backup_unsupported_reasons,
                   domain,
                   host_name,
                   is_global_catalog,
                   is_read_only,
                   utc_offset_min)


