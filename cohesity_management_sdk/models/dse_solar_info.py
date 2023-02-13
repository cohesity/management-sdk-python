# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DSESolrInfo(object):

    """Implementation of the 'DSESolrInfo' model.

    Message to hold information about DSE Solr node.

    Attributes:
        solr_node_vec (list of string): Solr node IP Addresses.
        solr_port (int): Solr node Port.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "solr_node_vec":'solrNodeVec',
        "solr_port":'solrPort'
    }

    def __init__(self,
                 solr_node_vec=None,
                 solr_port=None):
        """Constructor for the DSESolrInfo class"""

        # Initialize members of the class
        self.solr_node_vec = solr_node_vec
        self.solr_port = solr_port


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
        solr_node_vec = dictionary.get('solrNodeVec')
        solr_port = dictionary.get('solrPort')

        # Return an object of this model
        return cls(solr_node_vec,
                   solr_port)


