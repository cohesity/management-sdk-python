## Usage 
```
python --job_name "MSSQL-protect us-west-1" --start_time 2019-11-1 --end_time
 2019-11-18 --extend 10
```

## Connect to the Cohesity Cluster
First make sure that you are connected to a Cohesity Cluster.
```
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD,
                                 domain=DOMAIN)
```
## Example
``` 
 body.job_runs.append(UpdateProtectionJobRun())
 body.job_runs[index].job_uid = UniversalId()
 body.job_runs[index].job_uid.cluster_id  = cluster_id
 body.job_runs[index].job_uid.cluster_incarnation_id = incarnation_id
 body.job_runs[index].job_uid.id = job_id
 body.job_runs[index].run_start_time_usecs = run.copy_run[0].run_start_time_usecs
 body.job_runs[index].copy_run_targets = []
 body.job_runs[index].copy_run_targets.append(RunJobSnapshotTarget())
 body.job_runs[index].copy_run_targets[0].days_to_keep = int(extend)
 body.job_runs[index].copy_run_targets[0].mtype = \
            TypeRunJobSnapshotTargetEnum.KLOCAL
 index += 1
 cohesity_client.protection_runs.update_protection_runs(body=body)

```
## Example Output
```
Start Time		                  Status		Success/Error		Extended Snapshot?
Mon Nov 18 14:26:59 2019		  kSuccess		       1/0		       Yes
Mon Nov 18 10:26:59 2019		  kSuccess		       1/0		       Yes
Mon Nov 18 06:26:57 2019		  kSuccess		       1/0		       Yes
Mon Nov 18 02:26:57 2019		  kSuccess		       1/0		       Yes
Sun Nov 17 22:26:56 2019		  kSuccess		       1/0		       Yes
Sun Nov 17 18:26:56 2019		  kSuccess		       1/0		       Yes
Sun Nov 17 14:26:55 2019		  kSuccess		       1/0		       Yes
Sun Nov 17 10:26:55 2019		  kSuccess		       1/0		       Yes
Sun Nov 17 06:26:55 2019		  kSuccess		       1/0		       Yes
Sun Nov 17 02:26:54 2019		  kSuccess		       1/0		       Yes
Sat Nov 16 22:26:53 2019		  kSuccess		       1/0		       Yes
Sat Nov 16 18:26:52 2019		  kSuccess		       1/0		       Yes
Sat Nov 16 14:26:51 2019		  kSuccess		       1/0		       Yes
Sat Nov 16 10:26:51 2019		  kSuccess		       1/0		       Yes
Sat Nov 16 06:26:51 2019		  kSuccess		       1/0		       Yes
Sat Nov 16 02:26:51 2019		  kSuccess		       1/0		       Yes
Fri Nov 15 22:26:51 2019		  kSuccess		       1/0		       Yes
Fri Nov 15 18:26:51 2019		  kSuccess		       1/0		       Yes
Fri Nov 15 14:26:51 2019		  kSuccess		       1/0		       Yes
Fri Nov 15 10:26:50 2019		  kSuccess		       1/0		       Yes
Fri Nov 15 06:26:49 2019		  kSuccess		       1/0		       Yes
Fri Nov 15 02:26:49 2019		  kSuccess		       1/0		       Yes
Thu Nov 14 22:26:49 2019		  kSuccess		       1/0		       Yes
Thu Nov 14 18:26:48 2019		  kSuccess		       1/0		       Yes
Thu Nov 14 14:26:48 2019		  kSuccess		       1/0		       Yes
Thu Nov 14 10:26:47 2019		  kSuccess		       1/0		       Yes
Thu Nov 14 06:26:47 2019		  kSuccess		       1/0		       Yes
Thu Nov 14 02:26:46 2019		  kSuccess		       1/0		       Yes
Wed Nov 13 22:26:45 2019		  kSuccess		       1/0		       Yes
Wed Nov 13 18:26:44 2019		  kSuccess		       1/0		       Yes
Wed Nov 13 14:26:44 2019		  kSuccess		       1/0		       Yes
Wed Nov 13 10:26:44 2019		  kSuccess		       1/0		       Yes
Wed Nov 13 06:26:44 2019		  kSuccess		       1/0		       Yes
Wed Nov 13 02:26:44 2019		  kSuccess		       1/0		       Yes
Tue Nov 12 22:26:44 2019		  kSuccess		       1/0		       Yes
Tue Nov 12 18:26:44 2019		  kSuccess		       1/0		       Yes
Tue Nov 12 14:26:43 2019		  kSuccess		       1/0		       Yes
Tue Nov 12 10:26:43 2019		  kSuccess		       1/0		       Yes
Tue Nov 12 06:26:43 2019		  kSuccess		       1/0		       Yes
Tue Nov 12 02:26:43 2019		  kSuccess		       1/0		       Yes
Mon Nov 11 22:26:42 2019		  kSuccess		       1/0		       Yes
Mon Nov 11 18:26:42 2019		  kSuccess		       1/0		       Yes
Mon Nov 11 14:26:42 2019		  kSuccess		       1/0		       Yes
Mon Nov 11 10:26:41 2019		  kSuccess		       1/0		       Yes
Mon Nov 11 06:26:41 2019		  kSuccess		       1/0		       Yes
Mon Nov 11 02:26:41 2019		  kSuccess		       1/0		       Yes
Sun Nov 10 22:26:41 2019		  kSuccess		       1/0		       Yes
Sun Nov 10 18:26:41 2019		  kSuccess		       1/0		       Yes
Sun Nov 10 14:26:40 2019		  kSuccess		       1/0		       Yes
Sun Nov 10 10:26:40 2019		  kSuccess		       1/0		       Yes
Sun Nov 10 06:26:39 2019		  kSuccess		       1/0		       Yes
Sun Nov 10 02:26:39 2019		  kSuccess		       1/0		       Yes
Sat Nov  9 22:26:38 2019		  kSuccess		       1/0		       Yes
Sat Nov  9 18:26:37 2019		  kSuccess		       1/0		       Yes
Sat Nov  9 14:26:37 2019		  kSuccess		       1/0		       Yes
Sat Nov  9 10:26:37 2019		  kSuccess		       1/0		       Yes
Sat Nov  9 06:26:37 2019		  kSuccess		       1/0		       Yes
Sat Nov  9 02:26:37 2019		  kSuccess		       1/0		       Yes
Fri Nov  8 22:26:36 2019		  kSuccess		       1/0		       Yes
Fri Nov  8 18:26:35 2019		  kSuccess		       1/0		       Yes
Fri Nov  8 14:26:35 2019		  kSuccess		       1/0		       Yes
Fri Nov  8 10:26:34 2019		  kSuccess		       1/0		       Yes
Fri Nov  8 06:26:33 2019		  kSuccess		       1/0		       Yes
Fri Nov  8 02:26:32 2019		  kSuccess		       1/0		       Yes
Thu Nov  7 22:26:32 2019		  kSuccess		       1/0		       Yes
Thu Nov  7 18:26:32 2019		  kSuccess		       1/0		       Yes
Thu Nov  7 14:26:32 2019		  kSuccess		       1/0		       Yes
Thu Nov  7 10:26:32 2019		  kSuccess		       1/0		       Yes
Thu Nov  7 06:26:32 2019		  kSuccess		       1/0		       Yes
Thu Nov  7 02:26:31 2019		  kSuccess		       1/0		       Yes
Wed Nov  6 22:26:31 2019		  kSuccess		       1/0		       Yes
Wed Nov  6 18:26:30 2019		  kSuccess		       1/0		       Yes
Wed Nov  6 14:26:29 2019		  kSuccess		       1/0		       Yes
Wed Nov  6 10:26:29 2019		  kSuccess		       1/0		       Yes
Wed Nov  6 06:26:28 2019		  kSuccess		       1/0		       Yes
Wed Nov  6 02:26:28 2019		  kSuccess		       1/0		       Yes
Tue Nov  5 22:26:28 2019		  kSuccess		       1/0		       Yes
Tue Nov  5 18:26:27 2019		  kSuccess		       1/0		       Yes
Tue Nov  5 14:26:26 2019		  kSuccess		       1/0		       Yes
Tue Nov  5 10:26:25 2019		  kSuccess		       1/0		       Yes
Tue Nov  5 06:26:25 2019		  kSuccess		       1/0		       Yes
Tue Nov  5 02:26:24 2019		  kSuccess		       1/0		       Yes
Mon Nov  4 22:26:23 2019		  kSuccess		       1/0		       Yes
Mon Nov  4 18:26:22 2019		  kSuccess		       1/0		       Yes
Mon Nov  4 14:26:21 2019		  kSuccess		       1/0		       Yes
Mon Nov  4 10:26:20 2019		  kSuccess		       1/0		       Yes
Mon Nov  4 06:26:19 2019		  kSuccess		       1/0		       Yes
Mon Nov  4 02:26:19 2019		  kSuccess		       1/0		       Yes
Sun Nov  3 22:26:18 2019		  kSuccess		       1/0		       Yes
Sun Nov  3 18:26:18 2019		  kSuccess		       1/0		       Yes
Sun Nov  3 14:26:17 2019		  kSuccess		       1/0		       Yes
Sun Nov  3 10:26:17 2019		  kSuccess		       1/0		       Yes
Sun Nov  3 06:26:16 2019		  kSuccess		       1/0		       Yes
Sun Nov  3 02:26:15 2019		  kSuccess		       1/0		       Yes
Sat Nov  2 23:26:15 2019		  kSuccess		       1/0		       Yes
Sat Nov  2 19:26:15 2019		  kSuccess		       1/0		       Yes
Sat Nov  2 15:26:14 2019		  kSuccess		       1/0		       Yes
Sat Nov  2 11:26:13 2019		  kSuccess		       1/0		       Yes
Sat Nov  2 03:26:11 2019		  kSuccess		       1/0		       Yes
Fri Nov  1 03:26:08 2019		  kSuccess		       1/0		       Yes

```

