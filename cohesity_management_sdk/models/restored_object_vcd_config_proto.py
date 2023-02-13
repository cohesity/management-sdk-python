# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.connector_params
import cohesity_management_sdk.models.restore_object

class RestoredObjectVCDConfigProto(object):

    """Implementation of the 'RestoredObjectVCDConfigProto' model.

    TODO: type model description here.

    Attributes:
        is_vapp (bool): Whether the restored object is a VApp.
        is_vapp_template (bool): Whether the restored object is a VApp
            template.
        restored_vapp_info (EntityProto): Entity info enabled only when
            is_vapp is true. This proto will contain the original vApp that
            is protected (deprecated)
        restored_vapp_object (RestoreObject): Enabled only when is_vapp is
            true. This proto will contain the original vApp that is protected.
        restored_vapp_template_info (EntityProto): Entity info enabled only
            when is_vapp_template is true. This proto will contain the
            original vApp template that is protected (deprecated)
        restored_vapp_template_object (RestoreObject): Enabled only when
            is_vapp_template is true. This proto will contain the original
            vApp template that is protected.
        vapp_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        vcenter_connector_params (ConnectorParams): Message that encapsulates
            the various params required to establish a connection with a
            particular environment.
        vdc_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_vapp":'isVapp',
        "is_vapp_template":'isVappTemplate',
        "restored_vapp_info":'restoredVappInfo',
        "restored_vapp_object":'restoredVappObject',
        "restored_vapp_template_info":'restoredVappTemplateInfo',
        "restored_vapp_template_object":'restoredVappTemplateObject',
        "vapp_entity":'vappEntity',
        "vcenter_connector_params":'vcenterConnectorParams',
        "vdc_entity":'vdcEntity'
    }

    def __init__(self,
                 is_vapp=None,
                 is_vapp_template=None,
                 restored_vapp_info=None,
                 restored_vapp_object=None,
                 restored_vapp_template_info=None,
                 restored_vapp_template_object=None,
                 vapp_entity=None,
                 vcenter_connector_params=None,
                 vdc_entity=None):
        """Constructor for the RestoredObjectVCDConfigProto class"""

        # Initialize members of the class
        self.is_vapp = is_vapp
        self.is_vapp_template = is_vapp_template
        self.restored_vapp_info = restored_vapp_info
        self.restored_vapp_object = restored_vapp_object
        self.restored_vapp_template_info = restored_vapp_template_info
        self.restored_vapp_template_object = restored_vapp_template_object
        self.vapp_entity = vapp_entity
        self.vcenter_connector_params = vcenter_connector_params
        self.vdc_entity = vdc_entity


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
        is_vapp = dictionary.get('isVapp')
        is_vapp_template = dictionary.get('isVappTemplate')
        restored_vapp_info = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoredVappInfo')) if dictionary.get('restoredVappInfo') else None
        restored_vapp_object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('restoredVappObject')) if dictionary.get('restoredVappObject') else None
        restored_vapp_template_info = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoredVappTemplateInfo')) if dictionary.get('restoredVappTemplateInfo') else None
        restored_vapp_template_object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('restoredVappTemplateObject')) if dictionary.get('restoredVappTemplateObject') else None
        vapp_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vappEntity')) if dictionary.get('vappEntity') else None
        vcenter_connector_params = cohesity_management_sdk.models.connector_params.ConnectorParams.from_dictionary(dictionary.get('vcenterConnectorParams')) if dictionary.get('vcenterConnectorParams') else None
        vdc_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vdcEntity')) if dictionary.get('vdcEntity') else None

        # Return an object of this model
        return cls(is_vapp,
                   is_vapp_template,
                   restored_vapp_info,
                   restored_vapp_object,
                   restored_vapp_template_info,
                   restored_vapp_template_object,
                   vapp_entity,
                   vcenter_connector_params,
                   vdc_entity)


