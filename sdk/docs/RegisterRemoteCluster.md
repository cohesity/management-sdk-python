# RegisterRemoteCluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_endpoints_reachable** | **bool** | Specifies whether any endpoint (such as a Node) on the remote Cluster is reachable from this local Cluster. If true, a service running on the local Cluster can communicate directly with any of its peers running on the remote Cluster, without using a proxy. | [optional] 
**bandwidth_limit** | [**BandwidthLimit**](BandwidthLimit.md) | Specifies settings for limiting the data transfer rate between the local and remote Clusters. | [optional] 
**clear_interfaces** | **bool** |  | [optional] 
**clear_vlan_id** | **bool** | Specifies whether to clear the vlanId field, and thus stop using only the IPs in the VLAN for communicating with the remote Cluster. | [optional] 
**cluster_id** | **int** | Specifies the unique id of the remote Cluster. | [optional] 
**compression_enabled** | **bool** | Specifies whether to compress the outbound data when transferring the replication data over the network to the remote Cluster. | [optional] 
**encryption_key** | **str** | Specifies the encryption key used for encrypting the replication data from a local Cluster to a remote Cluster. If a key is not specified, replication traffic encryption is disabled. When Snapshots are replicated from a local Cluster to a remote Cluster, the encryption key specified on the local Cluster must be the same as the key specified on the remote Cluster. | [optional] 
**network_interface_group** | **str** | Specifies the group name of the network interfaces to use for communicating with the remote Cluster. | [optional] 
**network_interface_ids** | **list[int]** | Specifies the ids of the network interfaces to use for communicating with the remote Cluster. | [optional] 
**password** | **str** | Specifies the password for Cohesity user to use when connecting to the remote Cluster. | [optional] 
**purpose_remote_access** | **bool** | Whether the remote cluster will be used for remote access for SPOG. | [optional] 
**purpose_replication** | **bool** | Whether the remote cluster will be used for replication. | [optional] 
**remote_access_credentials** | [**AccessTokenCredential**](AccessTokenCredential.md) | Optional field for the user credentials to connect to Iris for remote access for SPOG. If this is not specified, then credentials specified for replication set up will be used for remote access for SPOG. Allowing a different user credentials to be set up for SPOG permits having different roles for remote access for SPOG and replication set up. | [optional] 
**remote_ips** | **list[str]** | Specifies the IP addresses of the Nodes on the remote Cluster to connect with. These IP addresses can also be VIPS. Specifying hostnames is not supported. | [optional] 
**remote_iris_ports** | **list[int]** | Specifies the ports to use when connecting to the Nodes of the remote Cluster. | [optional] 
**user_name** | **str** | Specifies the Cohesity user name used to connect to the remote Cluster. | [optional] 
**validate_only** | **bool** | Whether to only validate the credentials without saving the information. | [optional] 
**view_box_pair_info** | [**list[ViewBoxPairInfo]**](ViewBoxPairInfo.md) | Specifies pairings between Storage Domains (View Boxes) on the local Cluster with Storage Domains (View Boxes) on a remote Cluster that are used in replication. | [optional] 
**vlan_id** | **int** | Specifies the Id of the VLAN to use for communicating with the remote Cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


