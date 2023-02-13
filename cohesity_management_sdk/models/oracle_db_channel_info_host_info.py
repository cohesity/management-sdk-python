# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_sbt_host_params

class OracleDBChannelInfoHostInfo(object):

    """Implementation of the 'OracleDBChannelInfo_HostInfo' model.

    The name of this proto message is out-dated. This proto should
    generally be used to represent parameters needed for each Oracle
    'cluster' node. 'cluster' here is a loose term used to include
    more than Oracle RAC cluster, e.g. 'active-passive' cluster is also
    considered here as 'cluster' and its 'cluster node will also be
    represented by the following proto.

    Attributes:
        host (string): 'agent_id' of the host from which we are allowed to
            take the backup/restore.
        num_channels (int): Number of channels we need to create for this
            host. Default value for num_channels will be calculated as minimum
            of number of nodes in cohesity cluster, 2 * number of cpu on
            Oracle host.
        portnum (long|int): port number where database is listening.
        sbt_host_params (OracleSbtHostParams): The necessury parameters for
            SBT. This is set only when backup type is kSbt.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "host":'host',
        "num_channels":'numChannels',
        "portnum":'portnum',
        "sbt_host_params":'sbtHostParams'
    }

    def __init__(self,
                 host=None,
                 num_channels=None,
                 portnum=None,
                 sbt_host_params=None):
        """Constructor for the OracleDBChannelInfoHostInfo class"""

        # Initialize members of the class
        self.host = host
        self.num_channels = num_channels
        self.portnum = portnum
        self.sbt_host_params = sbt_host_params


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
        host = dictionary.get('host')
        num_channels = dictionary.get('numChannels')
        portnum = dictionary.get('portnum')
        sbt_host_params = cohesity_management_sdk.models.oracle_sbt_host_params.OracleSbtHostParams.from_dictionary(dictionary.get('sbtHostParams')) if dictionary.get('sbtHostParams') else None

        # Return an object of this model
        return cls(host,
                   num_channels,
                   portnum,
                   sbt_host_params)


