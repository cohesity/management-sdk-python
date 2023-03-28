# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ConnectorParameters(object):

    """Implementation of the 'ConnectorParameters' model.

    Specifies the parameters required to establish a connection with a
    particular environment.


    Attributes:

        connection_id (long|int): ID of the Bifrost (HyX or Rigel) network
            realm (i.e. a connection) associated with the source.
        connector_group_id (long|int): Specifies the Id of the connector group.
            Each connector group is collection of Rigel/hyx. Each entity will
            be tagged with connector group id.
        endpoint (string): Specify an IP address or URL of the environment.
            (such as the IP address of the vCenter Server for a VMware
            environment).
        environment (EnvironmentConnectorParametersEnum): Specifies the
            environment like VMware, SQL, where the Protection Source exists.
            Supported environment types such as 'kView', 'kSQL', 'kVMware',
            etc. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
            'kVMware' indicates the VMware Protection Source environment.
            'kHyperV' indicates the HyperV Protection Source environment.
            'kSQL' indicates the SQL Protection Source environment. 'kView'
            indicates the View Protection Source environment. 'kPuppeteer'
            indicates the Cohesity's Remote Adapter. 'kPhysical' indicates the
            physical Protection Source environment. 'kPure' indicates the Pure
            Storage Protection Source environment. 'kNimble' indicates the
            Nimble Storage Protection Source environment. 'kAzure' indicates
            the Microsoft's Azure Protection Source environment. 'kNetapp'
            indicates the Netapp Protection Source environment. 'kAgent'
            indicates the Agent Protection Source environment. 'kGenericNas'
            indicates the Generic Network Attached Storage Protection Source
            environment. 'kAcropolis' indicates the Acropolis Protection Source
            environment. 'kPhysicalFiles' indicates the Physical Files
            Protection Source environment. 'kIsilon' indicates the Dell EMC's
            Isilon Protection Source environment. 'kGPFS' indicates IBM's GPFS
            Protection Source environment. 'kKVM' indicates the KVM Protection
            Source environment. 'kAWS' indicates the AWS Protection Source
            environment. 'kExchange' indicates the Exchange Protection Source
            environment. 'kHyperVVSS' indicates the HyperV VSS Protection
            Source environment. 'kOracle' indicates the Oracle Protection
            Source environment. 'kGCP' indicates the Google Cloud Platform
            Protection Source environment. 'kFlashBlade' indicates the Flash
            Blade Protection Source environment. 'kAWSNative' indicates the AWS
            Native Protection Source environment. 'kO365' indicates the Office
            365 Protection Source environment. 'kO365Outlook' indicates Office
            365 outlook Protection Source environment. 'kHyperFlex' indicates
            the Hyper Flex Protection Source environment. 'kGCPNative'
            indicates the GCP Native Protection Source environment.
            'kAzureNative' indicates the Azure Native Protection Source
            environment. 'kKubernetes' indicates a Kubernetes Protection Source
            environment. 'kElastifile' indicates Elastifile Protection Source
            environment. 'kAD' indicates Active Directory Protection Source
            environment. 'kRDSSnapshotManager' indicates AWS RDS Protection
            Source environment. 'kCassandra' indicates Cassandra Protection
            Source environment. 'kMongoDB' indicates MongoDB Protection Source
            environment. 'kCouchbase' indicates Couchbase Protection Source
            environment. 'kHdfs' indicates Hdfs Protection Source environment.
            'kHive' indicates Hive Protection Source environment. 'kHBase'
            indicates HBase Protection Source environment. 'kUDA' indicates
            Universal Data Adapter Protection Source environment. 'kO365Teams'
            indicates the Office365 Teams Protection Source environment.
            'kO365Group' indicates the Office365 Groups Protection Source
            environment. 'kO365Exchange' indicates the Office365 Mailbox
            Protection Source environment. 'kO365OneDrive' indicates the
            Office365 OneDrive Protection Source environment. 'kO365Sharepoint'
            indicates the Office365 SharePoint Protection Source environment.
            'kO365PublicFolders' indicates the Office365 PublicFolders
            Protection Source environment.
        id (long|int): Specifies a Unique id that is generated when the Source
            is registered. This is a convenience field that is used to maintain
            an index to different connection params.
        version (long|int): Version is updated each time the connector
            parameters are updated. This is used to discard older connector
            parameters.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "connection_id":'connectionId',
        "connector_group_id":'connectorGroupId',
        "endpoint":'endpoint',
        "environment":'environment',
        "id":'id',
        "version":'version',
    }
    def __init__(self,
                 connection_id=None,
                 connector_group_id=None,
                 endpoint=None,
                 environment=None,
                 id=None,
                 version=None,
            ):

        """Constructor for the ConnectorParameters class"""

        # Initialize members of the class
        self.connection_id = connection_id
        self.connector_group_id = connector_group_id
        self.endpoint = endpoint
        self.environment = environment
        self.id = id
        self.version = version

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
        connection_id = dictionary.get('connectionId')
        connector_group_id = dictionary.get('connectorGroupId')
        endpoint = dictionary.get('endpoint')
        environment = dictionary.get('environment')
        id = dictionary.get('id')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(
            connection_id,
            connector_group_id,
            endpoint,
            environment,
            id,
            version
)