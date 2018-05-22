# CreateViewBoxParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_domain_name** | **str** | Specifies an active directory domain that this view box is mapped to. | [optional] 
**cluster_partition_id** | **int** | Specifies the Cluster Partition id where the Storage Domain (View Box) is located. | 
**default_user_quota_policy** | [**CreateViewBoxParamsDefaultUserQuotaPolicy**](CreateViewBoxParamsDefaultUserQuotaPolicy.md) |  | [optional] 
**default_view_quota_policy** | [**CreateViewBoxParamsDefaultViewQuotaPolicy**](CreateViewBoxParamsDefaultViewQuotaPolicy.md) |  | [optional] 
**name** | **str** | Specifies the name of the Storage Domain (View Box). | 
**physical_quota** | [**CreateViewBoxParamsPhysicalQuota**](CreateViewBoxParamsPhysicalQuota.md) |  | [optional] 
**s3_buckets_allowed** | **bool** | Specifies whether creation of a S3 bucket is allowed in this Storage Domain (View Box). When a new S3 bucket creation request arrives, we&#39;ll look at all the View Boxes and the first Storage Domain (View Box) that allows creating S3 buckets in it will be the one where the bucket will be placed. | [optional] 
**storage_policy** | [**StoragePolicy**](StoragePolicy.md) | Specifies the storage options applied to the Storage Domain (View Box). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


