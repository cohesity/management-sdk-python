# Copyright 2019 Cohesity Inc.
#
# Python example to
#   1. clone an existing view.
#   2. Update the cloned view.
# Usage: python clone_and_update_view.py --view_name=<name_of_view>
# --clone_name=<cloned_view_name>
import argparse
import json
import jsonpickle
import pprint
import random
import string

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.protocol_access_enum import ProtocolAccessEnum
from cohesity_management_sdk.models.view import View

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'

class CloneView(object):
    """
    Class to list the protection jobs.
    """

    def __init__(self, cohesity_client):
        self.view_client = cohesity_client.views

    def clone_existing_view(self, view_name, clone_name):
        """
        Method to clone the view.
        :param cohesity_client(obj): Cohesity Rest API client.
        :param view_name(str): View name.
        :param clone_name(str): Clone view name.
        :return None.
        """
        json_req = {"cloneViewName": clone_name, "sourceViewName": view_name}
        resp = self.view_client.create_clone_view(body=json_req)
        print ("Cloned view:")
        cloned_view = jsonpickle.encode(resp)
        pprint.pprint(json.loads(cloned_view))
        return cloned_view

    def update_view(self, view_name, protocol_access, description):
        """
        Method to update the existing view with different protocol & description
        :param view_name(str): Name of the view.
        :param protocol_access(str): Valid values: [ kAll, kNFSOnly,
                    kSMBOnly, kS3Only ]
        :param description(str): User defined description for the view.
        :return None.
        """
        req_json = View()
        req_json.description = description
        req_json.protocol_access = protocol_access
        resp = self.view_client.update_view_by_name(body=req_json,
                                                    name=view_name)
        updated_view = json.loads(jsonpickle.encode(resp))

        # Verify the fields updated
        assert updated_view['protocol_access']== protocol_access, "View not updated"
        assert updated_view['description'] == description, "View not updated"
        print ("Updated view:")
        pprint.pprint(updated_view)

def main(args):

    cohesity_client = CohesityClient(username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD)
    cohesity_client.config.cluster_vip = CLUSTER_VIP
    cohesity_client.config.disable_logging()
    cohesity_client.config.skip_ssl_verification = True
    view_name = args.view_name
    clone_name = args.clone_name

    if args.clone_name is None:
        clone_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+ \
                     '_cloned_view_' + args.view_name

    # Clone a view with name.
    try:
        cloneview = CloneView(cohesity_client)
        cloneview.clone_existing_view(view_name, clone_name)

        # Update the cloned view.
        cloneview.update_view(view_name=clone_name,
                              protocol_access=ProtocolAccessEnum.KNFSONLY,
                              description="View to restrict access to s3 only.")
    except APIException as e:
        print ("Error : %s" % e.context.response.raw_body)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--view_name", help="Name of the View to clone.", required=True)
    parser.add_argument("--clone_name", help="Clone view name.", required=False)
    args = parser.parse_args()
    main(args)