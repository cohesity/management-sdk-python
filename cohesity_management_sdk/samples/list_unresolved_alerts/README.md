## Usage: 
```
python list_unresolved_alerts.py --max_alerts 10
```

## Connect to the Cohesity Cluster
First make sure that you are connected to a Cohesity Cluster.
```
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD,
                                 domain=DOMAIN)
```
Note: Alternatively, you can set the above parameters in cohesity_management_sdk/configuration.py

## Example
``` 
alerts= cohesity_client.alerts
alerts_list = alerts.get_alerts(max_alerts=max_alerts, alert_state_list=AlertStateListEnum.KOPEN)
```


## Example Output
```
01-01-2019 15:27:25              CLUSTER              INFO
01-01-2019 15:39:16             NODE_HEALTH        WARNING

```
