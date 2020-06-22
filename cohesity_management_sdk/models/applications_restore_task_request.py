# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.application_restore_object
import cohesity_management_sdk.models.restore_object_details
import cohesity_management_sdk.models.vlan_parameters

class ApplicationsRestoreTaskRequest(object):

    """Implementation of the 'ApplicationsRestoreTaskRequest' model.

    Specifies the request to create a restore task for restoring Application
    Servers like SQL or Exchange servers hosted by a Protection Source.

    Attributes:
        application_environment (ApplicationEnvironmentEnum): Specifies the
            Environment of the Application to restore like 'kSQL', or
            'kExchange'. overrideDescription: true Supported environment types
            such as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers
            to Cohesity's Remote Adapter. 'kVMware' indicates the VMware
            Protection Source environment. 'kHyperV' indicates the HyperV
            Protection Source environment. 'kSQL' indicates the SQL Protection
            Source environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'kAzure' indicates the Microsoft's Azure Protection Source
            environment. 'kNetapp' indicates the Netapp Protection Source
            environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Genreric Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhsicalFiles' indicates
            the Physical Files Protection Source environment. 'kIsilon'
            indicates the Dell EMC's Isilon Protection Source environment.
            'kKVM' indicates the KVM Protection Source environment. 'kAWS'
            indicates the AWS Protection Source environment. 'kExchange'
            indicates the Exchange Protection Source environment. 'kHyperVVSS'
            indicates the HyperV VSS Protection Source environment. 'kOracle'
            indicates the Oracle Protection Source environment. 'kGCP'
            indicates the Google Cloud Platform Protection Source environment.
            'kFlashBlade' indicates the Flash Blade Protection Source
            environment. 'kAWSNative' indicates the AWS Native Protection
            Source environment. 'kO365' indicates the Office 365 Protection
            Source environment. 'kO365Outlook' indicates Office 365 outlook
            Protection Source environment. 'kHyperFlex' indicates the Hyper
            Flex Protection Source environment. 'kGCPNative' indicates the GCP
            Native Protection Source environment. 'kAzureNative' indicates the
            Azure Native Protection Source environment.
        application_restore_objects (list of ApplicationRestoreObject):
            Specifies the Application Server objects whose data should be
            restored and the restore parameters for each of them.
        hosting_protection_source (RestoreObjectDetails): Specifies an object
            to recover or clone or an object to restore files and folders
            from. A VM object can be recovered or cloned. A View object can be
            cloned. To specify a particular snapshot, you must specify a
            jobRunId and a startTimeUsecs. If jobRunId and startTimeUsecs are
            not specified, the last Job Run of the specified Job is used.
        name (string): Specifies a name for the new task to be created. This
            field has to be set, and it needs to be unique across all restore
            tasks.
        password (string): Specifies password of the username to access the
            target source.
        username (string): Specifies username to access the target source.
        vlan_parameters (VlanParameters): Specifies VLAN parameters for the
            restore operation.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_environment":'applicationEnvironment',
        "hosting_protection_source":'hostingProtectionSource',
        "name":'name',
        "application_restore_objects":'applicationRestoreObjects',
        "password":'password',
        "username":'username',
        "vlan_parameters":'vlanParameters'
    }

    def __init__(self,
                 application_environment=None,
                 hosting_protection_source=None,
                 name=None,
                 application_restore_objects=None,
                 password=None,
                 username=None,
                 vlan_parameters=None):
        """Constructor for the ApplicationsRestoreTaskRequest class"""

        # Initialize members of the class
        self.application_environment = application_environment
        self.application_restore_objects = application_restore_objects
        self.hosting_protection_source = hosting_protection_source
        self.name = name
        self.password = password
        self.username = username
        self.vlan_parameters = vlan_parameters


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
        application_environment = dictionary.get('applicationEnvironment')
        hosting_protection_source = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('hostingProtectionSource')) if dictionary.get('hostingProtectionSource') else None
        name = dictionary.get('name')
        application_restore_objects = None
        if dictionary.get('applicationRestoreObjects') != None:
            application_restore_objects = list()
            for structure in dictionary.get('applicationRestoreObjects'):
                application_restore_objects.append(cohesity_management_sdk.models.application_restore_object.ApplicationRestoreObject.from_dictionary(structure))
        password = dictionary.get('password')
        username = dictionary.get('username')
        vlan_parameters = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParameters')) if dictionary.get('vlanParameters') else None

        # Return an object of this model
        return cls(application_environment,
                   hosting_protection_source,
                   name,
                   application_restore_objects,
                   password,
                   username,
                   vlan_parameters)


