# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GcpTagTypeEnum(object):

    """Implementation of the 'GcpTagType' enum.
    Specifies the tag attribute type of GCP. Going forward, there will be an
    additional TagTypes for AWS as well. Specifies the type of the tag GCP
    entity refers to. 'kNetworkTag' indicates a network tag present on
    instances. 'kLabel' indicates a label (key-value pair) present on
    instances. 'kCustomMetadata' indicates custom Metadata (key-value pair)
    present on instances.


    Attributes:
        KNETWORKTAG: TODO: type description here.
        KLABEL: TODO: type description here.
        KCUSTOMMETADATA: TODO: type description here.

    """

    KNETWORKTAG = 'kNetworkTag'

    KLABEL = 'kLabel'

    KCUSTOMMETADATA = 'kCustomMetadata'
