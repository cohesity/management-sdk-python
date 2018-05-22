# VaultEncryptionKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | Specifies the name of the source Cohesity Cluster that archived the data on the Vault. | [optional] 
**encryption_key_data** | **str** | Specifies the encryption key data corresponding to the specified keyUid. It contains a Key Encryption Key (KEK) or a Encrypted Data Encryption Key (eDEK). | [optional] 
**key_uid** | [**VaultEncryptionKeyKeyUid**](VaultEncryptionKeyKeyUid.md) |  | [optional] 
**vault_id** | **int** | Specifies the id of the Vault whose data is encrypted by this key. | [optional] 
**vault_name** | **str** | Specifies the name of the Vault whose data is encrypted by this key. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


