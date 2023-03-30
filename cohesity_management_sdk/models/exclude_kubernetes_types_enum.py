# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ExcludeKubernetesTypesEnum(object):

    """Implementation of the 'ExcludeKubernetesTypes' enum.

    Specifies the Object types to be filtered out for Kubernetes that match
    the passed in types such as 'kService'.
    For example, set this parameter to 'kService' to exclude services
    from being returned.

    Attributes:
        KSERVICE: TODO: type description here.

    """

    KSERVICE = 'kService'

