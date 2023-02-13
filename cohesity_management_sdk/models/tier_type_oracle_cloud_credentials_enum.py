# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TierTypeOracleCloudCredentialsEnum(object):

    """Implementation of the 'TierType_OracleCloudCredentials' enum.

    Specifies the storage class of Oracle vault.
    OracleTierType specifies the storage class for Oracle.
    'kOracleTierStandard' indicates a tier type of Oracle properties that
    requires fast, immediate and frequent access.
    'kOracleTierArchive' indicates a tier type of Oracle properties that is
    rarely accesed and preserved for long times.

    Attributes:
        KORACLETIERSTANDARD: TODO: type description here.
        KORACLETIERARCHIVE: TODO: type description here.

    """

    KORACLETIERSTANDARD = 'kOracleTierStandard'

    KORACLETIERARCHIVE = 'kOracleTierArchive'

