# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NasProtectionSource(object):

    """Implementation of the 'NasProtectionSource' model.

    Specifies a Protection Source in a Generic NAS environment.

    Attributes:
        description (string): Specifies a description about the Protection
            Source.
        mount_path (string): Specifies the mount path of this NAS. For
            example, for a NFS mount point, this should be in the format of IP
            or hostname:/foo/bar.
        name (string): Specifies the name of the NetApp Object.
        protocol (ProtocolNasProtectionSourceEnum): Specifies the protocol
            used by the NAS server. Specifies the protocol used by a NAS
            server. 'kNfs3' indicates NFS v3 protocol. 'kCifs1' indicates CIFS
            v1.0 protocol.
        skip_validation (bool): Specifies whether to skip validation of the
            given mount point.
        mtype (TypeNasProtectionSourceEnum): Specifies the type of a
            Protection Source Object in a generic NAS Source such as 'kGroup',
            or 'kHost'. Specifies the kind of NAS mount. 'kGroup' indicates
            top level node that holds individual NAS hosts. 'kHost' indicates
            a single NAS path that can be mounted. 'kDfsGroup' indicates a DFS
            group containing top level directories mapped to different
            servers. 'kDfsTopDir' indicates a top level directory inside a DFS
            group, discovered when registering a DFS group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "mount_path":'mountPath',
        "name":'name',
        "protocol":'protocol',
        "skip_validation":'skipValidation',
        "mtype":'type'
    }

    def __init__(self,
                 description=None,
                 mount_path=None,
                 name=None,
                 protocol=None,
                 skip_validation=None,
                 mtype=None):
        """Constructor for the NasProtectionSource class"""

        # Initialize members of the class
        self.description = description
        self.mount_path = mount_path
        self.name = name
        self.protocol = protocol
        self.skip_validation = skip_validation
        self.mtype = mtype


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
        description = dictionary.get('description')
        mount_path = dictionary.get('mountPath')
        name = dictionary.get('name')
        protocol = dictionary.get('protocol')
        skip_validation = dictionary.get('skipValidation')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(description,
                   mount_path,
                   name,
                   protocol,
                   skip_validation,
                   mtype)


