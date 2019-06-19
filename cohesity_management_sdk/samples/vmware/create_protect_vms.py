#!/usr/bin/env python
# Copyright 2019 Cohesity Inc.
#
# Python example to create VMs in vCenter using pyVmomi and protect these VMs.
#
#
# Usage: python protect_vms.py
# All the run configurations are in VM_CONFIG and JOB in config.py


import random
import time
from config import CLUSTER_VIP, CLUSTER_PASSWORD, CLUSTER_USERNAME, VM_CONFIG, JOB
from util import connect_vcenter, register_vcenter, \
    vcenter_exists, get_vm_ids, is_task_successful, get_obj

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.models.run_type_enum import RunTypeEnum
from cohesity_management_sdk.models.status_source_backup_status_enum import \
    StatusSourceBackupStatusEnum
from pyVmomi import vim

cohesity_client = CohesityClient(CLUSTER_VIP, CLUSTER_USERNAME,
                                 CLUSTER_PASSWORD)
vcenter_client = connect_vcenter()

#### VMWARE Methods ####
def get_vms(vmfolder):
    """
    Test method ot get VMs from Cohesity
    :param vmfolder:
    :return:
    """
    vms = vmfolder.childEntity
    for vm in vms:
        print("VM name: %s" % vm.name)
    return


def create_vms():
    """
    Method to create vm on vcenter.
    :param service_instance: vCenter service instance.
    :return:
    """
    content = vcenter_client.RetrieveContent()
    datacenter = content.rootFolder.childEntity[0]
    vm_folder = datacenter.vmFolder
    hosts = datacenter.hostFolder.childEntity
    resource_pool = hosts[0].resourcePool
    vm_list = []
    for num in range(VM_CONFIG['num_vms']):
        vm_name = VM_CONFIG['prefix_name'] + '-' + str(num)
        datastore_path = '[' + VM_CONFIG['data_store'] + '] ' + vm_name
        vmx_file = vim.vm.FileInfo(logDirectory=None,
                                   snapshotDirectory=None,
                                   suspendDirectory=None,
                                   vmPathName=datastore_path)
        config = vim.vm.ConfigSpec(name=vm_name,
                                   memoryMB=VM_CONFIG['memory'],
                                   numCPUs=VM_CONFIG['num_vcpu'],
                                   files=vmx_file,
                                   guestId=VM_CONFIG['guest_id'],
                                   version=VM_CONFIG['version'])
        print ("Creating VM %s" % vm_name)
        task = vm_folder.CreateVM_Task(config=config, pool=resource_pool)
        if not is_task_successful(task):
            raise SystemExit("Unable to create VM: %s "% vm_name)
        vm = get_obj(content, [vim.VirtualMachine], vm_name)
        print ("Powering on VM %s" % vm_name)
        task = vm.PowerOn()
        if not is_task_successful(task):
            raise SystemExit("Unable to power on VM: %s"% vm_name)
        vm_list.append(vm_name)
    return vm_list

#### Cohesity Methods ####

def check_protection_job_exists(protect_job_name):
    """
    Method to check if protection job exists.
    :param pj_name(str): Name of Protection Job.
    :return
        Boolean: Return True if exists, else return False.
        job_id(int): Protection job ID.
    """
    job_list = cohesity_client.protection_jobs.get_protection_jobs(
        only_return_basic_summary=True)
    for job in job_list:
        if job.name == protect_job_name:
            return True, job
    return False, None

def add_vms_to_protection_job(vm_id_list, resp):
    """
    Method to add VM list to the protection Job. This method assumes the
    prtection job is already protecting existing VMs in vCenter.
    :param vm_list(list): List of VMs to be protected.
    :param pj_name(str): Name of protection job.
    :return: None
    """
    # Add the vms to the protection job.
    resp.source_ids = vm_id_list + resp.source_ids
    update_resp = cohesity_client.protection_jobs.\
        update_protection_job(body=resp, id=resp.id)
    assert update_resp.source_ids == resp.source_ids,\
        "Failed to add VMs to Protection Jobs."
    print("VM(s) %s added to protection job successfully" % vm_id_list)

def create_protection_job(vm_ids, vcenter_id):
    """
    Method to create
    :param vm_ids [int]: List of VM id
    :param vcenter_id int: Vcenter ID in cohesity cluster.
    :return:
    """
    try:
        body = ProtectionJobRequestBody()
        body.name = JOB['name']
        body.policy_id = _get_protection_policy_id(JOB['policy_name'])
        body.view_box_id = _get_storage_domain_id()
        body.parent_source_id = vcenter_id
        body.source_ids = vm_ids
        body.timezone = "America/Los_Angeles"  # TODO use pytz
        cohesity_client.protection_jobs.create_protection_job(body)
    except APIException as ex:
        print("Unable to create Protection Job due to: %s" %
              ex.context.response.raw_body)
    print("Successfully added VMs added to protection job.")

def _get_protection_policy_id(policy_name):
    """
    Method to get the protection policy ID
    :return:
    """
    resp = cohesity_client.protection_policies.get_protection_policies(
        names=policy_name)
    return resp[0].id

def _get_storage_domain_id():
    """
    Method to get the storage domain id.
    :return:
    """
    resp = cohesity_client.view_boxes.get_view_boxes()
    view_box = random.choice(resp) # chooses random storage domain.
    return view_box.id

def run_job(job_name):
    """
    Method to run the Job specified on demand.
    :param job_name(str): Protection Job name.
    :return: None.
    """
    status, job_id = _name_to_job_id(job_name)
    if not status:
        print ("Protection Job with name: %s doesn't exist" % job_name)
        exit(0)

    req_body = ProtectionJobRequestBody()
    req_body.run_type = RunTypeEnum.KREGULAR
    cohesity_client.protection_jobs.create_run_protection_job(id=job_id,
                                                              body=req_body)

    # Get the status of this Job run.
    jresp = cohesity_client.protection_runs.get_protection_runs(job_id=job_id,
                                                                num_runs=1)
    if jresp == []:
        time.sleep(20)
        jresp = cohesity_client.protection_runs.get_protection_runs(
            job_id=job_id, num_runs=1)[0]
    else:
        jresp = jresp[0]
    if jresp.backup_run.status == StatusSourceBackupStatusEnum.KSUCCESS or \
            jresp.backup_run.status == StatusSourceBackupStatusEnum.KACCEPTED:
        print ("Protection Job %s started successfully" % job_name)
    elif jresp.backup_run.status == StatusSourceBackupStatusEnum.KERROR:
        print ("Protection Job %s failed." % job_name)

def _name_to_job_id(job_name):
    """
    Method to convert name of the job to id. If conflicts
    :param job_name(str): Name of the Protection job.
    :return
        status(bool): If Protection job doesn't exist, this is set to False.
        job_id(int) : Protection Job ID.
    """
    result = cohesity_client.protection_jobs.get_protection_jobs(names=job_name)
    if not result:
        return False, 0
    return True, result[0].id

def main():

    ### VMWARE actions ###

    vm_list = create_vms()

    ### Cohesity actions ###
    vcenter_id = vcenter_exists(cohesity_client)
    if not vcenter_id:
        vcenter_id = register_vcenter(cohesity_client)

    vm_ids_list = get_vm_ids(cohesity_client, vcenter_id, vm_list)
    if not vm_ids_list:
        print("Unable to get VM IDs from Cohesity.")
        exit()

    # Check if protection job exists.
    status, resp = check_protection_job_exists(JOB['name'])
    if not status:
        create_protection_job(vm_ids_list, vcenter_id)
    else:
        add_vms_to_protection_job(vm_ids_list, resp)

    # Run protection job.
    if JOB['run_now']:
        print("Running the protection job : %s" % JOB['name'])
        run_job(JOB['name'])

if __name__ == '__main__':
    main()
