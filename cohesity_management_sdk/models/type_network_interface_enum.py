# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class TypeNetworkInterfaceEnum(object):

    """Implementation of the 'Type_NetworkInterface' enum.

    Specifies the type of interface.
    'kPhysicalInterface' indicates a physical interface type.
    'kBondMasterInterface' indicates that the interface is the master of a
    bond.
    'kBondSlaveInterface' indicates the the interface is a slave of a bond.
    'kTaggedVlanInterface' indicates a tagged vlan interface type.

    Attributes:
        KPHYSICALINTERFACE: TODO: type description here.
        KBONDMASTERINTERFACE: TODO: type description here.
        KBONDSLAVEINTERFACE: TODO: type description here.
        KTAGGEDVLANINTERFACE: TODO: type description here.

    """

    KPHYSICALINTERFACE = 'kPhysicalInterface'

    KBONDMASTERINTERFACE = 'kBondMasterInterface'

    KBONDSLAVEINTERFACE = 'kBondSlaveInterface'

    KTAGGEDVLANINTERFACE = 'kTaggedVlanInterface'

