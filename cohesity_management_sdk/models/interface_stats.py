# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class InterfaceStats(object):

    """Implementation of the 'InterfaceStats' model.

    Attributes:
        rx_bytes (long|int): TODO: Type description here.
        rx_dropped (long|int): TODO: Type description here.
        rx_errors (long|int): TODO: Type description here.
        rx_pkts (long|int): Receive counters.
        tx_bytes (long|int): TODO: Type description here.
        tx_dropped (long|int): TODO: Type description here.
        tx_errors (long|int): TODO: Type description here.
        tx_pkts (long|int): Transmit counters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rx_bytes": 'rxBytes',
        "rx_dropped": 'rxDropped',
        "rx_errors": 'rxErrors',
        "rx_pkts":'rxPkts',
        "tx_bytes":'txBytes',
        "tx_dropped":'txDropped',
        "tx_errors":'txErrors',
        "tx_pkts":'txPkts'
    }

    def __init__(self,
                 rx_bytes=None,
                 rx_dropped=None,
                 rx_errors=None,
                 rx_pkts=None,
                 tx_bytes=None,
                 tx_dropped=None,
                 tx_errors=None,
                 tx_pkts=None
                 ):
        """Constructor for the InterfaceStats class"""

        # Initialize members of the class
        self.rx_bytes = rx_bytes
        self.rx_dropped = rx_dropped
        self.rx_errors = rx_errors
        self.rx_pkts = rx_pkts
        self.tx_bytes = tx_bytes
        self.tx_dropped = tx_dropped
        self.tx_errors = tx_errors
        self.tx_pkts = tx_pkts

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
        rx_bytes = dictionary.get('rxBytes')
        rx_dropped = dictionary.get('rxDropped')
        rx_errors = dictionary.get('rxErrors')
        rx_pkts = dictionary.get('rxPkts')
        tx_bytes = dictionary.get('txBytes')
        tx_dropped = dictionary.get('txDropped')
        tx_errors = dictionary.get('txErrors')
        tx_pkts = dictionary.get('txPkts')

        # Return an object of this model
        return cls(rx_bytes,
                   rx_dropped,
                   rx_errors,
                   rx_pkts,
                   tx_bytes,
                   tx_dropped,
                   tx_errors,
                   tx_pkts)


