# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RequiredPrivilegesEnum(object):

    """Implementation of the 'RequiredPrivileges' enum.

    Specifies privileges that are required for this app.
    App privilege information.

    Specifies privileges that are required for this app.
    kReadAccess - App needs views for read access.
    kReadWriteAccess - App needs views for Read/write access.
    kManagementAccess - App needs management access via iris API.
    kAutoMountAccess - Whether to allow auto-mounting all the views.
    kUnrestrictedAppUIAccess - Whether app requires unrestricted UI access
    (i.e. without passing app access token in URL).
    kAuditLogViewReadAccess - Whether app requires read access to the internal
    audit log view.
    kProtectedObjectAccess - Whether app requires read access to protected
    objects.

    Attributes:
        KREADACCESS: TODO: type description here.
        KREADWRITEACCESS: TODO: type description here.
        KMANAGEMENTACCESS: TODO: type description here.
        KAUTOMOUNTACCESS: TODO: type description here.
        KUNRESTRICTEDAPPUIACCESS: TODO: type description here.
        KAUDITLOGVIEWREADACCESS: TODO: type description here.
        KPROTECTEDOBJECTACCESS: TODO: type description here.

    """

    KREADACCESS = 'kReadAccess'

    KREADWRITEACCESS = 'kReadWriteAccess'

    KMANAGEMENTACCESS = 'kManagementAccess'

    KAUTOMOUNTACCESS = 'kAutoMountAccess'

    KUNRESTRICTEDAPPUIACCESS = 'kUnrestrictedAppUIAccess'

    KAUDITLOGVIEWREADACCESS = 'kAuditLogViewReadAccess'

    KPROTECTEDOBJECTACCESS = 'kProtectedObjectAccess'

