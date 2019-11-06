#!/usr/bin/env python
# Copyright 2019 Cohesity Inc.
#
# Util methods for vcenter related functions.
#
import atexit
import time

from pyVim.connect import SmartConnectNoSSL, Disconnect
from cohesity_management_sdk.models.environment_enum import EnvironmentEnum
from cohesity_management_sdk.models.register_protection_source_parameters \
    import RegisterProtectionSourceParameters
from cohesity_management_sdk.models.vmware_type_enum import VmwareTypeEnum
from config import VCENTER_IP, \
    VCENTER_USERNAME, VCENTER_PASSWORD, DEFAULT_PORT

def connect_vcenter():
    """
    Connect to vcenter using the file defined credentials.
    :return None
    """
    try:
        si = SmartConnectNoSSL(host=VCENTER_IP,
                               user=VCENTER_USERNAME,
                               pwd=VCENTER_PASSWORD,
                               port=DEFAULT_PORT)
        atexit.register(Disconnect, si)
        return si
    except Exception as ex:
        print("Unable to connection to vCenter due to: %s" % ex.message)

def register_vcenter(cohesity_client):
    """
    Register vCenter as protection source.
    :param cohesity_client (CohesityClient): Cohesity Management SDK
    Client Object.
    :return: None
    """
    req_body = RegisterProtectionSourceParameters()
    req_body.endpoint = VCENTER_IP
    req_body.username = VCENTER_USERNAME
    req_body.password = VCENTER_PASSWORD
    req_body.environment = EnvironmentEnum.K_VMWARE
    req_body.vmware_type = VmwareTypeEnum.KVCENTER
    try:
        source = cohesity_client.protection_sources
        return source.create_register_protection_source(req_body)['entity']['id']
    except Exception as ex:
        print("Error in registering vcenter %s" % ex.message)
    print("Successfully Registered the vCenter.")

def vcenter_exists(cohesity_client):
    """
    Method to check if vcenter exists in the cluster
    :return (bool): Returns True if vcenter exists else returns False
    """
    vcenter_id = None
    resp = cohesity_client.protection_sources\
        .list_protection_sources_registration_info(environments=[
        EnvironmentEnum.K_VMWARE])
    for obj in resp.root_nodes:
        if obj.root_node.name == VCENTER_IP or \
           obj.registration_info.access_info.endpoint == VCENTER_IP:
           vcenter_id = obj.root_node.id
           return vcenter_id
    return vcenter_id

def get_vm_ids(cohesity_client, vcenter_id, vm_list):
    """
    Method to check if VM exists
    :return:(list) List of VM IDs in Cohesity.
    """
    # Refresh vcenter list :
    refresh_count = 0
    vm_id_list = []
    str_vm_list = ','.join(vm_list)
    while refresh_count < 60: # Time out for an hour.
        cohesity_client.protection_sources\
            .create_refresh_protection_source_by_id(vcenter_id)
        # Note: This API works only with vCenter VMs.
        resp_vm_list = cohesity_client.protection_sources.\
            list_virtual_machines(names=str_vm_list)
        if not resp_vm_list:
            refresh_count += 1
            print("Unable to get VMs from Cohesity , Refreshing source, "
                  "count: %s" % refresh_count)
            time.sleep(60)
            continue
        return [vm.id for vm in resp_vm_list]
    print("VM list: %s" % vm_id_list)
    return vm_id_list

def is_task_successful(task, retry=10 , interval=5):
    """
    Method to check the task state.
    :param task: VMware task.
    :param retry(int): Number of Retries.
    :param interval(int): Interval between each retry.
    :return: bool(
    """
    while retry > 0:
        task_status = str(task.info.state)
        if task_status == 'success':
            return True
        if task_status== 'running':
            time.sleep(interval)
        retry -= 1
    print("Task not successful.")
    return False

def get_obj(content, vimtype, name):
    """Create contrainer view and search for object in it."""
    obj = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True)
    for c in container.view:
        if name:
            if c.name == name:
                obj = c
                break
        else:
            obj = c
            break

    container.Destroy()
    return obj

