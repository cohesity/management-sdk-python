#!/usr/bin/env python
# Copyright 2019 Cohesity Inc.
#
# Python example to recover/restore  VMs in vCenter. This assumes the VMs
# are part of protection job in Cohesity cluster.
#
#
# Usage: python recover_vms.py
# All the vCenter, cohesity, VM recover configs are in config.py

import time

from pyVmomi import vim

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.recover_task_request import \
    RecoverTaskRequest
from cohesity_management_sdk.models.restore_object_details import \
    RestoreObjectDetails
from cohesity_management_sdk.models.type_recover_task_request_enum import \
    TypeRecoverTaskRequestEnum
from cohesity_management_sdk.models.vmware_restore_parameters import \
    VmwareRestoreParameters
from config import VM_CONFIG, CLUSTER_USERNAME, CLUSTER_PASSWORD,\
    CLUSTER_VIP, RESTORE, JOB
from util import connect_vcenter, \
    vcenter_exists, register_vcenter, get_vm_ids, get_obj, is_task_successful

vmware_client = connect_vcenter()
cohesity_client = CohesityClient(CLUSTER_VIP, CLUSTER_USERNAME,
                                 CLUSTER_PASSWORD)

#### VMware methods ####

def delete_vms_in_vcenter():
    """
    Method to delete VMs in vcenter
    :return:
    """
    for num in range(VM_CONFIG['num_vms']):
        vm_name = VM_CONFIG['prefix_name'] + '-' + str(num)
        vm_object = get_obj(vmware_client.content, [vim.VirtualMachine],
                             vm_name)
        if vm_object is None:
            print("Unable to locate the VM: %s" % vm_name)
            continue
        print("Powering off VM: %s" % vm_name)
        task = vm_object.PowerOffVM_Task()
        if not is_task_successful(task):
            print("VM already powered off, will try and destroy")
        print("Destroying VM: %s" % vm_name)
        task = vm_object.Destroy_Task()
        if not is_task_successful(task):
            raise SystemExit("Unable to destroy VM: %s" % vm_name)

def verify_vms_recovered():
    """
    This method checks vcenter to see if the VMs are successfully recovered.
    :return bool
    """
    vm_recover_list = []
    for num in range(VM_CONFIG['num_vms']):
        vm_name = VM_CONFIG['prefix_name'] + '-' + str(num)
        vm_object = get_obj(vmware_client.content, [vim.VirtualMachine],
                             vm_name)
        if vm_object:
            vm_recover_list.append(vm_name)
    print("VMs recovered: %s" % vm_recover_list)

##### Cohesity methods ####

def check_vms_in_cohesity():
    """
    Method to get the VM IDs from cohesity.
    :return: None
    """
    vcenter_id = vcenter_exists(cohesity_client)
    if not vcenter_id:
        vcenter_id = register_vcenter(cohesity_client)
    vm_id_list = get_vm_ids(cohesity_client, vcenter_id, RESTORE['vm_list'])
    if not vm_id_list:
        print("Unable to get VM IDs from Cohesity.")
        exit()

def recover_vms_in_cohesity():
    """
    Method to recover the VMs in Cohesity.
    :return: None
    """
    body = RecoverTaskRequest()
    body.name = RESTORE['name']
    body.type = TypeRecoverTaskRequestEnum.KRECOVERVMS
    body.vmware_parameters = VmwareRestoreParameters()
    body.vmware_parameters.disable_network = False
    body.vmware_parameters.powered_on = True

    body.objects = []
    body.objects.append(RestoreObjectDetails())
    body.objects[0].job_id = _get_protection_job_id(JOB['name'])
    try:
        restore_task = cohesity_client.restore_tasks.create_recover_task(body)
        task_id = restore_task.id
        _poll_for_task_complete(task_id)
    except Exception as ex:
        raise SystemExit("Error in recovering the VMs due to %s",
                         ex.message)

def _get_protection_job_id(job_name):
    """
    Method to get the protection job id.
    :return(int) . Protection job id
    """
    job = cohesity_client.protection_jobs.get_protection_jobs(
        names=job_name)[0]
    return job.id

def _poll_for_task_complete(task_id, timeout = 360, interval=10):
    """
    Method to poll for Restore task status.
    :param task_id(int): Restore task id.
    :return: None.
    """
    resp = cohesity_client.restore_tasks.get_restore_task_by_id(task_id)
    for num in xrange(1, timeout):
        if resp.status == 'kFinished':
            print("Task completed Successfully")
            return
        else:
            print("Elapsed time: %s Task status: %s" % (num*interval,
                                                        resp.status))
            time.sleep(interval)
            resp = cohesity_client.restore_tasks.get_restore_task_by_id(
                task_id)
    raise SystemExit("Unable to complete the task in %s seconds" % num *
                     interval)

def main():

    # Check if VMs are already deleted.
    if not RESTORE['vms_deleted']:
        # Check if VMs are in Cohesity Cluster.
        check_vms_in_cohesity()

        # Delete these VMs in vCenter.
        delete_vms_in_vcenter()

    # Recover these VMs and poll for the Recover Task.
    recover_vms_in_cohesity()

    # Verify in vCenter the VMs have recovered.
    verify_vms_recovered()

if __name__ == '__main__':
    main()
