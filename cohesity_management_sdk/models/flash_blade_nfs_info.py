# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FlashBladeNfsInfo(object):

    """Implementation of the 'FlashBladeNfsInfo' model.

    Specifies information specific to NFS protocol exposed by Pure Flash
    Blade
    file system.

    Attributes:
        export_rules (string): Specifies NFS protocol export rules. Rules are
            in the form host(options). host represents one of the following
            categories:  IP address in the form ddd.ddd.ddd.ddd for IPv4, or
            xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx for IPv6.  Netmask in the
            form ddd.ddd.ddd.ddd/dd for IPv4, or
            xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx for IPv6.  Wildcard in
            the form * to represent all clients  options in parenthesis
            represents a comma-separated list of NFS export options. Valid
            export options are rw, ro, root_squash, no_root_squash, and
            fileid_32bit.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "export_rules":'exportRules'
    }

    def __init__(self,
                 export_rules=None):
        """Constructor for the FlashBladeNfsInfo class"""

        # Initialize members of the class
        self.export_rules = export_rules


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
        export_rules = dictionary.get('exportRules')

        # Return an object of this model
        return cls(export_rules)


