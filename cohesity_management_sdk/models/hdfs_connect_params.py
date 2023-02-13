# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HdfsConnectParams(object):

    """Implementation of the 'HdfsConnectParams' model.

    Specifies an Object containing information about a registered Hdfs
    source.

    Attributes:
        hadoop_distribution (HadoopDistributionEnum): Specifies the Hadoop
            Distribution.
            Hadoop distribution.

            'CDH' indicates Hadoop distribution type Cloudera.
            'HDP' indicates Hadoop distribution type Hortonworks.
        hadoop_version (string): Specifies the Hadoop version
        kerberos_principal (string): Specifies the kerberos principal.
        namenode (string): Specifies the Namenode host or Nameservice.
        port (int): Specifies the Webhdfs Port
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hadoop_distribution": 'hadoopDistribution',
        "hadoop_version": 'hadoopVersion',
        "kerberos_principal":'kerberosPrincipal',
        "namenode": 'namenode',
        "port":'port'
    }

    def __init__(self,
                 hadoop_distribution=None,
                 hadoop_version=None,
                 kerberos_principal=None,
                 namenode=None,
                 port=None):
        """Constructor for the HdfsConnectParams class"""

        # Initialize members of the class
        self.hadoop_distribution = hadoop_distribution
        self.hadoop_version = hadoop_version
        self.kerberos_principal = kerberos_principal
        self.namenode = namenode
        self.port = port


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
        hadoop_distribution = dictionary.get('hadoopDistribution')
        hadoop_version = dictionary.get('hadoopVersion')
        kerberos_principal = dictionary.get('kerberosPrincipal')
        namenode = dictionary.get('namenode')
        port = dictionary.get('port')

        # Return an object of this model
        return cls(hadoop_distribution,
                   hadoop_version,
                   kerberos_principal,
                   namenode,
                   port)


