# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.application_special_parameters
import cohesity_management_sdk.models.oracle_special_parameters
import cohesity_management_sdk.models.physical_special_parameters
import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.vmware_special_parameters

class SourceSpecialParameter(object):

    """Implementation of the 'SourceSpecialParameter' model.

    Specifies additional special settings for a single Source in a Protection
    Job. This Source must be a leaf node in the Source tree.

    Attributes:
        ad_special_parameters (ApplicationSpecialParameters): Specifies
            additional special settings applicable for a Protection Source of
            'kSQL'/'kOracle' type in a Protection Job.
        exchange_special_parameters (ApplicationSpecialParameters): Specifies
            additional special parameters that are applicable only to
            Protection Sources of 'kExchange' type.
        oracle_special_parameters (OracleSpecialParameters): Specifies special
            settings applicable for 'kOracle' environment.
        physical_special_parameters (PhysicalSpecialParameters): Specifies
            additional special settings applicable for a Protection Source of
            'kPhysical' type in a Protection Job.
        skip_indexing (bool): Specifies not to index the objects in the
            Protection Source when backing up.
        source_id (long|int): Specifies the object id of the Protection Source
            that these special settings apply. This field must refer to a leaf
            node such a VM or a Physical Server.
        sql_special_parameters (ApplicationSpecialParameters): Specifies
            additional special settings applicable for a Protection Source of
            'kSQL'/'kOracle' type in a Protection Job.
        truncate_exchange_log (bool): If true, after the Cohesity Cluster
            successfully captures a Snapshot during a Job Run, the Cluster
            truncates the Exchange transaction logs on a Microsoft Exchange
            Server. The default value is false. This field is deprecated. Use
            the field in ApplicationParameters inside source specific
            parameter. deprecated: true
        vm_credentials (Credentials): Specifies the administrator credentials
            to log in to the guest Windows system of a VM that hosts the
            Microsoft Exchange Server. If truncateExchangeLog is set to true
            and the specified source is a VM, administrator credentials to log
            in to the guest Windows system of the VM must be provided to
            truncate the logs. This field is only applicable to Sources in the
            kVMware environment. This field is deprecated. Use the field in
            VmCredentials inside source specific parameter. deprecated: true
        vmware_special_parameters (VmwareSpecialParameters): Specifies
            additional special settings applicable for a Protection Source of
            'kVMware' type in a Protection Job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_special_parameters":'adSpecialParameters',
        "exchange_special_parameters":'exchangeSpecialParameters',
        "oracle_special_parameters":'oracleSpecialParameters',
        "physical_special_parameters":'physicalSpecialParameters',
        "skip_indexing":'skipIndexing',
        "source_id":'sourceId',
        "sql_special_parameters":'sqlSpecialParameters',
        "truncate_exchange_log":'truncateExchangeLog',
        "vm_credentials":'vmCredentials',
        "vmware_special_parameters":'vmwareSpecialParameters'
    }

    def __init__(self,
                 ad_special_parameters=None,
                 exchange_special_parameters=None,
                 oracle_special_parameters=None,
                 physical_special_parameters=None,
                 skip_indexing=None,
                 source_id=None,
                 sql_special_parameters=None,
                 truncate_exchange_log=None,
                 vm_credentials=None,
                 vmware_special_parameters=None):
        """Constructor for the SourceSpecialParameter class"""

        # Initialize members of the class
        self.ad_special_parameters = ad_special_parameters
        self.exchange_special_parameters = exchange_special_parameters
        self.oracle_special_parameters = oracle_special_parameters
        self.physical_special_parameters = physical_special_parameters
        self.skip_indexing = skip_indexing
        self.source_id = source_id
        self.sql_special_parameters = sql_special_parameters
        self.truncate_exchange_log = truncate_exchange_log
        self.vm_credentials = vm_credentials
        self.vmware_special_parameters = vmware_special_parameters


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
        ad_special_parameters = cohesity_management_sdk.models.application_special_parameters.ApplicationSpecialParameters.from_dictionary(dictionary.get('adSpecialParameters')) if dictionary.get('adSpecialParameters') else None
        exchange_special_parameters =  cohesity_management_sdk.models.application_special_parameters.ApplicationSpecialParameters.from_dictionary(dictionary.get('exchangeSpecialParameters')) if dictionary.get('exchangeSpecialParameters') else None
        oracle_special_parameters = cohesity_management_sdk.models.oracle_special_parameters.OracleSpecialParameters.from_dictionary(dictionary.get('oracleSpecialParameters')) if dictionary.get('oracleSpecialParameters') else None
        physical_special_parameters = cohesity_management_sdk.models.physical_special_parameters.PhysicalSpecialParameters.from_dictionary(dictionary.get('physicalSpecialParameters')) if dictionary.get('physicalSpecialParameters') else None
        skip_indexing = dictionary.get('skipIndexing')
        source_id = dictionary.get('sourceId')
        sql_special_parameters = cohesity_management_sdk.models.application_special_parameters.ApplicationSpecialParameters.from_dictionary(dictionary.get('sqlSpecialParameters')) if dictionary.get('sqlSpecialParameters') else None
        truncate_exchange_log = dictionary.get('truncateExchangeLog')
        vm_credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('vmCredentials')) if dictionary.get('vmCredentials') else None
        vmware_special_parameters = cohesity_management_sdk.models.vmware_special_parameters.VmwareSpecialParameters.from_dictionary(dictionary.get('vmwareSpecialParameters')) if dictionary.get('vmwareSpecialParameters') else None

        # Return an object of this model
        return cls(ad_special_parameters,
                   exchange_special_parameters,
                   oracle_special_parameters,
                   physical_special_parameters,
                   skip_indexing,
                   source_id,
                   sql_special_parameters,
                   truncate_exchange_log,
                   vm_credentials,
                   vmware_special_parameters)


