# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectClassEnum(object):

    """Implementation of the 'ObjectClass' enum.

    Specifies the object class of the principal (either 'kGroup' or 'kUser').
    'kUser' specifies a user object class.
    'kGroup' specifies a group object class.
    'kComputer' specifies a computer object class.
    'kWellKnownPrincipal' specifies a well known principal.
    'kServiceAccount' specifies a service account object class.

    Attributes:
        KUSER: TODO: type description here.
        KGROUP: TODO: type description here.
        KCOMPUTER: TODO: type description here.
        KWELLKNOWNPRINCIPAL: TODO: type description here.
        KSERVICEACCOUNT: TODO: type description here.

    """

    KUSER = 'kUser'

    KGROUP = 'kGroup'

    KCOMPUTER = 'kComputer'

    KWELLKNOWNPRINCIPAL = 'kWellKnownPrincipal'

    KSERVICEACCOUNT = 'kServiceAccount'

