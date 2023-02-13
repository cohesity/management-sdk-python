# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_object_details
import cohesity_management_sdk.models.cloud_deploy_target_details

class DeployTaskRequest(object):

    """Implementation of the 'DeployTaskRequest' model.

    Specifies the settings for a Deploy Task that deploys VMs on cloud.

    Attributes:
        name (string): Specifies the name of the Deploy Task. This field must
            be set and must be a unique name.
        new_parent_id (long|int): Specifies a new registered parent Protection
            Source. If specified the selected objects are cloned or recovered
            to this new Protection Source. If not specified, objects are
            cloned or recovered to the original Protection Source that was
            managing them.
        objects (list of RestoreObjectDetails): Array of Objects.  Specifies a
            list of Protection Source objects or Protection Job objects (with
            specified Protection Source objects).
        target (CloudDeployTargetDetails): Message that specifies the details
            about CloudDeploy target where backup snapshots may be converted
            and stored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "new_parent_id":'newParentId',
        "objects":'objects',
        "target":'target'
    }

    def __init__(self,
                 name=None,
                 new_parent_id=None,
                 objects=None,
                 target=None):
        """Constructor for the DeployTaskRequest class"""

        # Initialize members of the class
        self.name = name
        self.new_parent_id = new_parent_id
        self.objects = objects
        self.target = target


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
        name = dictionary.get('name')
        new_parent_id = dictionary.get('newParentId')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(structure))
        target = cohesity_management_sdk.models.cloud_deploy_target_details.CloudDeployTargetDetails.from_dictionary(dictionary.get('target')) if dictionary.get('target') else None

        # Return an object of this model
        return cls(name,
                   new_parent_id,
                   objects,
                   target)


