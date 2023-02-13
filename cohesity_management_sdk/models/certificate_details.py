# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CertificateDetails(object):

    """Implementation of the 'CertificateDetails' model.

    Specifies details about a certificate.

    Attributes:
        cert_file_name (string): Specifies the filename of the certificate.
            This is unique to each certificate generated.
        expiry_date (string): Specifies the date in epoch till when the
            certificate is valid.
        host_ips (list of string): Each certificate can be deployed to
            multiple hosts. List of all hosts is returned after deployment.
        mtype (TypeCertificateDetailsEnum): Specifies the type of the host
            such as 'kSapHana', 'kSapOracle', etc. Specifies the host type of
            host for generating and deploying a Certificate. 'kOther'
            indicates it is any of the other hosts. 'kSapOracle' indicates it
            is a SAP Oracle host. 'kSapHana' indicates it is a SAP HANA host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cert_file_name":'certFileName',
        "expiry_date":'expiryDate',
        "host_ips":'hostIps',
        "mtype":'type'
    }

    def __init__(self,
                 cert_file_name=None,
                 expiry_date=None,
                 host_ips=None,
                 mtype=None):
        """Constructor for the CertificateDetails class"""

        # Initialize members of the class
        self.cert_file_name = cert_file_name
        self.expiry_date = expiry_date
        self.host_ips = host_ips
        self.mtype = mtype


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
        expiry_date = dictionary.get('expiryDate')
        host_ips = dictionary.get('hostIps')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(cert_file_name,
                   expiry_date,
                   host_ips,
                   mtype)


