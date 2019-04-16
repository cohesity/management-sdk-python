# Copyright 2019 Cohesity Inc.
#
# Python example to add a VM to a protection Job.
#
# Usage: python register_vcenter.py

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.environment_enum import EnvironmentEnum
from cohesity_management_sdk.models.vmware_type_enum import VmwareTypeEnum
from cohesity_management_sdk.models.register_protection_source_parameters import RegisterProtectionSourceParameters


CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
DOMAIN = 'LOCAL'
VCENTER_IP = 'vcenter_ip'
VCENTER_USERNAME = 'administrator'
VCENTER_PASSWORD = 'vcenter_password'

class AddVCenter(object):

    def __init__(self, cohesity_client):
        self.cohesity_client = cohesity_client

    def register_vcenter(self):
        """
        Method to register vcenter.
        :return True, False.
        """
        req_body = RegisterProtectionSourceParameters()
        req_body.endpoint = VCENTER_IP
        req_body.username = VCENTER_USERNAME
        req_body.password = VCENTER_PASSWORD
        req_body.environment = EnvironmentEnum.K_VMWARE
        req_body.vmware_type = VmwareTypeEnum.KVCENTER
        source = self.cohesity_client.protection_sources
        source.create_register_protection_source(req_body)
        print("Successfully Registered the vCenter.")


def main():
    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				     domain=DOMAIN)
    vcenter_object = AddVCenter(cohesity_client)
    vcenter_object.register_vcenter()

if __name__ == '__main__':
    main()
