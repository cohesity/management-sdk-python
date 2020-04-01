import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.controllers.views_controller import ViewsController


# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=configparser.get('cohesity', 'host_ip'),
                                 username=configparser.get('cohesity', 'username'),
                                 password=configparser.get('cohesity', 'password'),
                                 domain= configparser.get('cohesity', 'domain'))

# Get the view details
def get_views():
    class_obj = ViewsController()
    views = class_obj.get_views().views
    views_list = []
    if not views:
        print("No views available in the cluster.")
        return
    for view in views:
        view_obj = {}
        stats = {}
        logical_quota = {}
        nfs_all_squash = {}
        nfs_root_squash = {}
        if view.logical_quota:
            logical_quota["hard_limit_bytes"] = view.logical_quota.hard_limit_bytes
            logical_quota["alert_limit_bytes"] = view.logical_quota.alert_limit_bytes
            logical_quota["alert_threshold_percentage"] = view.logical_quota.alert_threshold_percentage

        if view.stats:
            stats["id"] = view.stats.id

        if view.nfs_root_squash:
            nfs_root_squash["uid"] = view.nfs_root_squash.uid
            nfs_root_squash["gid"] = view.nfs_root_squash.gid

        if view.nfs_all_squash:
            nfs_all_squash["uid"] = view.nfs_all_squash.uid
            nfs_all_squash["gid"] = view.nfs_all_squash.gid

        #print(view_obj);break
        view_obj["stats"] = stats
        view_obj["logical_quota"] = logical_quota
        view_obj["nfs_all_squah"] = nfs_all_squash
        view_obj["nfs_root_squah"] = nfs_root_squash
        view_obj['basic_mount_path'] = view.basic_mount_path
        view_obj['case_insensitive_names_enabled'] = view.case_insensitive_names_enabled
        view_obj['create_time_msecs'] = view.create_time_msecs
        view_obj['data_lock_expiry_usecs'] = view.data_lock_expiry_usecs
        view_obj['description'] = view.description
        view_obj['enable_filer_audit_logging'] = view.enable_filer_audit_logging
        view_obj['enable_mixed_mode_permissions'] = view.enable_mixed_mode_permissions
        view_obj['enable_nfs_view_discovery'] = view.enable_nfs_view_discovery
        view_obj['enable_offline_caching'] = view.enable_offline_caching
        view_obj['enable_smb_access_based_enumeration'] = view.enable_smb_access_based_enumeration
        view_obj['enable_smb_encryption'] = view.enable_smb_encryption
        view_obj['enable_smb_view_discovery'] = view.enable_smb_view_discovery
        view_obj['enforce_smb_encryption'] = view.enforce_smb_encryption
        view_obj['is_target_for_migrated_data'] = view.is_target_for_migrated_data
        view_obj['logical_usage_bytes'] = view.logical_usage_bytes
        view_obj['name'] = view.name
        view_obj['nfs_mount_path'] = view.nfs_mount_path
        view_obj['override_global_whitelist'] = view.override_global_whitelist
        view_obj['protocol_access'] = view.protocol_access
        view_obj['s_3_access_path'] = view.s_3_access_path
        view_obj['s_3_key_mapping_config'] = view.s_3_key_mapping_config
        view_obj['security_mode'] = view.security_mode
        view_obj['smb_mount_path'] = view.smb_mount_path
        view_obj['storage_policy_override'] = view.storage_policy_override
        view_obj['view_box_id'] = view.view_box_id
        view_obj['view_box_name'] = view.view_box_name
        view_obj['view_id'] = view.view_id
        view_obj['view_protection'] = view.view_protection
        views_list.append(view_obj)
    print(views_list)
get_views()