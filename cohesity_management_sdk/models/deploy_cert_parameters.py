# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.host_info

class DeployCertParameters(object):

    """Implementation of the 'DeployCertParameters' model.

    Specifies the parameters used to generate and deploy a certificate.

    Attributes:
        cert_file_name (string): Specifies the filename of the certificate.
        hosts_info_list (list of HostInfo): Specifies the list of all hosts on
            which the certificate is to be deployed.
        mtype (TypeDeployCertParametersEnum): Specifies the type of the host
            such as 'kSapHana', 'kSapOracle', etc. Specifies the host type of
            host for generating and deploying a Certificate. 'kOther'
            indicates it is any of the other hosts. 'kSapOracle' indicates it
            is a SAP Oracle host. 'kSapHana' indicates it is a SAP HANA host.
        valid_days (long|int): Specifies the number of days after which the
            certificate will expire. The user has to input the number of days
            (from the current date) till when the certificate is valid.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cert_file_name":'certFileName',
        "hosts_info_list":'hostsInfoList',
        "mtype":'type',
        "valid_days":'validDays'
    }

    def __init__(self,
                 cert_file_name=None,
                 hosts_info_list=None,
                 mtype=None,
                 valid_days=None):
        """Constructor for the DeployCertParameters class"""

        # Initialize members of the class
        self.cert_file_name = cert_file_name
        self.hosts_info_list = hosts_info_list
        self.mtype = mtype
        self.valid_days = valid_days


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
        cert_file_name = dictionary.get('certFileName')
        hosts_info_list = None
        if dictionary.get('hostsInfoList') != None:
            hosts_info_list = list()
            for structure in dictionary.get('hostsInfoList'):
                hosts_info_list.append(cohesity_management_sdk.models.host_info.HostInfo.from_dictionary(structure))
        mtype = dictionary.get('type')
        valid_days = dictionary.get('validDays')

        # Return an object of this model
        return cls(cert_file_name,
                   hosts_info_list,
                   mtype,
                   valid_days)


