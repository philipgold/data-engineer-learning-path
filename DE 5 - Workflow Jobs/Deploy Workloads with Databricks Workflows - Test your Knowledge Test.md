# Deploy Workloads with Databricks Workflows - Test your Knowledge Test

#### Test 1
A data engineering team has been using a Databricks SQL query to monitor the performance of an ELT job. The ELT job is triggered when a specific number of input records are ready to be processed. The Databricks SQL query returns the number of records added since the job’s most recent runtime. The team has manually reviewed some of the records and knows that at least one of them will be successfully processed without violating any constraints.

Which of the following approaches can the data engineering team use to be notified if the ELT job did not complete successfully? Select one response.

- They can set up an alert for the job to notify them when a record has been flagged as invalid.
- This type of alerting is not possible in Databricks.
- They can set up an alert for the job to notify them when a constraint has been violated.
- They can set up an alert for the job to notify them when a record has been added to the target dataset.
- They can set up an alert for the job to notify them if the returned value of the SQL query is less than 1.

#### Test 2 
Which of the following tools can be used to create a Databricks Job? Select three responses.

- External Git repository
- Jobs REST API
- Databricks CLI
- Data Explorer
- Job Scheduler UI

#### Test 3

A data engineer has a job that creates and displays a result set of baby names by year, where each row has a unique year. They want to display the results for baby names from the past three years only.

Which of the following approaches allows them to filter rows from the table by year? Select one response.

They can add a filter condition to the job’s configuration.

They can add an import statement to input the year.

They can edit the table to remove certain rows in the Job Details page.

They can add widgets to the notebook and re-run the job.

They can re-run the job with new parameters for the task.

#### Test 4

A data engineer needs to view the metadata concerning the order that events in a DLT pipeline were executed.

Which of the following steps can the data engineer complete to view this information? Select one response.

- The data engineer can query the metrics column of the event log for DLT metrics
- The data engineer can view the DLT metrics from the bar graph that is generated within the notebook.
- The data engineer can view the DLT metrics from the Pipeline Details page.
- The data engineer can view the DLT metrics from the resultant Directed Acyclic Graph (DAG).
- The data engineer can query the event log from a new notebook.

#### Test 5
A data engineer needs to view whether each task within a job run succeeded.

Which of the following steps can the data engineer complete to view this information? Select one response.

- They can review job run output from the resultant directed acyclic graph (DAG).
- They can review the job run history from the Workflow Details page.
- They can review the task output from the notebook commands.
- They can review the task history by clicking on each task in the workflow.
- They can review the job run history from the Job run details page.

#### Test 6

Which of the following statements about the advantages of using Workflows for task orchestration are correct? Select three responses.

- Workflows supports built-in data quality constraints for logging purposes.
- Workflows can be used to make external API calls.
- Workflows is fully managed, which means users do not need to worry about infrastructure.
- Workflows provides a centralized repository for data visualization tools.
- Workflows can be configured to use external access control permissions.


#### Test 7

Which of the following workloads can be configured using Databricks Workflows? Select three responses.

- An ETL job with batch and streaming data
- A job with Python, SQL, and Scala tasks
- A data analysis job that uses R notebooks
- A custom task where data is extracted from a JAR file
- A job running on a triggered schedule with dependent tasks

#### Test 8

A data engineer is using Workflows to run a multi-hop (medallion) ETL workload. They notice that the workflow will not complete because one of the tasks is failing.

Which of the following describes the order of execution when running the repair tool? Select one response.

The data engineer can use the repair feature to re-run only the failed task and the task it depends on.

The data engineer can use the repair feature to re-run only the sub-tasks of the failed task.

The data engineer can use the repair feature to re-run only the failed task and sub-tasks.

The data engineer can use the repair feature to re-run only the failed task and the tasks following it.

The data engineer can use the repair feature to re-run only the failed sub-tasks.

Single Choice

#### Test 9

A data engineer has a workload that includes transformations of batch and streaming data, with built-in constraints to ensure each record meets certain conditions.

Which of the following task types is considered best practice for the data engineer to use to configure this workload? Select one response.

- dbt
- Notebook
- Spark submit
- Python script
- Delta Live Tables pipeline
- Multiple Choice

#### Test 10

Which of the following components are necessary to create a Databricks Workflow? Select three responses.

- Tasks
- Experiment
- Cluster
- Alert
- Schedule


#### Test 11

A data engineer is running multiple notebooks that are triggered on different job schedules. Each notebook is part of a different task orchestration workflow. They want to use a cluster with the same configuration for each notebook.

Which of the following describes how the data engineer can use a feature of Workflows to meet the above requirements? Select one response.

- They can configure each notebook’s job schedule to swap out the cluster after the job has finished running.
- They can use an alert schedule to swap out the clusters after each job has completed.
- They can refresh the cluster after each notebook has finished running in order to use the cluster on a new notebook.
- They can use a sequence pattern to make the notebooks depend on each other in a task orchestration workflow and run the new workflow on the cluster.
- They can use the same cluster to run the notebooks as long as the cluster is a shared cluster.


#### Test 12

A data engineer is running a workflow orchestration on a shared job cluster. They notice that the job they are running is failing and want to use the repair tool to fix the pipeline. 

Which of the following statements describes how Databricks assigns a cluster to the repaired job run? Select one response.

- The platform administrator can set who can search for jobs by id or grant access permissions with access control lists at the user or group level.
- The workspace administrator can set the maximum number of users who can access the table at the group level.
- The platform administrator can set who can view job results or manage runs of a job with access control lists at the user or group level.
- The workspace administrator can set the maximum number of users who can access the table at the user level.
- The platform administrator can set who can grant access permissions or view job history with access control lists at the user level.


#### Test 13

A lead data engineer needs the rest of their team to know when an update has been made to the status of a job run within a Databricks Job.  

How can the data engineer notify their team of the status of the job? Select one response.

- They can schedule a Dashboard alert to the whole team for when the job succeeds.
- They can schedule an email alert to themselves for when the job begins.
- They can schedule a Dashboard alert to themselves for when the job succeeds.
- They can schedule an email alert to the whole team for when the job completes.
- They can schedule a Dashboard alert to a group containing all members of the team for when the job completes.


#### Test 14

A data engineer has a Python workload they want to run as a job. The code for the workload is located in an external cloud storage location.

Which of the following task types and sources can the data engineer use to configure this job? Select one response.

- Delta Live Tables pipeline with Workspace source
- Python script with DBFS source
- Notebook with DBFS source
- Python script with Workspace source
- Notebook with local path source
- Multiple Choice

#### Test 15

Which of the following task types can be combined into a single workflow? Select three responses.

- Python notebooks
- SQL notebooks
- Alert destinations
- JAR files
- SQL warehouses


#### Test 16

A data engineer has run a Delta Live Tables pipeline and wants to see if there are records that were not added to the target dataset due to constraint violations.

Which of the following approaches can the data engineer use to view metrics on failed records for the pipeline? Select two responses.

- They can view the percentage of records that failed each data expectation from the Pipeline details page.
- They can view information on the percentage of records that succeeded each data expectation from the audit log.
- They can view how many records were dropped from the Pipeline details page.
- They can view how many records were added to the target dataset from the accompanying SQL dashboard.
- They can view the duration of each task from the Pipeline details page.


#### Test 17

A data engineer is running a job every 15 minutes. They want to stop the job schedule for an hour before starting it again.

Which of the following allows the data engineer to stop the job during this interval and then start it again without losing the job’s configuration? Select two responses.

- They can detach the job from its accompanying dashboard and then reattach and refresh the dashboard after an hour
- They can stop the job schedule and then refresh the query within the job after an hour.
- They can stop the job schedule and then refresh the notebook that is attached to the task after an hour.
- They can set the Schedule Type to Manual in the Job details panel and change it back to Scheduled after an hour.
- They can click Pause in the Job details panel.


#### Test 18

A data engineer has a notebook that ingests data from a single data source and stores it in an object store. The engineer has three other notebooks that read from the data in the object store and perform various data transformations. The engineer would like to run these three notebooks in parallel after the ingestion notebook finishes running.

Which of the following workflow orchestration patterns do they need to use to meet the above requirements? Select one response. 

- Fan-out pattern
- Hourglass pattern
- Sequence pattern
- Multi-sequence pattern
- Funnel pattern
- Single Choice

#### Test 19

A data engineer needs to configure the order of tasks to run in their ETL workload. The workload has two tasks, Task A and Task B, where Task B can only be run if Task A succeeds.

Which of the following statements describes the dependencies that the data engineer needs to configure and the order they need to be run in? Select one response.

- They need to add Task B as a subtask of Task A and run the tasks in sequence.
- They need to add Task B as a dependency of Task A and run the tasks in parallel.
- They need to add Task B as a subtask of Task A and run the tasks in parallel.
- They need to add Task A as a dependency of Task B and run the tasks in sequence.
- They need to add Task B as a dependency of Task A and run the tasks in sequence.


#### Test 20

A data engineering team needs to be granted access to metrics on a job run. Each team member has user access without any additional privileges.

Which of the following tasks can be performed by an administrator so that each member of the team has access to the metrics? Select one response.

- The workspace administrator can set the maximum number of users who can access the table at the group level.
- The workspace administrator can set the maximum number of users who can access the table at the user level.
- The platform administrator can set who can view job results or manage runs of a job with access control lists at the user or group level.
- The platform administrator can set who can search for jobs by id or grant access permissions with access control lists at the user or group level.
- The platform administrator can set who can grant access permissions or view job history with access control lists at the user level.


#### Test 21

Which of the following configurations are required to specify when scheduling a job? Select two responses. 

- Time zone
- Maximum number of runs
- Trigger type
- Trigger frequency
- Start time


#### Test 22

A data engineer has multiple data sources that they need to combine into one. The combined data sources then need to go through a multi-task ETL process to refine the data using multi-hop (medallion) architecture. It is a requirement that the source data jobs need to be run in parallel.

Which of the following workflow orchestration patterns do they need to use to meet the above requirements? Select one response. 

- Fan-out to sequence pattern
- Funnel to sequence pattern
- Funnel to fan-out pattern
- Parallel to multi-sequence pattern
- Sequence to fan-out pattern


#### Test 23

A data engineer needs their pipeline to run every 12 minutes. 

Which of the following approaches automates this process? Select one response.

- The data engineer can manually pause and start the job every 12 minutes.

- The data engineer can use custom Python code to set the job’s schedule.

- The data engineer can call the Apache AirFlow API to set the job’s schedule.

- This type of scheduling cannot be done with Databricks Workflows.

- The data engineer can set the job’s schedule with custom cron syntax.


#### Test 24

Which of the following are managed by Databricks Workflows? Select three responses.

- Table access control lists (ACLs)
- Error reporting
- Git version control
- Cluster management
- Task orchestration


#### Test 25

A data engineer has a notebook in a remote Git repository. The data from the notebook needs to be ingested into a second notebook that is hosted in Databricks Repos.

Which of the following approaches can the data engineer use to meet the above requirements? Select one response.

- The data engineer can configure the notebook in the remote repository as a task and make it a dependency of the second notebook.
- The data engineer can configure the notebook in a new local remote repository as a job and make it a dependency of the second notebook.
- The data engineer can configure the notebook in a new local repository as a job and make the second notebook dependent on it.
- The data engineer can configure the notebook in the remote repository as a job and make the second notebook dependent on it.
- The data engineer can configure the notebook in a new local repository as a task and make the second notebook dependent on it.