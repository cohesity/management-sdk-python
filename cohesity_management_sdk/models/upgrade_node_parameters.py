# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpgradeNodeParameters(object):

    """Implementation of the 'UpgradeNodeParameters' model.

    Specifies the parameters needed for a Node upgrade request.

    Attributes:
        node_ids (list of long|int): Specifies a list of IDs of additional
            nodes to be upgraded. These must be free Nodes present on the same
            local network as the Node that the request was sent to. The ID of
            the Node the request was sent to should not be included in this
            list. This parameter can only be specified if upgradeAllFreeNodes
            is not.
        target_sw_version (string): Specifies the target software version. The
            node that the request is sent to will search itself for the
            specified software package and if that package is found, it will
            be used for the upgrade.
        upgrade_all_free_nodes (bool): Specifies whether or not to attempt to
            upgrade all free nodes which are currently connected to the same
            local network as the node that the request was sent to. This
            parameter can only be specified if nodeIds is not.
        upgrade_self (bool): Specifies that the node that the request is being
            sent to should be upgraded. By default this is set to true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "node_ids":'nodeIds',
        "target_sw_version":'targetSwVersion',
        "upgrade_all_free_nodes":'upgradeAllFreeNodes',
        "upgrade_self":'upgradeSelf'
    }

    def __init__(self,
                 node_ids=None,
                 target_sw_version=None,
                 upgrade_all_free_nodes=None,
                 upgrade_self=None):
        """Constructor for the UpgradeNodeParameters class"""

        # Initialize members of the class
        self.node_ids = node_ids
        self.target_sw_version = target_sw_version
        self.upgrade_all_free_nodes = upgrade_all_free_nodes
        self.upgrade_self = upgrade_self


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
        node_ids = dictionary.get('nodeIds')
        target_sw_version = dictionary.get('targetSwVersion')
        upgrade_all_free_nodes = dictionary.get('upgradeAllFreeNodes')
        upgrade_self = dictionary.get('upgradeSelf')

        # Return an object of this model
        return cls(node_ids,
                   target_sw_version,
                   upgrade_all_free_nodes,
                   upgrade_self)


