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
from cohesity_management_sdk.samples.list_protection_jobs import ProtectionJobsList
from cohesity_management_sdk.samples.list_unresolved_alerts import Alerts

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
INVALID_PASSWORD = 'wrong_password'
CLUSTER_VIEWER = 'cluster_viewer'
CLUSTER_VIEWER_PASSWORD = 'cluster_viewer_password'

AUTH_TOKEN = {
    "accessToken":
        "eyzI1NiIsInR5cCI6IkpXVCJ9.eyJkb21haW4iOiJMT0NBTCIsImV4cGlyYXRpb24tdGl"
        "tZSI6IjE1NDc5NTI0MjkiLCJzaWRzLWhhc2giOiJmaGgzSmY4VWZwODJwM3lKb09jMzl"
        "JM1p6TTJZZUFJMldjX0kyY2p5SEtZIiwidGVuYW50LWlkIjoiIiwidXNlci1zaWQiOiJTL"
        "TEtMTAwLTIxLTcwMTYwMjMtNDU2MjMxMzAtMSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.N4f5"
        "lTwS-GwcwFUsp3jSY2M-r8a5KGjp9Kw-3gHujDAvvZSBUSQ1eEefkd5Tr-tg3zeBxuKGkq"
        "sYrnl4NMT8W0gVwZJBicE_QjT1oHhzsLobV5q82CWKUAHqlqWfQasAGn_QEY8_cqMUlciH"
        "v1DSCxSNS34fBuaHzhTiYouAkI7jbw6Zj4Ed_cuCfJHwb8S6e9DaeHq6-CTa4AGRDdaHY8"
        "0o1pqUBri4fNTCDkxgSzYM-LJ3SENLFLpMKwvo8g4d84mvDzvg7UG6Pai02k6i_m9PTvE_"
        "H2D3p3cvso2wKGN9V1Wgjy2fXt0bFRa5NbqZsLM-xgdXzEMBoZBzS_npFw",
    "tokenType": "Bearer"}
def handle_invalid_auth(username, password):
    """
    Method to demonstrate invalid auth
    :param username(str): Username of Cohesity cluster user.
    :param password(str): Password of Cohesity cluster user.
    :return None:
    """
    print ("Init client with username: {0}, password: {1}".format(username, password))
    cohesity_client = init_client(username, password)
    cohesity_client.config.cluster_vip = CLUSTER_VIP
    cohesity_client.config.disable_logging()
    cohesity_client.config.skip_ssl_verification = True
    try:
        ProtectionJobsList().display_protection_jobs(cohesity_client)
        print ("\n\n *** List Protection Jobs successful ***\n\n")
    except APIException as ex:
        if json.loads(ex.context.response.raw_body)['errorCode'] == 'KValidationError':
            print ("\n\n *** Invalid Username/Password ***\n\n")
            handle_invalid_auth(CLUSTER_USERNAME, CLUSTER_PASSWORD)

def init_client(username, password):
    """
    Method to initialize the cohesity client.
    :param username(str): Username of Cohesity cluster user.
    :param password(str): Password of Cohesity cluster user.
    :return None:
    """
    if username and password:
        return CohesityClient(username=username, password=password)
    else:
        client = CohesityClient()
        client.auth.authorize()
        return client

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
    cohesity_client.config.cluster_vip = CLUSTER_VIP
    cohesity_client.config.disable_logging()
    cohesity_client.config.skip_ssl_verification = True
    Alerts().display_alerts(cohesity_client, 100)

def handle_priv_error(cluster_username, cluster_password):
    """
    Method to initialize the cohesity client.
    :param cluster_username(str): Username of Cohesity cluster user.
    :param cluster_password(str): Password of Cohesity cluster user.
    :return None:
    """
    cohesity_client = init_client(cluster_username, cluster_password)
    try:
        cohesity_client.protection_sources.get_download_physical_agent(host_type='kLinux')
    except APIException as ex:
        if json.loads(ex.context.response.raw_body)['errorCode'] == 'KPrivilegeError':
            print ("\n\n*** User Privileges not Sufficient.****\n\n")

def main():

    #Invalid username/password
    handle_invalid_auth(CLUSTER_USERNAME, INVALID_PASSWORD)

    # Expired token.
    # If token is expired, you'd need to re-init the client
    auth_token = AccessToken.from_dictionary(AUTH_TOKEN)
    cohesity_client = CohesityClient(auth_token=auth_token)
    handle_expired_token(cohesity_client)

    # Insufficient priviledges
    viewer_username = CLUSTER_VIEWER
    viewer_password = CLUSTER_VIEWER_PASSWORD
    handle_priv_error(viewer_username, viewer_password)

if __name__ == '__main__':
    main()