## Usage: 
```
python handling_errors.py
```

## Connect to the Cohesity Cluster
First make sure that you are connected to a Cohesity Cluster.
```
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD)
```
Note: Alternatively, you can set the above parameters in cohesity_management_sdk/configuration.py

## Example: Incorrect Username/Password
``` 
    try:
        ProtectionJobsList().display_protection_jobs(cohesity_client)
    except APIException as ex:
        if json.loads(ex.context.response.raw_body)['errorCode'] == 'KValidationError':
            # Handle logging/Error here.
```

## Example: Handle expired Tokens
```
@reinit_token(ExpiredTokenException, tries=3)
def function_to_test(cohesity_client)
    
```


Re-Initializing cohesity client.
```
def init_client(username, password):
    if not username and not password:
        return CohesityClient(cluster_vip=CLUSTER_VIP,
                              username=username, 
                              password=password)
    else:
        client = CohesityClient(cluster_vip=CLUSTER_VIP)
        client.auth.authorize()
        return client
```


## Example: Handle insufficient Privileges.
```
try:
    cohesity_client.protection_sources.get_download_physical_agent(host_type='kLinux')
except APIException as ex:
    if json.loads(ex.context.response.raw_body)['errorCode'] == 'KPrivilegeError':
      # Handle logging/Error here.
```
