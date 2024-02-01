# Copyright 2019 Cohesity Inc.
#
# Python example to
#    0. Handle invalid authentication.
#    1. handle expired tokens.
#    2. Handle other APIException
# Usage: python handling_error.py

import json
from functools import wraps

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException, ExpiredTokenException
from cohesity_management_sdk.models.access_token import AccessToken
from samples.list_protection_jobs.list_protection_jobs import ProtectionJobsList
from samples.list_unresolved_alerts.list_unresolved_alerts import Alerts

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
DOMAIN = 'LOCAL'

INVALID_PASSWORD = 'wrong_password'
CLUSTER_VIEWER = 'cluster_viewer'
CLUSTER_VIEWER_PASSWORD = 'cluster_viewer'

AUTH_TOKEN = {
    "accessToken":
        "INVALID_TOKEN",
    "tokenType": "Bearer"}

def handle_invalid_auth(username, password, domain):
    """
    Method to demonstrate invalid auth
    :param username(str): Username of Cohesity cluster user.
    :param password(str): Password of Cohesity cluster user.
    :return None:
    """
    print ("Init client with username: {0}, password: {1}".format(username, password))
    cohesity_client = init_client(username, password, domain)

    try:
        ProtectionJobsList().display_protection_jobs(cohesity_client)
        print ("\n\n *** List Protection Jobs successful ***\n\n")
    except APIException as ex:
        if json.loads(ex.context.response.raw_body)['errorCode'] == 'KValidationError':
            print ("\n\n *** Invalid Username/Password ***\n\n")
            handle_invalid_auth(CLUSTER_USERNAME,
                                CLUSTER_PASSWORD,
				                DOMAIN)

def init_client(username, password, domain):
    """
    Method to initialize the cohesity client.
    :param username(str): Username of Cohesity cluster user.
    :param password(str): Password of Cohesity cluster user.
    :return None:
    """
    return CohesityClient(cluster_vip=CLUSTER_VIP,
                          username=username,
                          password=password,
			  domain=domain)

def reinit_token(ExpiredTokenExcept, tries=3):
    def deco_retry(f):
        @wraps(f)
        def func_retry(*args, **kwargs):
            num_tries = tries
            while num_tries > 0:
                try:
                    return f(*args, **kwargs)
                except ExpiredTokenExcept:
                    print ("Expired token , Re-initilize the cohesity client.\n\n")
                    cohesity_client = args[0]
                    cohesity_client.auth.authorize()
                    num_tries -= 1
            return f(*args, **kwargs)
        return func_retry
    return deco_retry

@reinit_token(ExpiredTokenException, tries=3)
def handle_expired_token(cohesity_client):
    """
    Method to demonstrate expired token. Displays 100 more recent alerts
    :param cohesity_client(CohesityClient): Cohesity cluster Client object.
    :return None:
    """
    cohesity_client.config.disable_logging()
    cohesity_client.config.skip_ssl_verification = True
    Alerts().display_alerts(cohesity_client, 10)

def handle_priv_error(cluster_username, cluster_password, domain):
    """
    Method to initialize the cohesity client.
    :param cluster_username(str): Username of Cohesity cluster user.
    :param cluster_password(str): Password of Cohesity cluster user.
    :return None:
    """
    cohesity_client = init_client(cluster_username, cluster_password, domain)
    try:
        cohesity_client.protection_sources.get_download_physical_agent(host_type='kLinux')
    except APIException as ex:
        if json.loads(ex.context.response.raw_body)['errorCode'] == 'KPrivilegeError':
            print ("\n\n*** User Privileges not Sufficient.****\n\n")

def main():

    #Invalid username/password
    handle_invalid_auth(CLUSTER_USERNAME, INVALID_PASSWORD, DOMAIN)

    # Expired token.
    # If token is expired, you'd need to re-init the client
    auth_token = AccessToken.from_dictionary(AUTH_TOKEN)
    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     auth_token=auth_token)
    handle_expired_token(cohesity_client)

    # Insufficient priviledges
    viewer_username = CLUSTER_VIEWER
    viewer_password = CLUSTER_VIEWER_PASSWORD
    domain = 'LOCAL'
    handle_priv_error(viewer_username, viewer_password, domain)

if __name__ == '__main__':
    main()
