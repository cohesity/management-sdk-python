# Copyright 2019 Cohesity Inc.
#
# Usage: python backup_nas_to_cohesity.py


from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.models.environment_enum import EnvironmentEnum
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.run_protection_job_param import RunProtectionJobParam

import configparser
import json
import requests


parser = configparser.ConfigParser()
parser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=parser.get('cohesity', 'cluster_vip'),
                                 username=parser.get('cohesity', 'username'),
                                 password=parser.get('cohesity', 'password'),
                                 domain= parser.get('cohesity', 'domain'))

def register_nas_source(nas_source):

    url = 'https://%s/irisservices/api/v1/backupsources' % \
          cohesity_client.config.cluster_vip
    cohesity_client.auth.authorize()
    bearer_token = cohesity_client.config.auth_token.access_token
    data = {
        "entity": {
            "type": 11,
            "genericNasEntity": {
                "protocol": 1,
                "type": 1,
                "path": nas_source
            }
        },
        "entityInfo": {
            "endpoint": nas_source,
            "type": 11
        }
    }
    headers = {"Authorization": "Bearer %s" % bearer_token}
    resp = requests.post(url=url, data=json.dumps(data), headers=headers,
                         verify=False)
    if not resp.ok:
        print("Registration of %s unsuccessfull, skipping protection job "
              "creation." % nas_source)
        print("Reason: %s, Status_Code %s" % (resp.reason, resp.status_code))
        print("Message: %s" % resp.json()['message'])

    return resp.json()['entity']['id']

def get_policy_id(policy_name):
    try:
        policy_resp = cohesity_client.protection_policies\
            .get_protection_policies(names=policy_name)
        return policy_resp[0].id
    except:
        SystemExit("Unable to get Protection Policy ")

def get_storage_domain_id(storage_domain):
    try:
        sd_resp = cohesity_client.view_boxes.get_view_boxes(
            names=storage_domain)
        return sd_resp[0].id
    except:
        SystemExit("Unable to get Storage Domain details")

def create_nas_protection_job(nas_source, object_id):
    try:
        body = ProtectionJobRequestBody()
        body.environment = EnvironmentEnum.KGENERICNAS
        body.name = parser.get('cohesity', 'job_name_prefix')  + \
                    nas_source.split(':/')[1]
        body.policy_id = get_policy_id(parser.get('cohesity', 'policy'))
        body.view_box_id = get_storage_domain_id(parser.get('cohesity','storage_domain'))
        body.source_ids=[object_id]
        body.parent_source_id = \
        cohesity_client.protection_sources.list_protection_sources_root_nodes(
            environments=EnvironmentEnum.KGENERICNAS)[0].protection_source.id
        body.timezone = cohesity_client.cluster.get_cluster().timezone
        pro_resp = cohesity_client.protection_jobs.create_protection_job(body=body)
        return pro_resp.id
    except APIException as ex:
        print("Unable to create Protection Job for %s due to: %s" %(
            nas_source, ex.message))


def run_protection_job(job_id):
    try:
        resp = cohesity_client.protection_runs.get_protection_runs(
            num_runs=1, job_id=job_id)
        if len(resp) == 0: #This means protection run has not started.
            cohesity_client.protection_jobs.create_run_protection_job(id=job_id,
                                                                  body=RunProtectionJobParam())
    except APIException as ex:
        print("Unable to start Protection Job for due to: %s" % ex.message)


def main():
    for _, nas_source in parser.items('nas_export_list'):
        # Register the sources.
        object_id = register_nas_source(nas_source)
        print("Registered the NAS target: %s successfully." % nas_source)
        # Create protection job for each source.
        job_id = create_nas_protection_job(nas_source, object_id)
        pj_name = parser.get('cohesity','job_name_prefix') + \
                   nas_source.split(':/')[1]
        print("Protection Job %s created for the NAS target: %s "
              "successfully." % (pj_name, nas_source))

        # Trigger protection run
        run_protection_job(job_id)
        print("Backup for NAS : %s has started."% nas_source)

        # Poll for protection run complete %
        #TODO if enhancement request

if __name__ == '__main__':
    main()

