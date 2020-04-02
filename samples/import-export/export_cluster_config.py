import os
import shutil
from rest_client import RestClient
rest_client = RestClient.get_instance(conf_type="export")

# Get the current working directory.
cwd = os.getcwd()

config_file_dir = os.path.join(cwd, "cluster_config")
protect_policy_json_file = os.path.join(config_file_dir, "protection_policies.json")
storage_domain_json_file = os.path.join(config_file_dir, "storage_domains.json")
protect_job_json_file = os.path.join(config_file_dir, "protection_jobs.json")
protect_source_json_file = os.path.join(config_file_dir, "protection_sources.json")
external_targets_json_file = os.path.join(config_file_dir, "external_targets.json")

# Check for already available config files folder, if found delete the folder
# and its contents.
if os.path.isdir(config_file_dir):
    shutil.rmtree(config_file_dir)
os.makedirs(config_file_dir)

def get_protection_policies():
    """
    Fetches the protection policies available in the cluster and save the response
    to  a json file.
    """
    code, cont = rest_client.get("protectionPolicies")
    if code == 200:
        with open(protect_policy_json_file, "w") as file_obj:
            file_obj.write(cont.decode("utf-8"))
    else:
        print("Failure while fetching protection policies")
        exit()


def get_protection_jobs():
    code, cont = rest_client.get("protectionJobs")
    if code == 200:
        with open(protect_job_json_file, "w") as file_obj:
            file_obj.write(cont.decode("utf-8"))
    else:
        print("Failure while fetching protection Jobs.")
        exit()

def get_storage_domains():
    code, cont = rest_client.get("viewBoxes")
    if code == 200:
        with open(storage_domain_json_file, "w") as file_obj:
            file_obj.write(cont.decode("utf-8"))
    else:
        print("Failure while fetching storage domains.")
        exit()


def get_protection_sources():
    code, cont = rest_client.get("protectionSources?allUnderHierarchy=false&environments=kVMware,kAzure,kPhysical,kGenericNas&excludeTypes="\
    "kVCenter,kFolder,kDatacenter,kComputeResource,kClusterComputeResource,kResourcePool,kDatastore,kHostSystem,kVirtualApp,kStandaloneHost,kStoragePod,kNetwork,kDistributedVirtualPortgroup,kTagCategory,kTag")
    print(code, cont)
    if code == 200:
        with open(protect_source_json_file, "w") as file_obj:
            file_obj.write(cont.decode("utf-8"))
    else:
        print("Failure while fetching protection sources.")
        exit()

def get_external_targets():
    code, cont = rest_client.get("vaults")
    if code == 200:
        with open(external_targets_json_file, "w") as file_obj:
            file_obj.write(cont.decode("utf-8"))
    else:
        print("Failure while fetching external targets.")
        exit()

get_storage_domains()
get_protection_policies()
get_protection_jobs()
get_protection_sources()
get_external_targets()