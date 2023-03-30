# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NodeIpmiUser(object):

    """Implementation of the 'NodeIpmiUser' model.

    TODO: type description here.


    Attributes:

        ipmi_password (string): In request, IPMI password is entered by the
            user. In response, it is is set to empty and hence will be omitted.
        ipmi_user (string): TODO: Type description here.
        node_ip (string): TODO: Type description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "ipmi_password":'ipmiPassword',
        "ipmi_user":'ipmiUser',
        "node_ip":'nodeIp',
    }
    def __init__(self,
                 ipmi_password=None,
                 ipmi_user=None,
                 node_ip=None,
            ):

        """Constructor for the NodeIpmiUser class"""

        # Initialize members of the class
        self.ipmi_password = ipmi_password
        self.ipmi_user = ipmi_user
        self.node_ip = node_ip

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
        ipmi_password = dictionary.get('ipmiPassword')
        ipmi_user = dictionary.get('ipmiUser')
        node_ip = dictionary.get('nodeIp')

        # Return an object of this model
        return cls(
            ipmi_password,
            ipmi_user,
            node_ip
)