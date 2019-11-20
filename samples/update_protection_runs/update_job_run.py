# Copyright 2019 Cohesity Inc.
#
# Python example to extend the snapshot retention per protection job run. The
# runs can be filtered by start/end date.
#
# Usage : python update_job_run.py --job_name=<protect-job>
# --start_date=2019-2-31 --end_date=2019-7-29 --extend=<num-of-days>
#
# --extend = 30 # Extends snapshot retention by 30 days or 1 month.
# --extend = 0 # Deletes the snapshot.
# --extend = -10 # Reduces the snapshot by 10 days.


import argparse
import datetime

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.type_run_job_snapshot_target_enum import \
    TypeRunJobSnapshotTargetEnum
from cohesity_management_sdk.models.run_job_snapshot_target import \
    RunJobSnapshotTarget
from cohesity_management_sdk.models.update_protection_job_run import \
    UpdateProtectionJobRun
from cohesity_management_sdk.models.update_protection_job_runs_param import \
    UpdateProtectionJobRunsParam
from cohesity_management_sdk.models.universal_id import UniversalId

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
DOMAIN = 'LOCAL'

MILLISECONDS = '0' * 6
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME,
                                 password=CLUSTER_PASSWORD,
                                 domain=DOMAIN)

def get_job_details(job_name):
    """
    Function to get job related attributes
    :param job_name:
    :return: job_id, cluster_id and cluster_incarnation_id.
    """
    try:
        job = cohesity_client.protection_jobs.get_protection_jobs(names=job_name)[0]
    except APIException as ex:
        print("Unable to get the protection job details.")
    return job.uid.id, job.uid.cluster_id, job.uid.cluster_incarnation_id


def convert_to_epoch(date, end_time=False):
    """
    Helper function to convert date to epochtime
    :param date:
    :return: datetime
    """
    if end_time:
        # This is to get the time till end of the day.
        return datetime.datetime(int(date[0]), int(date[1]),
                                 int(date[2]), 23, 59).strftime('%s')
    return datetime.datetime(int(date[0]), int(date[1]), int(date[2])).strftime('%s')


def convert_to_date(epoch):
    """
    Convert epoch to date
    :param epoch:
    :return:
    """
    return datetime.datetime.fromtimestamp(epoch / 1000000).strftime('%c')


def change_retention(job_run, job_id, cluster_id, incarnation_id, extend):
    """
    Change the snapshot retention time.
    :param job_run:
    :param job_id:
    :param cluster_id:
    :param incarnation_id:
    :param extend:
    :return:
    """
    body = UpdateProtectionJobRunsParam()
    body.job_runs = []
    index = 0

    if len(job_run) == 0:
        print("No Job Run to update for this protection job.")
        return

    for run in job_run:
        if run.backup_run.snapshots_deleted:
            continue
        body.job_runs.append(UpdateProtectionJobRun())
        body.job_runs[index].job_uid = UniversalId()
        body.job_runs[index].job_uid.cluster_id = cluster_id
        body.job_runs[index].job_uid.cluster_incarnation_id = incarnation_id
        body.job_runs[index].job_uid.id = job_id
        body.job_runs[index].run_start_time_usecs = run.copy_run[
            0].run_start_time_usecs
        body.job_runs[index].copy_run_targets = []
        body.job_runs[index].copy_run_targets.append(RunJobSnapshotTarget())
        body.job_runs[index].copy_run_targets[0].days_to_keep = int(extend)
        body.job_runs[index].copy_run_targets[0].mtype = \
            TypeRunJobSnapshotTargetEnum.KLOCAL
        index += 1
    try:
        cohesity_client.protection_runs.update_protection_runs(body=body)
    except APIException as ex:
       raise SystemExit("Unable to update the protection job")

    print ('{0:<10}\t\t{1:>24}\t\t{2:>10}\t\t{3:>10}'.format('Start Time',
                                                             'Status',
                                                             'Success/Error',
                                                             'Extended '
                                                             'Snapshot?'))
    for run in job_run:
        yes = 'Yes'
        if run.backup_run.snapshots_deleted:
            yes = 'Deleted'
        print ('{0:<10}\t\t{1:>10}\t\t{2:>10}\t\t{3:>10}'.format(
            str(convert_to_date(run.backup_run.stats.start_time_usecs)),
            run.backup_run.status,
            str(job_run[0].backup_run.stats.num_successful_tasks) + '/' +
            str(job_run[0].backup_run.stats.num_failed_tasks), yes))



def main(args):
    start_time = convert_to_epoch(args.start_date.split('-')) + MILLISECONDS
    end_time = convert_to_epoch(args.end_date.split('-'), True) + MILLISECONDS

    job_id, cluster_id, incarnation_id = get_job_details(args.job_name)
    job_run = cohesity_client.protection_runs.get_protection_runs(
        job_id=job_id, start_time_usecs=start_time, end_time_usecs=end_time)

    change_retention(job_run, job_id, cluster_id, incarnation_id, args.extend)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Arguments needed to run this python script.")
    parser.add_argument("--job_name", help="Protection Job Name",
                        required=True)
    parser.add_argument("--start_date", help="Format YEAR-MM-DD",
                        required=True)
    parser.add_argument("--end_date",
                        help="Format YEAR-MM-DD",
                        required=True)
    parser.add_argument("--extend",
                        help="In number of days",
                        required=True)
    args = parser.parse_args()
    main(args)
