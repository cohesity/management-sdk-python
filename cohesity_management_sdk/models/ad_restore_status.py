# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_object_restore_status
import cohesity_management_sdk.models.compare_ad_objects_result_ad_object


class ADRestoreStatus(object):

    """Implementation of the 'ADRestoreStatus' model.

    Represents AD restore status for object/attribute recovery. Each
    ADRestoreStatus entry will contain object_info: information about the
    object getting restored and status: status of the restore operation.
    object_info is used to generate the audit information of the AD restore
    operations.


    Attributes:

        object_info (CompareADObjectsResult_ADObject): The audit information
            about the AD object which was being recovered. This field will
            contain values like name,objectGUID,DN,objectClass and this
            information is used by the UI to show the audit information.
        status (ADObjectRestoreStatus): Status object for AD objects/attributes
            for which the restores were done. This is an echo of the restore
            status sent by the agent for restore RPC call.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "object_info":'objectInfo',
        "status":'status',
    }
    def __init__(self,
                 object_info=None,
                 status=None,
            ):

        """Constructor for the ADRestoreStatus class"""

        # Initialize members of the class
        self.object_info = object_info
        self.status = status

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
        object_info = cohesity_management_sdk.models.compare_ad_objects_result_ad_object.CompareADObjectsResult_ADObject.from_dictionary(dictionary.get('objectInfo')) if dictionary.get('objectInfo') else None
        status = cohesity_management_sdk.models.ad_object_restore_status.ADObjectRestoreStatus.from_dictionary(dictionary.get('status')) if dictionary.get('status') else None

        # Return an object of this model
        return cls(
            object_info,
            status
)