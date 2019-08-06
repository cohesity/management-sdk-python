# Requirements
* Python 2 >=2.7.9 or Python 3 >=3.4.
* Access to Cluster APIs from the machine this script is running.
* NFS shares accessible to cluster.
* pip has to be installed. 

# Install Python Requirements
```
pip install -r requirements.txt
```

# Backup the views

Make sure the config.ini is populated correctly with nfs exports data
and cohesity cluster config.

Required fields in config.ini:
```
[nas_export_list]
nas_export1=<server-fqdn.com:/nas-share1>
nas_export2=<server-ip:/nas-share2> #you can Add 'n' number of shares here.

[cohesity]
cluster_vip=<cluster_vip>
username=<cluster_username>
password=<cluster_password>
domain=LOCAL
policy=<Backup-policy-name>           
job_name_prefix=<backup-job-prefix-> 
storage_domain=<Storage domain name>
```
Note: 1 Job per nas share will start with name <job_name_prefix-{nas-name}> ,
in this example: backup-job-prefix-nas-share1

Run script:
```python

python backup_nas_to_cohesity.py
```

# Create views from Backup

After the NAS has backed up sufficiently. 
Make sure the config.ini is populated correctly and 
the protection job is prefixed correctly in config.ini, especially 
nfs_target_qos, storage_domain

Required fileds in config.ini:
```
[cohesity]
cluster_vip=<cluster_vip>
username=<cluster_username>
password=<cluster_password>
domain=LOCAL
#Choose from: ['TestAndDev High’, 'Backup Target SSD’, ‘Backup Target High’, 
'TestAndDev Low', 'Backup Target Low’]
nfs_target_qos=Backup Target High
#Storage Domain where the view will be created.
storage_domain=<Storage Domain of the View>
```
Run script:
```python
python create_nas_from_backup.py --job_name NAS-Protect-Nas-server
--cohesity_nfs_name cohesity_nas
```

# Update nfs whitelist 
This is a generic script, this will whitelist the IPs to access the view. 
nfs_access, nfs_root_squash are optional parameters. 

Required fields in config.ini:
```
[cohesity]
cluster_vip=<cluster_vip>
username=<cluster_username>
password=<cluster_password>
domain=LOCAL
```

```python
python update_nfs_whitelist.py --nfs_share_name cohesity_nas --whitelist_ip 10.2.2.3 --whitelist_netmask 255.255.252.0 

Help:
  --whitelist_ip WHITELIST_IP
                        IP to whitelist Eg: 10.0.0.1
  --nfs_share_name NFS_SHARE_NAME
                        Name of Cohesity NFS/View
  --whitelist_netmask WHITELIST_NETMASK
                        Netmask to whitelist Eg: 255.255.252.0
  --nfs_access NFS_ACCESS
                        Choose between: [kDisabled,kReadOnly,kReadWrite]
                        Defaults to : kReadWrite
                        Specifies whether clients from this subnet can mount
                        using NFS protocol.
  --nfs_root_squash NFS_ROOT_SQUASH Choose between: [True, False]
                        Defaults: False
                        Specifies whether clients from this subnet can mount
                        as root on NFS.
```


