# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeMongoDBProtectionSourceEnum(object):

    """Implementation of the 'Type_MongoDBProtectionSource' enum.

    Specifies the type of the
    managed Object in MongoDB Protection Source.
    Specifies the type of an MongoDB source entity.
    'kCluster' indicates a mongodb cluster distributed over several
    physical nodes.
    'kDatabase' indicates a Database within the MongoDB environment.
    'kCollection' indicates a Collection in the MongoDB enironment.

    Attributes:
        KCLUSTER: TODO: type description here.
        KDATABASE: TODO: type description here.
        KCOLLECTION: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KDATABASE = 'kDatabase'

    KCOLLECTION = 'kCollection'

