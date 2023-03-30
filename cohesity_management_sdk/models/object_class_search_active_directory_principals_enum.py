# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectClassSearchActiveDirectoryPrincipalsEnum(object):

    """Implementation of the 'objectClass_SearchActiveDirectoryPrincipals' enum.

    Optionally filter by a principal object class such as 'kGroup' or 'kUser'.
    If 'kGroup' is specified, only group principals are returned.
    If 'kUser' is specified, only user principals are returned.
    If not specified, both group and user principals are returned.
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

