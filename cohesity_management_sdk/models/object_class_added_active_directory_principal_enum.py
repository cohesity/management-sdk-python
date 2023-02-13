# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectClassAddedActiveDirectoryPrincipalEnum(object):

    """Implementation of the 'ObjectClass_AddedActiveDirectoryPrincipal' enum.

    Specifies the type of the referenced Active Directory principal.
    If 'kGroup', the referenced Active Directory principal is a group.
    If 'kUser', the referenced Active Directory principal is a user.
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

