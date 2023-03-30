# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OverwritePolicyEnum(object):

    """Implementation of the 'OverwritePolicy' enum.
    Overwrite Policy specifies a policy to be used while recovering existing
    databases. Specifies the policy to be used while recovering existing
    databases. 'kFailIfExists' refers to a policy to fail if DB exists already.
    'kOverwrite' refres to the policy to overwrite existing DB.


    Attributes:
        KFAILIFEXISTS: TODO: type description here.
        KOVERWRITE: TODO: type description here.

    """

    KFAILIFEXISTS = 'kFailIfExists'

    KOVERWRITE = 'kOverwrite'
