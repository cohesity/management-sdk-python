# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RegisteringAppEnum(object):

    """Implementation of the 'RegisteringApp' enum.

    Application being registered.
    This param is used to indicate the app for which the job is created.
    'oracle' indicates that the job was created for oracle app.
    'msSql' indicates that the job was created for msSql app.
    'physical' indicates that the job was created for physical machine.

    Attributes:
        ORACLE: TODO: type description here.
        MSSQL: TODO: type description here.
        PHYSICAL: TODO: type description here.

    """

    ORACLE = 'oracle'

    MSSQL = 'msSql'

    PHYSICAL = 'physical'

