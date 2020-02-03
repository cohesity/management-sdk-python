# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class UpdateLinuxPasswordReqParams(object):

    """Implementation of the 'UpdateLinuxPasswordReqParams' model.

    Specifies the user input parameters.

    Attributes:
        cluster_id (long|int): If cluster ID is specified, then the password
            is updated for all the nodes in the cluster. Optional Field.
        linux_password (string): Specifies the new linux password.
        linux_username (string): Specifies the linux username for which the
            password will be updated.
        node_ips (list of string): Specifies the node IP address on which the
            linux password will be updated. Optional Field.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "linux_password":'linuxPassword',
        "linux_username":'linuxUsername',
        "cluster_id":'clusterId',
        "node_ips":'nodeIps'
    }

    def __init__(self,
                 linux_password=None,
                 linux_username=None,
                 cluster_id=None,
                 node_ips=None):
        """Constructor for the UpdateLinuxPasswordReqParams class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.linux_password = linux_password
        self.linux_username = linux_username
        self.node_ips = node_ips


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
        linux_password = dictionary.get('linuxPassword')
        linux_username = dictionary.get('linuxUsername')
        cluster_id = dictionary.get('clusterId')
        node_ips = dictionary.get('nodeIps')

        # Return an object of this model
        return cls(linux_password,
                   linux_username,
                   cluster_id,
                   node_ips)


