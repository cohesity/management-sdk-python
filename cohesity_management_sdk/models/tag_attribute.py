# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TagAttribute(object):

    """Implementation of the 'TagAttribute' model.

    Specifies a VMware tag.

    Attributes:
        gcp_tag_type (GcpTagTypeEnum): Specifies the tag attribute type of
            GCP.
            Going forward, there will be an additional TagTypes for AWS as
            well.
            Specifies the type of the tag GCP entity refers to.
            'kNetworkTag' indicates a network tag present on instances.
            'kLabel' indicates a label (key-value pair) present on instances.
            'kCustomMetadata' indicates custom Metadata (key-value pair)
            present on instances.
        id (long|int): Specifies the Coheisty id of the VM tag.
        name (string): Specifies the VMware name of the VM tag.
        uuid (string): Specifies the VMware Universally Unique Identifier
            (UUID) of the VM tag.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gcp_tag_type":'gcpTagType',
        "id":'id',
        "name":'name',
        "uuid":'uuid'
    }

    def __init__(self,
                 gcp_tag_type=None,
                 id=None,
                 name=None,
                 uuid=None):
        """Constructor for the TagAttribute class"""

        # Initialize members of the class
        self.gcp_tag_type = gcp_tag_type
        self.id = id
        self.name = name
        self.uuid = uuid


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
        gcp_tag_type = dictionary.get('gcpTagType', None)
        id = dictionary.get('id')
        name = dictionary.get('name')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(gcp_tag_type,
                   id,
                   name,
                   uuid)


