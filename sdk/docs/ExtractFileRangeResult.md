# ExtractFileRangeResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **list[int]** |  | [optional] 
**eof** | **bool** | Will be true if start_offset &gt; file length or EOF is reached. This is an alternative to using file_length to determine when entire file is read. Used when fetching from a view. | [optional] 
**error** | [**ErrorProto**](ErrorProto.md) | Success/error status of the operation. | [optional] 
**file_length** | **int** | The total length of the file. This field would be set provided no error had occurred (indicated by error field above). | [optional] 
**start_offset** | **int** | The offset from which data was read. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


