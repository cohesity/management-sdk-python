import os
import json

from rest_client import RestClient
rest_client = RestClient.get_instance(conf_type="import")


def create_protection_policy():
    """
    """
    json_body = {
    "name": "TestPolicy",
    "incrementalSchedulingPolicy": {
        "periodicity": "kMonthly",
        "monthlySchedule": {
        "dayCount": "kFirst",
        "day": "kSunday"
        }
    },
    "daysToKeep": 90,
    "retries": 3,
    "retryIntervalMins": 30,
    "blackoutPeriods": [],
    "extendedRetentionPolicies": [],
    "snapshotReplicationCopyPolicies": [],
    "snapshotArchivalCopyPolicies": [],
    "cloudDeployPolicies": []
    }
    code, cont = rest_client.post("protectionPolicies", data=json.dumps(json_body))
    if code == 201:
        print("ProtectionPolicy is created successfully.")
    else:
        print("Failure while creating new protection policy.")
        err_msg = json.loads(cont.decode("utf-8"))["message"]
        print(err_msg)
        #exit()


def create_storage_domain():
    # For creating storage domain we need cluster partition id and requires
    # another API call. Also deleting storage domain option is not available.
    json_body = {
        "name": "DemoSD",
        "clusterPartitionId": 3,
        "storagePolicy": {
            "deduplicationEnabled": True,
            "inlineDeduplicate": True,
            "compressionPolicy": "kCompressionLow",
            "inlineCompress": True,
            "encryptionPolicy": "kEncryptionNone",
            "erasureCodingInfo": {
            "erasureCodingEnabled": False
            },
            "numFailuresTolerated": 0,
            "numNodeFailuresTolerated": 0
        },
        "s3BucketsAllowed": False,
        "adDomainName": None,
        "nisDomainNameVec": None,
        "ldapProviderId": None,
        "clusterPartitionName": "DuplicateDefaultPartition",
        "removalState": "kDontRemove",
        "IsRecommended": None
        }
    code, cont = rest_client.post("viewBoxes", data=json.dumps(json_body))
    if code == 201:
        print("Storage domain is created successfully.")
    else:
        print("Failure while creating storage domain.")
        exit()

create_protection_policy()
#create_storage_domain()