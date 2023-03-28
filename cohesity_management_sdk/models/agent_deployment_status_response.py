# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AgentDeploymentStatusResponse(object):

    """Implementation of the 'AgentDeploymentStatusResponse' model.

    Specifies the overview of the agent deployment status.


    Attributes:

        compact_version (string): Specifies the compact version of Cohesity
            agent. For example, 6.0.1.
        health_status (HealthStatusEnum): Specifies the health status of the
            Cohesity agent. Specifies the status of the agent running on a
            physical source. 'kUnknown' indicates the Agent is not known. No
            attempt to connect to the Agent has occurred. 'kUnreachable'
            indicates the Agent is not reachable. 'kHealthy' indicates the
            Agent is healthy. 'kDegraded' indicates the Agent is running but in
            a degraded state.
        host_ip (string): Specifies the IP of the host on which the agent is
            installed.
        host_os_type (HostOsTypeEnum): Specifies the host type on which the
            agent is installed. 'kLinux' indicates the Linux operating system.
            'kWindows' indicates the Microsoft Windows operating system. 'kAix'
            indicates the IBM AIX operating system. 'kSolaris' indicates the
            Oracle Solaris operating system. 'kSapHana' indicates the Sap Hana
            database system developed by SAP SE. 'kSapOracle' indicates the Sap
            Oracle database system developed by SAP SE. 'kCockroachDB'
            indicates the CockroachDB database system. 'kMySQL' indicates the
            MySQL database system. 'kOther' indicates the other types of
            operating system.
        last_upgrade_status (LastUpgradeStatusEnum): Specifies the status of
            the last upgrade attempt. Specifies the status of the upgrade of
            the agent on a physical server. 'kIdle' indicates there is no agent
            upgrade in progress. 'kAccepted' indicates the Agent upgrade is
            accepted. 'kStarted' indicates the Agent upgrade is in progress.
            'kFinished' indicates the Agent upgrade is completed. 'kScheduled'
            indicates that the Agent is scheduled for upgrade.
        upgradability (UpgradabilityEnum): Specifies the upgradability of the
            agent running on the server. Specifies the upgradability of the
            agent running on the physical server. 'kUpgradable' indicates the
            Agent can be upgraded to the agent software version on the cluster.
            'kCurrent' indicates the Agent is running the latest version.
            'kUnknown' indicates the Agent's version is not known.
            'kNonUpgradableInvalidVersion' indicates the Agent's version is
            invalid. 'kNonUpgradableAgentIsNewer' indicates the Agent's version
            is newer than the agent software version the cluster.
            'kNonUpgradableAgentIsOld' indicates the Agent's version is too old
            that does not support upgrades.
        upgrade_status_message (string): Specifies detailed message about the
            agent upgrade failure. This field is not set for successful
            upgrade.
        version (string): Specifies the Cohesity software version of the agent.
            For example: 6.0.1-release-YYYYMMDD_<hash>
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "compact_version":'compactVersion',
        "health_status":'healthStatus',
        "host_ip":'hostIp',
        "host_os_type":'hostOsType',
        "last_upgrade_status":'lastUpgradeStatus',
        "upgradability":'upgradability',
        "upgrade_status_message":'upgradeStatusMessage',
        "version":'version',
    }
    def __init__(self,
                 compact_version=None,
                 health_status=None,
                 host_ip=None,
                 host_os_type=None,
                 last_upgrade_status=None,
                 upgradability=None,
                 upgrade_status_message=None,
                 version=None,
            ):

        """Constructor for the AgentDeploymentStatusResponse class"""

        # Initialize members of the class
        self.compact_version = compact_version
        self.health_status = health_status
        self.host_ip = host_ip
        self.host_os_type = host_os_type
        self.last_upgrade_status = last_upgrade_status
        self.upgradability = upgradability
        self.upgrade_status_message = upgrade_status_message
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
        compact_version = dictionary.get('compactVersion')
        health_status = dictionary.get('healthStatus')
        host_ip = dictionary.get('hostIp')
        host_os_type = dictionary.get('hostOsType')
        last_upgrade_status = dictionary.get('lastUpgradeStatus')
        upgradability = dictionary.get('upgradability')
        upgrade_status_message = dictionary.get('upgradeStatusMessage')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(
            compact_version,
            health_status,
            host_ip,
            host_os_type,
            last_upgrade_status,
            upgradability,
            upgrade_status_message,
            version
)