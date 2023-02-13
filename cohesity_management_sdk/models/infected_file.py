# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class InfectedFile(object):

    """Implementation of the 'InfectedFile' model.

    Specifies the Result parameters for all infected files.

    Attributes:
        antivirus_provider_name (string): Specifies the name of antivirus
            service provider.
        entity_id (long|int): Specifies the entity id of the infected file.
        file_path (string): Specifies file path of the infected file.
        infection_detection_timestamp (long|int): Specifies unix epoch
            timestamp (in microseconds) at which these threats were detected.
        modified_timestamp_usecs (long|int): Specifies unix epoch timestamp
            (in microseconds) at which this file is modified.
        remediation_state (RemediationStateEnum): Specifies the remediation
            state of the file. Remediation State. 'kQuarantine' indicates
            'Quarantine' state of the file. This state blocks the client
            access. The administrator will have to manually delete, rescan or
            unquarantine the file. 'kUnquarantine' indicates 'Unquarantine'
            state of the file. The administrator has manually moved files from
            quarantined to the unquarantined state to allow client access.
            Unquarantined files are not scanned for virus until manually
            reset.
        root_inode_id (long|int): Specifies the root inode id of the file
            system that infected file belongs to.
        scan_timestamp_usecs (long|int): Specifies unix epoch timestamp (in
            microseconds) at which inode was scanned for viruses.
        service_icap_uri (string): Specifies the instance of an antivirus ICAP
            server in the cluster config that detected these threats.
        threat_descriptions (list of string): Specifies the list of virus
            threat descriptions found in the file.
        view_id (long|int): Specifies the id of the View the infected file
            belongs to.
        view_name (string): Specifies the View name corresponding to above
            view id.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "antivirus_provider_name":'antivirusProviderName',
        "entity_id":'entityId',
        "file_path":'filePath',
        "infection_detection_timestamp":'infectionDetectionTimestamp',
        "modified_timestamp_usecs":'modifiedTimestampUsecs',
        "remediation_state":'remediationState',
        "root_inode_id":'rootInodeId',
        "scan_timestamp_usecs":'scanTimestampUsecs',
        "service_icap_uri":'serviceIcapUri',
        "threat_descriptions":'threatDescriptions',
        "view_id":'viewId',
        "view_name":'viewName'
    }

    def __init__(self,
                 antivirus_provider_name=None,
                 entity_id=None,
                 file_path=None,
                 infection_detection_timestamp=None,
                 modified_timestamp_usecs=None,
                 remediation_state=None,
                 root_inode_id=None,
                 scan_timestamp_usecs=None,
                 service_icap_uri=None,
                 threat_descriptions=None,
                 view_id=None,
                 view_name=None):
        """Constructor for the InfectedFile class"""

        # Initialize members of the class
        self.antivirus_provider_name = antivirus_provider_name
        self.entity_id = entity_id
        self.file_path = file_path
        self.infection_detection_timestamp = infection_detection_timestamp
        self.modified_timestamp_usecs = modified_timestamp_usecs
        self.remediation_state = remediation_state
        self.root_inode_id = root_inode_id
        self.scan_timestamp_usecs = scan_timestamp_usecs
        self.service_icap_uri = service_icap_uri
        self.threat_descriptions = threat_descriptions
        self.view_id = view_id
        self.view_name = view_name


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
        antivirus_provider_name = dictionary.get('antivirusProviderName')
        entity_id = dictionary.get('entityId')
        file_path = dictionary.get('filePath')
        infection_detection_timestamp = dictionary.get('infectionDetectionTimestamp')
        modified_timestamp_usecs = dictionary.get('modifiedTimestampUsecs')
        remediation_state = dictionary.get('remediationState')
        root_inode_id = dictionary.get('rootInodeId')
        scan_timestamp_usecs = dictionary.get('scanTimestampUsecs')
        service_icap_uri = dictionary.get('serviceIcapUri')
        threat_descriptions = dictionary.get('threatDescriptions')
        view_id = dictionary.get('viewId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(antivirus_provider_name,
                   entity_id,
                   file_path,
                   infection_detection_timestamp,
                   modified_timestamp_usecs,
                   remediation_state,
                   root_inode_id,
                   scan_timestamp_usecs,
                   service_icap_uri,
                   threat_descriptions,
                   view_id,
                   view_name)


