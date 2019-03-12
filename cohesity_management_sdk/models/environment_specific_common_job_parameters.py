# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.hyperv_environment_job_parameters
import cohesity_management_sdk.models.nas_environment_job_parameters
import cohesity_management_sdk.models.outlook_environment_job_parameters
import cohesity_management_sdk.models.physical_environment_job_parameters
import cohesity_management_sdk.models.pure_environment_job_parameters
import cohesity_management_sdk.models.sql_environment_job_parameters
import cohesity_management_sdk.models.vmware_environment_job_parameters

class EnvironmentSpecificCommonJobParameters(object):

    """Implementation of the 'Environment Specific Common Job Parameters.' model.

    Specifies additional parameters that are common to all Protection
    Sources in a Protection Job created for a particular environment type.

    Attributes:
        hyperv_parameters (HypervEnvironmentJobParameters): Specifies job
            parameters applicable for all 'kHyperV' Environment type
            Protection Sources in a Protection Job.
        nas_parameters (NASEnvironmentJobParameters): Specifies job parameters
            applicable for all 'kGenericNas' Environment type Protection
            Sources in a Protection Job.
        outlook_parameters (OutlookEnvironmentJobParameters): Specifies job
            parameters applicable for all 'kO365Outlook' Environment type
            Protection Sources in a Protection Job.
        physical_parameters (PhysicalEnvironmentJobParameters): Protection Job
            parameters applicable to 'kPhysical' Environment type. Specifies
            job parameters applicable for all 'kPhysical' Environment type
            Protection Sources in a Protection Job.
        pure_parameters (PureEnvironmentJobParameters): Specifies job
            parameters applicable for all 'kPure' Environment type Protection
            Sources in a Protection Job.
        sql_parameters (SQLEnvironmentJobParameters): Specifies job parameters
            applicable for all 'kSQL' Environment type Protection Sources in a
            Protection Job.
        vmware_parameters (VmwareEnvironmentJobParameters): Specifies job
            parameters applicable for all 'kVMware' Environment type
            Protection Sources in a Protection Job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hyperv_parameters":'hypervParameters',
        "nas_parameters":'nasParameters',
        "outlook_parameters":'outlookParameters',
        "physical_parameters":'physicalParameters',
        "pure_parameters":'pureParameters',
        "sql_parameters":'sqlParameters',
        "vmware_parameters":'vmwareParameters'
    }

    def __init__(self,
                 hyperv_parameters=None,
                 nas_parameters=None,
                 outlook_parameters=None,
                 physical_parameters=None,
                 pure_parameters=None,
                 sql_parameters=None,
                 vmware_parameters=None):
        """Constructor for the EnvironmentSpecificCommonJobParameters class"""

        # Initialize members of the class
        self.hyperv_parameters = hyperv_parameters
        self.nas_parameters = nas_parameters
        self.outlook_parameters = outlook_parameters
        self.physical_parameters = physical_parameters
        self.pure_parameters = pure_parameters
        self.sql_parameters = sql_parameters
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
        hyperv_parameters = cohesity_management_sdk.models.hyperv_environment_job_parameters.HypervEnvironmentJobParameters.from_dictionary(dictionary.get('hypervParameters')) if dictionary.get('hypervParameters') else None
        nas_parameters = cohesity_management_sdk.models.nas_environment_job_parameters.NASEnvironmentJobParameters.from_dictionary(dictionary.get('nasParameters')) if dictionary.get('nasParameters') else None
        outlook_parameters = cohesity_management_sdk.models.outlook_environment_job_parameters.OutlookEnvironmentJobParameters.from_dictionary(dictionary.get('outlookParameters')) if dictionary.get('outlookParameters') else None
        physical_parameters = cohesity_management_sdk.models.physical_environment_job_parameters.PhysicalEnvironmentJobParameters.from_dictionary(dictionary.get('physicalParameters')) if dictionary.get('physicalParameters') else None
        pure_parameters = cohesity_management_sdk.models.pure_environment_job_parameters.PureEnvironmentJobParameters.from_dictionary(dictionary.get('pureParameters')) if dictionary.get('pureParameters') else None
        sql_parameters = cohesity_management_sdk.models.sql_environment_job_parameters.SQLEnvironmentJobParameters.from_dictionary(dictionary.get('sqlParameters')) if dictionary.get('sqlParameters') else None
        vmware_parameters = cohesity_management_sdk.models.vmware_environment_job_parameters.VmwareEnvironmentJobParameters.from_dictionary(dictionary.get('vmwareParameters')) if dictionary.get('vmwareParameters') else None

        # Return an object of this model
        return cls(hyperv_parameters,
                   nas_parameters,
                   outlook_parameters,
                   physical_parameters,
                   pure_parameters,
                   sql_parameters,
                   vmware_parameters)


