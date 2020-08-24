# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class NetworkInterface(object):

    """Implementation of the 'NetworkInterface' model.

    Specifies the properties of a network interface.

    Attributes:
        bond_slave_slot_types (list of string): Specifies the types of the
            slots of any slaves if this interface is a bond.
        bond_slaves (list of string): Specifies the names of any slaves if
            this interface is a bond.
        bonding_mode (int): Specifies the bonding mode if this interface is
            a bond.
        gateway (string): Specifies the gateway of the interface.
        gateway6 (string): Specifies the gateway6 of the interface.
        group (string): Specifies the group that this interface belongs to.
        id (long|int): Specifies the ID of this network interface.
        is_connected (bool): Specifies whether or not the Interface is
            connected.
        is_default_route (bool): Specifies whether or not to use this
            interface as the default route.
        is_up (bool): Specifies whether or not the interface is currently
            up.
        mac_address (string): Specifies the Mac address of the Interface.
        mtu (int): Specifies the MTU of the interface.
        name (string): Specifies the name of the interface port.
        role (RoleNetworkInterfaceEnum): Specifies the role of this interface.
            'kPrimary' indicates a primary role. 'kSecondary' indicates a
            secondary role.
        services (list of ServiceNetworkInterfaceEnum): Specifies the types of
            services this interface is used for.
        speed (string): Specifies the speed of the Interface.
        static_ip (string): Specifies the static IP of the interface.
        static_ip6 (string): Specifies the static IPv6 of the interface.
        subnet (string): Specifies the subnet mask of the interface.
        subnet6 (string): Specifies the subnet6 mask of the interface.
        mtype (int): Specifies the type of interface.
        virtual_ip (string): Specifies the virtual IP of the interface.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bond_slave_slot_types":'bondSlaveSlotTypes',
        "bond_slaves":'bondSlaves',
        "bonding_mode":'bondingMode',
        "gateway":'gateway',
        "gateway6":'gateway6',
        "group":'group',
        "id":'id',
        "is_connected":'isConnected',
        "is_default_route":'isDefaultRoute',
        "is_up":'isUp',
        "mac_address":'macAddress',
        "mtu":'mtu',
        "name":'name',
        "role":'role',
        "services":'services',
        "speed":'speed',
        "static_ip":'staticIp',
        "static_ip6":'staticIp6',
        "subnet":'subnet',
        "subnet6":'subnet6',
        "mtype":'type',
        "virtual_ip":'virtualIp'
    }

    def __init__(self,
                 bond_slave_slot_types=None,
                 bond_slaves=None,
                 bonding_mode=None,
                 gateway=None,
                 gateway6=None,
                 group=None,
                 id=None,
                 is_connected=None,
                 is_default_route=None,
                 is_up=None,
                 mac_address=None,
                 mtu=None,
                 name=None,
                 role=None,
                 services=None,
                 speed=None,
                 static_ip=None,
                 static_ip6=None,
                 subnet=None,
                 subnet6=None,
                 mtype=None,
                 virtual_ip=None):
        """Constructor for the NetworkInterface class"""

        # Initialize members of the class
        self.bond_slave_slot_types = bond_slave_slot_types
        self.bond_slaves = bond_slaves
        self.bonding_mode = bonding_mode
        self.gateway = gateway
        self.gateway6 = gateway6
        self.group = group
        self.id = id
        self.is_connected = is_connected
        self.is_default_route = is_default_route
        self.is_up = is_up
        self.mac_address = mac_address
        self.mtu = mtu
        self.name = name
        self.role = role
        self.services = services
        self.speed = speed
        self.static_ip = static_ip
        self.static_ip6 = static_ip6
        self.subnet = subnet
        self.subnet6 = subnet6
        self.mtype = mtype
        self.virtual_ip = virtual_ip


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        bond_slave_slot_types = dictionary.get('bondSlaveSlotTypes')
        bond_slaves = dictionary.get('bondSlaves')
        bonding_mode = dictionary.get('bondingMode')
        gateway = dictionary.get('gateway')
        gateway6 = dictionary.get('gateway6')
        group = dictionary.get('group')
        id = dictionary.get('id')
        is_connected = dictionary.get('isConnected')
        is_default_route = dictionary.get('isDefaultRoute')
        is_up = dictionary.get('isUp')
        mac_address = dictionary.get('macAddress')
        mtu = dictionary.get('mtu')
        name = dictionary.get('name')
        role = dictionary.get('role')
        services = dictionary.get('services')
        speed = dictionary.get('speed')
        static_ip = dictionary.get('staticIp')
        static_ip6 = dictionary.get('staticIp6')
        subnet = dictionary.get('subnet')
        subnet6 = dictionary.get('subnet6')
        mtype = dictionary.get('type')
        virtual_ip = dictionary.get('virtualIp')

        # Return an object of this model
        return cls(bond_slave_slot_types,
                   bond_slaves,
                   bonding_mode,
                   gateway,
                   gateway6,
                   group,
                   id,
                   is_connected,
                   is_default_route,
                   is_up,
                   mac_address,
                   mtu,
                   name,
                   role,
                   services,
                   speed,
                   static_ip,
                   static_ip6,
                   subnet,
                   subnet6,
                   mtype,
                   virtual_ip)


