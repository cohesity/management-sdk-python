# Copyright 2019 Cohesity Inc.
#
#Usage: python create_nas_from_backup.py --job_name NAS-Protect-hitachi-nas --cohesity_nfs_name cohesity_nas

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.environment_enum import EnvironmentEnum
from cohesity_management_sdk.models.protocol_access_enum import ProtocolAccessEnum
from cohesity_management_sdk.models.recover_task_request import RecoverTaskRequest
from cohesity_management_sdk.models.restore_object_details import RestoreObjectDetails
from cohesity_management_sdk.models.update_view_param import UpdateViewParam
from cohesity_management_sdk.models.qo_s import QoS

import argparse
import configparser


configparser = configparser.ConfigParser()
configparser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=configparser.get('cohesity', 'cluster_vip'),
                                 username=configparser.get('cohesity', 'username'),
                                 password=configparser.get('cohesity', 'password'),
                                 domain= configparser.get('cohesity', 'domain'))

def main(args):

    try:
        resp = cohesity_client.protection_jobs.get_protection_jobs(
            environments=EnvironmentEnum.KGENERICNAS,
            names=args.job_name)
        if len(resp) == 0 : # No protection Job exist.
            print("No protection job with : %s" % args.job_name)
            exit(1)
        if len(resp) > 1:
            print("More than one protection job exists with this prefix."
                       "Provide the Protection job name more specifically.")
            exit(1)
        for job in resp:
            cohesity_nfs_name = args.cohesity_nfs_name
            body = RecoverTaskRequest()
            body.name = 'Recover-' + cohesity_nfs_name
            body.mtype = "kMountFileVolume"
            body.view_name = cohesity_nfs_name

            body.objects = []
            body.objects.append(RestoreObjectDetails())
            body.objects[0].job_id = job.id
            body.objects[0].protection_source_id = job.source_ids[0]

            body.restore_view_parameters = UpdateViewParam()
            body.restore_view_parameters.protocol_access = ProtocolAccessEnum.KNFSONLY
            body.restore_view_parameters.qos = QoS()
            body.restore_view_parameters.qos.principal_name = \
                configparser.get('cohesity', 'nfs_target_qos')

            cohesity_client.restore_tasks.create_recover_task(body=body)
            print("Scheduled to create NFS share %s." % cohesity_nfs_name)

            #TODO: poll for the restore task and copy NFS mount path.

    except APIException as ex:
        SystemExit("Unable to create Cohesity NFS share. Error: %s" %
                   ex.message)
    print("Successfully created NFS share %s on Cohesity." %
          args.cohesity_nfs_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Arguments needed to run this python process.")
    parser.add_argument("--job_name", help="Protection Job Name",
                        required=True)
    parser.add_argument("--cohesity_nfs_name", help="Cohesity NFS share name",
                        required=True)
    args = parser.parse_args()
    main(args)