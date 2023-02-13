# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpgradePhysicalServerAgents(object):

    """Implementation of the 'UpgradePhysicalServerAgents' model.

    Specifies a request to upgrade the Cohesity agents on one or more
    Physical Servers registered on the Cohesity Cluster.

    Attributes:
        agent_ids (list of long|int): Array of Agent Ids.  Specifies a list of
            agentIds associated with the Physical Servers to upgrade with the
            agent release currently available from the Cohesity Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agent_ids":'agentIds'
    }

    def __init__(self,
                 agent_ids=None):
        """Constructor for the UpgradePhysicalServerAgents class"""

        # Initialize members of the class
        self.agent_ids = agent_ids


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
        agent_ids = dictionary.get('agentIds')

        # Return an object of this model
        return cls(agent_ids)


