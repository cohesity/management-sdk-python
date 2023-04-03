# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity
import cohesity_management_sdk.models.k_8_s_filter_params_label_vec


class K8SFilterParams(object):

    """Implementation of the 'K8SFilterParams' model.

    Message defining the different criteria to filter objects, such as
    persistent volumes from backup for include or exclude. This is used to
    specify both object-level (BackupSourceParams) and job-level
    (EnvBackupParams) in/exclusion criteria.  If a criterion is specified at
    both object-level and job-level, then job-level setting will be ignored.


    Attributes:

        entity_vec (list of Entity): List of entities included in filter. This
            contains the list of entities corresponding to entity IDs in
            'object_id_vec' and the list of entities under the union of
            intersection of labels specified by 'label_vec_vec'. This will be
            populated during backup run.
        label_vec_vec (list of K8SFilterParams_LabelVec): Array of Arrays of
            Label Ids that Specify Persistent Volumes (PV) and Persistent
            Volume Claims (PVC) to include in filter. The outer array
            represents a union operation (i.e.: match any label rule), while
            the inner array represents an intersection operation (i.e.: match
            all label rules). See
            iris/apiSpecs/v2/common/adapters/kubernetes/jobs.yaml:filterLabelIds
            for full description.
        object_id_vec (list of long|int): IDs of objects to be included in
            filter.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "entity_vec":'entityVec',
        "label_vec_vec":'labelVecVec',
        "object_id_vec":'objectIdVec',
    }
    def __init__(self,
                 entity_vec=None,
                 label_vec_vec=None,
                 object_id_vec=None,
            ):

        """Constructor for the K8SFilterParams class"""

        # Initialize members of the class
        self.entity_vec = entity_vec
        self.label_vec_vec = label_vec_vec
        self.object_id_vec = object_id_vec

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
        entity_vec = None
        if dictionary.get('entityVec') != None:
            entity_vec = list()
            for structure in dictionary.get('entityVec'):
                entity_vec.append(cohesity_management_sdk.models.entity.Entity.from_dictionary(structure))
        label_vec_vec = None
        if dictionary.get('labelVecVec') != None:
            label_vec_vec = list()
            for structure in dictionary.get('labelVecVec'):
                label_vec_vec.append(cohesity_management_sdk.models.k_8_s_filter_params_label_vec.K8SFilterParams_LabelVec.from_dictionary(structure))
        object_id_vec = dictionary.get("objectIdVec")

        # Return an object of this model
        return cls(
            entity_vec,
            label_vec_vec,
            object_id_vec
)