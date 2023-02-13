# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class InstallStateEnum(object):

    """Implementation of the 'InstallState' enum.

    Specifies app installation status.
    Specifies status of the app installation.
    kNotInstalled - App yet to be installed.
    kInstallInProgress - App installation is in progress.
    kInstalled - App is installed successfully and can be launched.
    kInstallFailed - App installation failed.
    kUninstallInProgress - App uninstallation is in progress.
    kUninstallFailed - App uninstallation failed.
    kDownloadNotStarted - App download has not started.
    kDownloadInProgress - App download in progress.
    kDownloadComplete - App download completed.
    kDownloadFailed - App download failed.

    Attributes:
        KNOTINSTALLED: TODO: type description here.
        KINSTALLINPROGRESS: TODO: type description here.
        KINSTALLED: TODO: type description here.
        KINSTALLFAILED: TODO: type description here.
        KUNINSTALLINPROGRESS: TODO: type description here.
        KUNINSTALLFAILED: TODO: type description here.
        KDOWNLOADNOTSTARTED: TODO: type description here.
        KDOWNLOADINPROGRESS: TODO: type description here.
        KDOWNLOADCOMPLETE: TODO: type description here.
        KDOWNLOADFAILED: TODO: type description here.
        
    """

    KNOTINSTALLED = 'kNotInstalled'

    KINSTALLINPROGRESS = 'kInstallInProgress'

    KINSTALLED = 'kInstalled'

    KINSTALLFAILED = 'kInstallFailed'

    KUNINSTALLINPROGRESS = 'kUninstallInProgress'

    KUNINSTALLFAILED = 'kUninstallFailed'

    KDOWNLOADNOTSTARTED = 'kDownloadNotStarted'

    KDOWNLOADINPROGRESS = 'kDownloadInProgress'

    KDOWNLOADCOMPLETE = 'kDownloadComplete'

    KDOWNLOADFAILED = 'kDownloadFailed'

