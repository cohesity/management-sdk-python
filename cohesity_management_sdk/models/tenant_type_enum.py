# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TenantTypeEnum(object):

    """Implementation of the 'TenantType' enum.

    Specifies the MCM tenant type.
    'Dmaas' implies tenant type is DMaaS.
    'OnPrem' implies tenant is cluster tenant.

    Attributes:

        DMAAS: TODO: type description here.
        ONPREM: TODO: type description here.

    """

    DMAAS = 'Dmaas'

    ONPREM = 'OnPrem'

