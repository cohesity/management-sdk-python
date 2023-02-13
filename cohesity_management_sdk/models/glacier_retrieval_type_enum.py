# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GlacierRetrievalTypeEnum(object):

    """Implementation of the 'GlacierRetrievalType' enum.

    Specifies the way data needs to be retrieved from the external target.
    This information will be filled in by Iris and Magneto will pass it along
    to the Icebox as it is to support bulk retrieval from Glacier.
    Specifies the type of Restore Task.

    'kStandard' specifies retrievals that allow to access any of your
    archives
    within several hours. Standard retrievals typically complete within 3–5
    hours. This is the default option for retrieval requests that do not
    specify
    the retrieval option.
    'kBulk' specifies retrievals that are Glacier’s lowest-cost retrieval
    option, which can be used to retrieve large amounts, even petabytes, of
    data
    inexpensively in a day. Bulk retrieval typically complete within 5–12
    hours.
    'kExpedited' specifies retrievals that allows to quickly access your data
    when occasional urgent requests for a subset of archives are required.
    For
    all but the largest archives (250 MB+), data accessed using Expedited
    retrievals are typically made available within 1–5 minutes.

    Attributes:
        KSTANDARD: TODO: type description here.
        KBULK: TODO: type description here.
        KEXPEDITED: TODO: type description here.

    """

    KSTANDARD = 'kStandard'

    KBULK = 'kBulk'

    KEXPEDITED = 'kExpedited'

