# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CompressionPolicyEnum(object):

    """Implementation of the 'CompressionPolicy' enum.

    Specifies the compression setting to be applied to a Storage Domain
    (View Box).
    'kCompressionNone' indicates that data is not compressed.
    'kCompressionLow' indicates that data is compressed using LZ4 or Snappy.
    'kCompressionHigh' indicates that data is compressed in Gzip.

    Attributes:
        KCOMPRESSIONNONE: TODO: type description here.
        KCOMPRESSIONLOW: TODO: type description here.
        KCOMPRESSIONHIGH: TODO: type description here.

    """

    KCOMPRESSIONNONE = 'kCompressionNone'

    KCOMPRESSIONLOW = 'kCompressionLow'

    KCOMPRESSIONHIGH = 'kCompressionHigh'

