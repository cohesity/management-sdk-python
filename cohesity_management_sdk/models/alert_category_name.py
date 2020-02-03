# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class AlertCategoryName(object):

    """Implementation of the 'AlertCategoryName' model.

    AlertCategoryName returns alert category and its public facing string.

    Attributes:
        category (CategoryEnum): Specifies alert category. Specifies the
            category of an Alert. kDisk - Alerts that are related to Disk.
            kNode - Alerts that are related to Node. kCluster - Alerts that
            are related to Cluster. kNodeHealth - Alerts that are related to
            Node Health. kClusterHealth - Alerts that are related to Cluster
            Health. kBackupRestore - Alerts that are related to
            Backup/Restore. kEncryption - Alerts that are related to
            Encryption. kArchivalRestore - Alerts that are related to
            Archival/Restore. kRemoteReplication - Alerts that are related to
            Remote Replication. kQuota - Alerts that are related to Quota.
            kLicense - Alerts that are related to License.
            kHeliosProActiveWellness - Alerts that are related to Helios
            ProActive Wellness. kHeliosAnalyticsJobs - Alerts that are related
            to Helios Analytics Jobs. kHeliosSignatureJobs - Alerts that are
            related to Helios Signature Jobs. kSecurity - Alerts that are
            related to Security.
        name (string): Specifies public facing string for alert enums.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "category":'category',
        "name":'name'
    }

    def __init__(self,
                 category=None,
                 name=None):
        """Constructor for the AlertCategoryName class"""

        # Initialize members of the class
        self.category = category
        self.name = name


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
        category = dictionary.get('category')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(category,
                   name)


