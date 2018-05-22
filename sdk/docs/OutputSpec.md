# OutputSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_reduce_shards** | **int** | Number of reduce shards. | [optional] 
**output_dir** | **str** | Name of output directory. | [optional] 
**partition_id** | **int** | Partition id where output will go. | [optional] 
**reduce_output_prefix** | **str** | Prefix of the reduce output files. File names will be: ${reduce_output_prefix}-00000-of-00100 if num_reduce_shards&#x3D;100 This name can contain some path components. e.g. \&quot;awb_results/run1\&quot; is a valid value. output_dir is deprecated. | [optional] 
**view_box_id** | **int** | Viewbox id where the output will go. | [optional] 
**view_name** | **str** | Name of the view where output will go. This will be filled up by yoda. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


