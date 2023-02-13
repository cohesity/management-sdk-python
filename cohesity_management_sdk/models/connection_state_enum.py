# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ConnectionStateEnum(object):

    """Implementation of the 'ConnectionState' enum.

    Specifies the connection state of the Object and are only valid for
    ESXi hosts ('kHostSystem') or Virtual Machines ('kVirtualMachine').
    These enums are equivalent to the connection states documented in
    VMware's reference documentation.
    Examples of Cohesity connection states include 'kConnected',
    'kDisconnected', 'kInacccessible', etc.
    'kConnected' indicates that server has access to virtual machine.
    'kDisconnected' indicates that server is currently disconnected to
    virtual
    machine.
    'kInaccessible' indicates that one or more configuration files are
    inacccessible.
    'kInvalid' indicates that virtual machine configuration is invalid.
    'kOrphaned' indicates that virtual machine is no longer registered on the
    host it is associated with.
    'kNotResponding' indicates that virtual machine is failed to response
    due to external issues such as network connectivity, hostd not running
    etc.

    Attributes:
        KCONNECTED: TODO: type description here.
        KDISCONNECTED: TODO: type description here.
        KINACCESSIBLE: TODO: type description here.
        KINVALID: TODO: type description here.
        KORPHANED: TODO: type description here.
        KNOTRESPONDING: TODO: type description here.

    """

    KCONNECTED = 'kConnected'

    KDISCONNECTED = 'kDisconnected'

    KINACCESSIBLE = 'kInaccessible'

    KINVALID = 'kInvalid'

    KORPHANED = 'kOrphaned'

    KNOTRESPONDING = 'kNotResponding'

