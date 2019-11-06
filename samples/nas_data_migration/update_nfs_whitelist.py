# Copyright 2019 Cohesity Inc.
#
# Usage: python update_nfs_whitelist.py --nfs_share_name cohesity_nas --whitelist_ip 10.2.2.3 --whitelist_netmask 255.255.252.0

import argparse
import configparser


from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.update_view_param import UpdateViewParam
from cohesity_management_sdk.models.protocol_access_enum import ProtocolAccessEnum
from cohesity_management_sdk.models.subnet import Subnet
from cohesity_management_sdk.exceptions.api_exception import APIException


parser = configparser.ConfigParser()
parser.read('config.ini')
CLUSTER_VIP = parser.get('cohesity', 'cluster_vip')
CLUSTER_USERNAME = parser.get('cohesity', 'username')
CLUSTER_PASSWORD = parser.get('cohesity', 'password')
DOMAIN = parser.get('cohesity', 'domain')
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				                     domain=DOMAIN)
cohesity_client.config.disable_logging()

def update_view_whitelist(args):
    body = UpdateViewParam()
    body.protocol_access = ProtocolAccessEnum.KNFSONLY
    body.subnet_whitelist = []
    body.subnet_whitelist.append(Subnet())
    body.subnet_whitelist[0].ip = args.whitelist_ip
    body.subnet_whitelist[0].netmask_ip_4 = args.whitelist_netmask
    body.subnet_whitelist[0].nfs_access = args.nfs_access
    body.subnet_whitelist[0].nfs_root_squash = args.nfs_root_squash
    try:
        cohesity_client.views.update_view_by_name(name=args.nfs_share_name,
                                                  body=body)
    except APIException as ex:
        print("Failed to update %s , reason: %s" % (args.nfs_share_name,
                                                  ex.message))
        exit(1)

    print("Updated the NFS share: %s successfully." % args.nfs_share_name)

def main(args):

    update_view_whitelist(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Arguments needed to run this python script.")
    parser.add_argument("--whitelist_ip", help="IP to whitelist Eg: 10.0.0.1",
                        required=True)
    parser.add_argument("--nfs_share_name", help="Name of Cohesity NFS/View",
                        required=True)
    parser.add_argument("--whitelist_netmask",
                        help="Netmask to whitelist Eg: 255.255.252.0",
                        required=True)
    parser.add_argument("--nfs_access",
                        help="Choose between: [kDisabled,kReadOnly,kReadWrite]"
                             "Defaults to : kReadWrite"
                             "Specifies whether clients from this "
                             "subnet can mount using NFS protocol.",
                        required=False,
                        default='kReadWrite')
    parser.add_argument("--nfs_root_squash",
                        help="Specifies whether clients from this subnet can mount as root on NFS."
                             "Choose between: [True, False] Defaults: False",
                        required=False,
                        default=False, type=bool)

    args = parser.parse_args()
    main(args)
