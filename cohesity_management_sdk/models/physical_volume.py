# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class PhysicalVolume(object):

    """Implementation of the 'PhysicalVolume' model.

    Specifies volume information about a Physical Protection Source.

    Attributes:
        device_path (string): Specifies the path to the device that hosts the
            volume locally.
        guid (string): Specifies an id for the Physical Volume.
        is_extended_attributes_supported (bool): Specifies whether this volume
            supports extended attributes (like ACLs) when performing file
            backups.
        is_protected (bool): Specifies if a volume is protected by a Job.
        label (string): Specifies a volume label that can be used for
            displaying additional identifying information about a volume.
        logical_size_bytes (int): Specifies the logical size of the volume in
            bytes that is not reduced by change-block tracking, compression
            and deduplication.
        mount_points (list of string): Array of Mount Points.  Specifies the
            mount points where the volume is mounted, for example: 'C:\',
            '/mnt/foo' etc.
        network_path (string): Specifies the full path to connect to the
            network attached volume. For example, (IP or
            hostname):/path/to/share for NFS volumes).
        used_size_bytes (int): Specifies the size used by the volume in
            bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_path":'devicePath',
        "guid":'guid',
        "is_extended_attributes_supported":'isExtendedAttributesSupported',
        "is_protected":'isProtected',
        "label":'label',
        "logical_size_bytes":'logicalSizeBytes',
        "mount_points":'mountPoints',
        "network_path":'networkPath',
        "used_size_bytes":'usedSizeBytes'
    }

    def __init__(self,
                 device_path=None,
                 guid=None,
                 is_extended_attributes_supported=None,
                 is_protected=None,
                 label=None,
                 logical_size_bytes=None,
                 mount_points=None,
                 network_path=None,
                 used_size_bytes=None):
        """Constructor for the PhysicalVolume class"""

        # Initialize members of the class
        self.device_path = device_path
        self.guid = guid
        self.is_extended_attributes_supported = is_extended_attributes_supported
        self.is_protected = is_protected
        self.label = label
        self.logical_size_bytes = logical_size_bytes
        self.mount_points = mount_points
        self.network_path = network_path
        self.used_size_bytes = used_size_bytes


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
        device_path = dictionary.get('devicePath')
        guid = dictionary.get('guid')
        is_extended_attributes_supported = dictionary.get('isExtendedAttributesSupported')
        is_protected = dictionary.get('isProtected')
        label = dictionary.get('label')
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        mount_points = dictionary.get('mountPoints')
        network_path = dictionary.get('networkPath')
        used_size_bytes = dictionary.get('usedSizeBytes')

        # Return an object of this model
        return cls(device_path,
                   guid,
                   is_extended_attributes_supported,
                   is_protected,
                   label,
                   logical_size_bytes,
                   mount_points,
                   network_path,
                   used_size_bytes)


