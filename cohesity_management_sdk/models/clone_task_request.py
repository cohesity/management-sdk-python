# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.clone_view_request
import cohesity_management_sdk.models.hyperv_clone_parameters
import cohesity_management_sdk.models.restore_object_details
import cohesity_management_sdk.models.vlan_parameters
import cohesity_management_sdk.models.vmware_clone_parameters

class CloneTaskRequest(object):

    """Implementation of the 'CloneTaskRequest' model.

    Specifies the settings for a Restore Task that clones VMs or Views.

    Attributes:
        clone_view_parameters (CloneViewRequest): Specifies settings for
            cloning an existing View. This field is required for a
            'kCloneView' Restore Task.
        continue_on_error (bool): Specifies if the Restore Task should
            continue when some operations on some objects fail. If true, the
            Cohesity Cluster ignores intermittent errors and restores as many
            objects as possible.
        glacier_retrieval_type (GlacierRetrievalTypeEnum): Specifies the way
            data needs to be retrieved from the external target. This
            information will be filled in by Iris and Magneto will pass it
            along to the Icebox as it is to support bulk retrieval from
            Glacier. Specifies the type of Restore Task.  'kStandard'
            specifies retrievals that allow to access any of your archives
            within several hours. Standard retrievals typically complete
            within 3–5 hours.This is the default option for retrieval requests
            that do not specify the retrieval option. 'kBulk' specifies
            retrievals that are Glacier’s lowest-cost retrieval option, which
            can be use to retrieve large amounts, even petabytes, of data
            inexpensively in a day. Bulk retrieval typically complete within
            5–12 hours. 'kExpedited' specifies retrievals that allows to
            quickly access your data when occasional urgent requests for a
            subset of archives are required. For all but the largest archives
            (250 MB+), data accessed using Expedited retrievals are typically
            made available within 1–5 minutes.
        hyperv_parameters (HypervCloneParameters): Specifies information
            needed when cloning VMs in HyperV enviroment. This field defines
            the HyperV specific params for restore tasks of type kCloneVMs.
        name (string): Specifies the name of the Restore Task. This field must
            be set and must be a unique name.
        new_parent_id (long|int): Specify a new registered parent Protection
            Source. If specified the selected objects are cloned or recovered
            to this new Protection Source. If not specified, objects are
            cloned or recovered to the original Protection Source that was
            managing them.
        objects (list of RestoreObjectDetails): Array of Objects.  Specifies a
            list of Protection Source objects or Protection Job objects (with
            specified Protection Source objects).
        target_view_name (string): Specifies the name of the View where the
            cloned VMs are stored. This field is required for a 'kCloneVMs'
            Restore Task.
        mtype (TypeCloneTaskRequestEnum): Specifies the type of Restore Task
            such as 'kCloneVMs' or 'kCloneView'. 'kCloneVMs' specifies a
            Restore Task that clones VMs. 'kCloneView' specifies a Restore
            Task that clones a View.
        vlan_parameters (VlanParameters): Specifies VLAN parameters for the
            restore operation.
        vmware_parameters (VmwareCloneParameters): Specifies the information
            required for recovering or cloning VmWare VMs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "clone_view_parameters":'cloneViewParameters',
        "continue_on_error":'continueOnError',
        "glacier_retrieval_type":'glacierRetrievalType',
        "hyperv_parameters":'hypervParameters',
        "new_parent_id":'newParentId',
        "objects":'objects',
        "target_view_name":'targetViewName',
        "vlan_parameters":'vlanParameters',
        "vmware_parameters":'vmwareParameters'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 clone_view_parameters=None,
                 continue_on_error=None,
                 glacier_retrieval_type=None,
                 hyperv_parameters=None,
                 new_parent_id=None,
                 objects=None,
                 target_view_name=None,
                 vlan_parameters=None,
                 vmware_parameters=None):
        """Constructor for the CloneTaskRequest class"""

        # Initialize members of the class
        self.clone_view_parameters = clone_view_parameters
        self.continue_on_error = continue_on_error
        self.glacier_retrieval_type = glacier_retrieval_type
        self.hyperv_parameters = hyperv_parameters
        self.name = name
        self.new_parent_id = new_parent_id
        self.objects = objects
        self.target_view_name = target_view_name
        self.mtype = mtype
        self.vlan_parameters = vlan_parameters
        self.vmware_parameters = vmware_parameters


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
        mtype = dictionary.get('type')
        clone_view_parameters = cohesity_management_sdk.models.clone_view_request.CloneViewRequest.from_dictionary(dictionary.get('cloneViewParameters')) if dictionary.get('cloneViewParameters') else None
        continue_on_error = dictionary.get('continueOnError')
        glacier_retrieval_type = dictionary.get('glacierRetrievalType')
        hyperv_parameters = cohesity_management_sdk.models.hyperv_clone_parameters.HypervCloneParameters.from_dictionary(dictionary.get('hypervParameters')) if dictionary.get('hypervParameters') else None
        new_parent_id = dictionary.get('newParentId')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(structure))
        target_view_name = dictionary.get('targetViewName')
        vlan_parameters = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParameters')) if dictionary.get('vlanParameters') else None
        vmware_parameters = cohesity_management_sdk.models.vmware_clone_parameters.VmwareCloneParameters.from_dictionary(dictionary.get('vmwareParameters')) if dictionary.get('vmwareParameters') else None

        # Return an object of this model
        return cls(name,
                   mtype,
                   clone_view_parameters,
                   continue_on_error,
                   glacier_retrieval_type,
                   hyperv_parameters,
                   new_parent_id,
                   objects,
                   target_view_name,
                   vlan_parameters,
                   vmware_parameters)


