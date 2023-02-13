# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.certificate_details

class ListCertResponse(object):

    """Implementation of the 'ListCertResponse' model.

    Specifies list of all certificates deployed from the cluster.

    Attributes:
        certificate_list (list of CertificateDetails): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "certificate_list":'certificateList'
    }

    def __init__(self,
                 certificate_list=None):
        """Constructor for the ListCertResponse class"""

        # Initialize members of the class
        self.certificate_list = certificate_list


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
        certificate_list = None
        if dictionary.get('certificateList') != None:
            certificate_list = list()
            for structure in dictionary.get('certificateList'):
                certificate_list.append(cohesity_management_sdk.models.certificate_details.CertificateDetails.from_dictionary(structure))

        # Return an object of this model
        return cls(certificate_list)


