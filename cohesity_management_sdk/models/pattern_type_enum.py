# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PatternTypeEnum(object):

    """Implementation of the 'PatternType' enum.
    Specifies the Pattern type. 'REGULAR' indicates that the pattern contains a
    regular expression. 'TEMPLATE' indicates that the pattern has a pre defined
    input pattern such as date of the form 'DD-MM-YYYY'.


    Attributes:
        REGULAR: TODO: type description here.
        TEMPLATE: TODO: type description here.

    """

    REGULAR = 'REGULAR'

    TEMPLATE = 'TEMPLATE'
