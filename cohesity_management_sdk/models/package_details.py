# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PackageDetails(object):

    """Implementation of the 'PackageDetails' model.

    Specifies all of the details of a package that is currently installed
    on the cluster.

    Attributes:
        downtime_required (bool): Specifies whether or not downtime is
            required to update to this package.
        installed_on_nodes (list of long|int): Specifies the list of IDs of
            nodes on the cluster where this package is currently installed.
        package_name (string): Specifies the name of the current package.
        release_date (string): Specifies the release date of this package.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "downtime_required":'downtimeRequired',
        "installed_on_nodes":'installedOnNodes',
        "package_name":'packageName',
        "release_date":'releaseDate'
    }

    def __init__(self,
                 downtime_required=None,
                 installed_on_nodes=None,
                 package_name=None,
                 release_date=None):
        """Constructor for the PackageDetails class"""

        # Initialize members of the class
        self.downtime_required = downtime_required
        self.installed_on_nodes = installed_on_nodes
        self.package_name = package_name
        self.release_date = release_date


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
        downtime_required = dictionary.get('downtimeRequired')
        installed_on_nodes = dictionary.get('installedOnNodes')
        package_name = dictionary.get('packageName')
        release_date = dictionary.get('releaseDate')

        # Return an object of this model
        return cls(downtime_required,
                   installed_on_nodes,
                   package_name,
                   release_date)


