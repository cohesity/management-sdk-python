# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.agent_information
import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.networking_information
import cohesity_management_sdk.models.physical_volume
import cohesity_management_sdk.models.vss_writer

class PhysicalProtectionSource(object):

    """Implementation of the 'PhysicalProtectionSource' model.

    Specifies a Protection Source in a Physical environment.

    Attributes:
        agents (list of AgentInformation): Array of Agents on the Physical
            Protection Source.  Specifiles the agents running on the Physical
            Protection Source and the status information.
        host_name (string): Specifies the hostname.
        host_type (HostTypePhysicalProtectionSourceEnum): Specifies the
            environment type for the host. 'kLinux' indicates the Linux
            operating system. 'kWindows' indicates the Microsoft Windows
            operating system. 'kAix' indicates the IBM AIX operating system.
            'kSolaris' indicates the Oracle Solaris operating system.
            'kSapHana' indicates the Sap Hana database system developed by SAP
            SE. 'kOther' indicates the other types of operating system.
        id (UniversalId): Specifies a unique id of a Physical Protection
            Source. The id is unique across Cohesity Clusters.
        is_proxy_host (bool): Specifies if the physical host is a proxy host.
        memory_size_bytes (long|int): Specifies the total memory on the host
            in bytes.
        name (string): Specifies a human readable name of the Protection
            Source.
        networking_info (NetworkingInformation): Specifies the struct
            containing information about network addresses configured on the
            given box. This is needed for dealing with Windows/Oracle Cluster
            resources that we discover and protect automatically.
        num_processors (long|int): Specifies the number of processors on the
            host.
        os_name (string): Specifies a human readable name of the OS of the
            Protection Source.
        mtype (TypePhysicalProtectionSourceEnum): Specifies the type of
            managed Object in a Physical Protection Source. 'kGroup' indicates
            the EH container. 'kHost' indicates a single physical server.
            'kWindowsCluster' indicates a Microsoft Windows cluster.
            'kOracleRACCluster' indicates an Oracle Real Application
            Cluster(RAC). 'kOracleAPCluster' indicates an Oracle
            Active-Passive Cluster.
        vcs_version (string): Specifies cluster version for VCS host.
        volumes (list of PhysicalVolume): Array of Physical Volumes.
            Specifies the volumes available on the physical host. These fields
            are populated only for the kPhysicalHost type.
        vsswriters (list of VssWriter): Specifies the list of writers
            available on the physical host. These fields are populated only
            for the kPhysicalHost type, particularly when the host is windows

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agents":'agents',
        "host_name":'hostName',
        "host_type":'hostType',
        "id":'id',
        "is_proxy_host":'isProxyHost',
        "memory_size_bytes":'memorySizeBytes',
        "name":'name',
        "networking_info":'networkingInfo',
        "num_processors":'numProcessors',
        "os_name":'osName',
        "mtype":'type',
        "vcs_version":'vcsVersion',
        "volumes":'volumes',
        "vsswriters":'vsswriters'
    }

    def __init__(self,
                 agents=None,
                 host_name=None,
                 host_type=None,
                 id=None,
                 is_proxy_host=None,
                 memory_size_bytes=None,
                 name=None,
                 networking_info=None,
                 num_processors=None,
                 os_name=None,
                 mtype=None,
                 vcs_version=None,
                 volumes=None,
                 vsswriters=None):
        """Constructor for the PhysicalProtectionSource class"""

        # Initialize members of the class
        self.agents = agents
        self.host_name = host_name
        self.host_type = host_type
        self.id = id
        self.is_proxy_host = is_proxy_host
        self.memory_size_bytes = memory_size_bytes
        self.name = name
        self.networking_info = networking_info
        self.num_processors = num_processors
        self.os_name = os_name
        self.mtype = mtype
        self.vcs_version = vcs_version
        self.volumes = volumes
        self.vsswriters = vsswriters


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
        agents = None
        if dictionary.get('agents') != None:
            agents = list()
            for structure in dictionary.get('agents'):
                agents.append(cohesity_management_sdk.models.agent_information.AgentInformation.from_dictionary(structure))
        host_name = dictionary.get('hostName')
        host_type = dictionary.get('hostType')
        is_proxy_host = dictionary.get('isProxyHost')
        id = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('id')) if dictionary.get('id') else None
        memory_size_bytes = dictionary.get('memorySizeBytes')
        name = dictionary.get('name')
        networking_info = cohesity_management_sdk.models.networking_information.NetworkingInformation.from_dictionary(dictionary.get('networkingInfo')) if dictionary.get('networkingInfo') else None
        num_processors = dictionary.get('numProcessors')
        os_name = dictionary.get('osName')
        mtype = dictionary.get('type')
        vcs_version = dictionary.get('vcsVersion')
        volumes = None
        if dictionary.get('volumes') != None:
            volumes = list()
            for structure in dictionary.get('volumes'):
                volumes.append(cohesity_management_sdk.models.physical_volume.PhysicalVolume.from_dictionary(structure))
        vsswriters = None
        if dictionary.get('vsswriters') != None:
            vsswriters = list()
            for structure in dictionary.get('vsswriters'):
                vsswriters.append(cohesity_management_sdk.models.vss_writer.VssWriter.from_dictionary(structure))

        # Return an object of this model
        return cls(agents,
                   host_name,
                   host_type,
                   id,
                   is_proxy_host,
                   memory_size_bytes,
                   name,
                   networking_info,
                   num_processors,
                   os_name,
                   mtype,
                   vcs_version,
                   volumes,
                   vsswriters)


