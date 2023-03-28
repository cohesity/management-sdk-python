# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cbt_info
import cohesity_management_sdk.models.registered_source_info


class AgentInformation(object):

    """Implementation of the 'AgentInformation' model.

    Specifies information about the Agent software running on the server or the
    Virtual Machine.


    Attributes:

        cbmr_version (string): Specifies the version if Cristie BMR product is
            installed on the host.
        file_cbt_info (CbtInfo): Specifies the status of FileCbt driver
            associated with the agent.
        host_type (HostTypeEnum): Specifies the host type where the agent is
            running. This is only set for persistent agents. 'kLinux' indicates
            the Linux operating system. 'kWindows' indicates the Microsoft
            Windows operating system. 'kAix' indicates the IBM AIX operating
            system. 'kSolaris' indicates the Oracle Solaris operating system.
            'kSapHana' indicates the Sap Hana database system developed by SAP
            SE. 'kSapOracle' indicates the Sap Oracle database system developed
            by SAP SE. 'kCockroachDB' indicates the CockroachDB database
            system. 'kMySQL' indicates the MySQL database system. 'kOther'
            indicates the other types of operating system.
        id (long|int): Specifies the agent's id.
        name (string): Specifies the agent's name.
        oracle_multi_node_channel_supported (bool): Specifies whether oracle
            multi node multi channel is supported or not.
        registration_info (RegisteredSourceInfo): Specifies registration
            information for an Agent.
        source_side_dedup_enabled (bool): Specifies whether source side dedup
            is enabled or not.
        status (StatusAgentInformationEnum): Specifies the agent status.
            Specifies the status of the agent running on a physical source.
            'kUnknown' indicates the Agent is not known. No attempt to connect
            to the Agent has occurred. 'kUnreachable' indicates the Agent is
            not reachable. 'kHealthy' indicates the Agent is healthy.
            'kDegraded' indicates the Agent is running but in a degraded state.
        status_message (string): Specifies additional details about the agent
            status.
        upgradability (UpgradabilityEnum): Specifies the upgradability of the
            agent running on the physical server. Specifies the upgradability
            of the agent running on the physical server. 'kUpgradable'
            indicates the Agent can be upgraded to the agent software version
            on the cluster. 'kCurrent' indicates the Agent is running the
            latest version. 'kUnknown' indicates the Agent's version is not
            known. 'kNonUpgradableInvalidVersion' indicates the Agent's version
            is invalid. 'kNonUpgradableAgentIsNewer' indicates the Agent's
            version is newer than the agent software version the cluster.
            'kNonUpgradableAgentIsOld' indicates the Agent's version is too old
            that does not support upgrades.
        upgrade_status (UpgradeStatusEnum): Specifies the status of the upgrade
            of the agent on a physical server. Specifies the status of the
            upgrade of the agent on a physical server. 'kIdle' indicates there
            is no agent upgrade in progress. 'kAccepted' indicates the Agent
            upgrade is accepted. 'kStarted' indicates the Agent upgrade is in
            progress. 'kFinished' indicates the Agent upgrade is completed.
            'kScheduled' indicates that the Agent is scheduled for upgrade.
        upgrade_status_message (string): Specifies detailed message about the
            agent upgrade failure. This field is not set for successful
            upgrade.
        version (string): Specifies the version of the Agent software.
        vol_cbt_info (CbtInfo): Specifies the status of VolCbt driver
            associated with the agent.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cbmr_version":'cbmrVersion',
        "file_cbt_info":'fileCbtInfo',
        "host_type":'hostType',
        "id":'id',
        "name":'name',
        "oracle_multi_node_channel_supported":'oracleMultiNodeChannelSupported',
        "registration_info":'registrationInfo',
        "source_side_dedup_enabled":'sourceSideDedupEnabled',
        "status":'status',
        "status_message":'statusMessage',
        "upgradability":'upgradability',
        "upgrade_status":'upgradeStatus',
        "upgrade_status_message":'upgradeStatusMessage',
        "version":'version',
        "vol_cbt_info":'volCbtInfo',
    }
    def __init__(self,
                 cbmr_version=None,
                 file_cbt_info=None,
                 host_type=None,
                 id=None,
                 name=None,
                 oracle_multi_node_channel_supported=None,
                 registration_info=None,
                 source_side_dedup_enabled=None,
                 status=None,
                 status_message=None,
                 upgradability=None,
                 upgrade_status=None,
                 upgrade_status_message=None,
                 version=None,
                 vol_cbt_info=None,
            ):

        """Constructor for the AgentInformation class"""

        # Initialize members of the class
        self.cbmr_version = cbmr_version
        self.file_cbt_info = file_cbt_info
        self.host_type = host_type
        self.id = id
        self.name = name
        self.oracle_multi_node_channel_supported = oracle_multi_node_channel_supported
        self.registration_info = registration_info
        self.source_side_dedup_enabled = source_side_dedup_enabled
        self.status = status
        self.status_message = status_message
        self.upgradability = upgradability
        self.upgrade_status = upgrade_status
        self.upgrade_status_message = upgrade_status_message
        self.version = version
        self.vol_cbt_info = vol_cbt_info

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
        cbmr_version = dictionary.get('cbmrVersion')
        file_cbt_info = cohesity_management_sdk.models.cbt_info.CbtInfo.from_dictionary(dictionary.get('fileCbtInfo')) if dictionary.get('fileCbtInfo') else None
        host_type = dictionary.get('hostType')
        id = dictionary.get('id')
        name = dictionary.get('name')
        oracle_multi_node_channel_supported = dictionary.get('oracleMultiNodeChannelSupported')
        registration_info = cohesity_management_sdk.models.registered_source_info.RegisteredSourceInfo.from_dictionary(dictionary.get('registrationInfo')) if dictionary.get('registrationInfo') else None
        source_side_dedup_enabled = dictionary.get('sourceSideDedupEnabled')
        status = dictionary.get('status')
        status_message = dictionary.get('statusMessage')
        upgradability = dictionary.get('upgradability')
        upgrade_status = dictionary.get('upgradeStatus')
        upgrade_status_message = dictionary.get('upgradeStatusMessage')
        version = dictionary.get('version')
        vol_cbt_info = cohesity_management_sdk.models.cbt_info.CbtInfo.from_dictionary(dictionary.get('volCbtInfo')) if dictionary.get('volCbtInfo') else None

        # Return an object of this model
        return cls(
            cbmr_version,
            file_cbt_info,
            host_type,
            id,
            name,
            oracle_multi_node_channel_supported,
            registration_info,
            source_side_dedup_enabled,
            status,
            status_message,
            upgradability,
            upgrade_status,
            upgrade_status_message,
            version,
            vol_cbt_info
)