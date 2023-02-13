# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GetAlertTypesParams(object):

    """Implementation of the 'GetAlertTypesParams' model.

    Specifies params to get alert types.

    Attributes:
        alert_category_list (list of AlertCategoryListEnum): Specifies a list
            of Alert Categories to filter alert types by. Specifies the
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
            related to Security. kAppsInfra - Alerts that are related to
            applications infra. kAntivirus - Alerts that are related to
            antivirus. kArchivalCopy - Alerts that are related to archival
            copies.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_category_list":'alertCategoryList'
    }

    def __init__(self,
                 alert_category_list=None):
        """Constructor for the GetAlertTypesParams class"""

        # Initialize members of the class
        self.alert_category_list = alert_category_list


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
        alert_category_list = dictionary.get('alertCategoryList')

        # Return an object of this model
        return cls(alert_category_list)


