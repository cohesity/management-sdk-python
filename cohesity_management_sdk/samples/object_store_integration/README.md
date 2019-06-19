## Usage: 
```
python object_store_integration.py
```
Python example to Get, List, Upload, Download objects and stream them s3 
buckets hosted on cohesity object storage. Primarily using s3 boto3 API 
client in conjuction with cohesity client to show the integration.

## Connect to the Cohesity Cluster
First make sure that you are connected to a Cohesity Cluster.
```python
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD,
                                 domain=DOMAIN)
```
Note: Alternatively, you can set the above parameters in cohesity_management_sdk/configuration.py

## Get the Key and Access ID for s3 initialization.
```python
user = self.cohesity_client.principals.get_users(usernames=CLUSTER_USER)[0]
return user.s_3_access_key_id, user.s_3_secret_key
```
## Initialize AWS Boto3 Client.
```python
session = boto3.session.Session()
s3_client = session.client(
                    service_name='s3',
                    aws_access_key_id=key_id,
                    aws_secret_access_key=secret_access_key,
                    endpoint_url= self._get_s3_url(),
                    verify=False)
```

## Create bucket through cohesity client.
```python
body = View()
body.view_box_id = self._get_storage_domain_id()
body.name = BUCKET_NAME
body.protocol_access = ProtocolAccessEnum.KS3ONLY
self.cohesity_client.views.create_view(body)
```

## Buckets and Objects operations.
```pythonstub
create_bucket()
list_buckets()

upload_file_to_bucket()
list_bucket_objects()
download_file_from_bucket()

delete_file_from_bucket()
delete_bucket()
```

## Example Output
```bash
Bucket test_bucket created on Cohesity.
['test_bucket', 'aws_s3']
Uploaded File file.txt of size 1048576 to Bucket: test_bucket
('Bucket content: ', 'file.txt')
File downloaded to :/path/to/file/download-file.txt
File file.txt deleted from Bucket: test_bucket
Deleted Bucket: test_bucket
```
