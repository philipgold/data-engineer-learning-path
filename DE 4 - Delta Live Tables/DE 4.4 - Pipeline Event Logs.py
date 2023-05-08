# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Exploring the Pipeline Events Logs
# MAGIC
# MAGIC DLT uses the event logs to store much of the important information used to manage, report, and understand what's happening during pipeline execution.
# MAGIC
# MAGIC Below, we provide a number of useful queries to explore the event log and gain greater insight into your DLT pipelines.

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-04.4

# COMMAND ----------

# MAGIC %md
# MAGIC ## Query Event Log
# MAGIC The event log is managed as a Delta Lake table with some of the more important fields stored as nested JSON data.
# MAGIC
# MAGIC The query below shows how simple it is to read this table and created a DataFrame and temporary view for interactive querying.

# COMMAND ----------

event_log_path = f"{DA.paths.storage_location}/system/events"

event_log = spark.read.format('delta').load(event_log_path)
event_log.createOrReplaceTempView("event_log_raw")

display(event_log)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Set Latest Update ID
# MAGIC
# MAGIC In many cases, you may wish to gain updates about the latest update (or the last N updates) to your pipeline.
# MAGIC
# MAGIC We can easily capture the most recent update ID with a SQL query.

# COMMAND ----------

latest_update_id = spark.sql("""
    SELECT origin.update_id
    FROM event_log_raw
    WHERE event_type = 'create_update'
    ORDER BY timestamp DESC LIMIT 1""").first().update_id

print(f"Latest Update ID: {latest_update_id}")

# Push back into the spark config so that we can use it in a later query.
spark.conf.set('latest_update.id', latest_update_id)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Perform Audit Logging
# MAGIC
# MAGIC Events related to running pipelines and editing configurations are captured as **`user_action`**.
# MAGIC
# MAGIC Yours should be the only **`user_name`** for the pipeline you configured during this lesson.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT timestamp, details:user_action:action, details:user_action:user_name
# MAGIC FROM event_log_raw 
# MAGIC WHERE event_type = 'user_action'

# COMMAND ----------

# MAGIC %md
# MAGIC ## Examine Lineage
# MAGIC
# MAGIC DLT provides built-in lineage information for how data flows through your table.
# MAGIC
# MAGIC While the query below only indicates the direct predecessors for each table, this information can easily be combined to trace data in any table back to the point it entered the lakehouse.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT details:flow_definition.output_dataset, details:flow_definition.input_datasets 
# MAGIC FROM event_log_raw 
# MAGIC WHERE event_type = 'flow_definition' AND 
# MAGIC       origin.update_id = '${latest_update.id}'

# COMMAND ----------

# MAGIC %md
# MAGIC ## Examine Data Quality Metrics
# MAGIC
# MAGIC Finally, data quality metrics can be extremely useful for both long term and short term insights into your data.
# MAGIC
# MAGIC Below, we capture the metrics for each constraint throughout the entire lifetime of our table.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT row_expectations.dataset as dataset,
# MAGIC        row_expectations.name as expectation,
# MAGIC        SUM(row_expectations.passed_records) as passing_records,
# MAGIC        SUM(row_expectations.failed_records) as failing_records
# MAGIC FROM
# MAGIC   (SELECT explode(
# MAGIC             from_json(details :flow_progress :data_quality :expectations,
# MAGIC                       "array<struct<name: string, dataset: string, passed_records: int, failed_records: int>>")
# MAGIC           ) row_expectations
# MAGIC    FROM event_log_raw
# MAGIC    WHERE event_type = 'flow_progress' AND 
# MAGIC          origin.update_id = '${latest_update.id}'
# MAGIC   )
# MAGIC GROUP BY row_expectations.dataset, row_expectations.name

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Validate Your Knowledge

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **A data engineer wants to query metrics on the latest update made to their pipeline. They need to be able to see the event type and timestamp for each update.**
# MAGIC
# MAGIC Which of the following approaches allows the data engineer to complete this task? Select one response.
# MAGIC
# MAGIC - The data engineer can query the update ID from the events log where the event type is **create_update**.
# MAGIC
# MAGIC - The data engineer can query the update ID from the events log where the action type is **user_action**.
# MAGIC
# MAGIC - The data engineer can view the update ID from the Pipeline Details page in the **user_action** table.
# MAGIC
# MAGIC - The data engineer can query the update ID from the events log where the event type is **last_update**.
# MAGIC
# MAGIC - The data engineer can view the update ID from the Pipeline Details page in the **create_update** table.

# COMMAND ----------

# MAGIC %md
# MAGIC Which of the following data quality metrics are captured through **row_epectations** in a pipeline’s event log? Select three responses.
# MAGIC
# MAGIC - Update ID
# MAGIC - Name
# MAGIC - Failed records
# MAGIC - Flow progress
# MAGIC - Dataset

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A data engineer needs to examine how data is flowing through tables within their pipeline.
# MAGIC
# MAGIC Which of the following correctly describes how they can accomplish this? Select one response.
# MAGIC
# MAGIC - The data engineer can query the flow definition for the direct successor of the table and then combine the results.
# MAGIC
# MAGIC - The data engineer can view the flow definition of each table in the pipeline from the Pipeline Events log.
# MAGIC
# MAGIC - The data engineer can query the flow definition for each table and then combine the results.
# MAGIC
# MAGIC - The data engineer can query the flow definition for the direct predecessor of each table and then combine the results.
# MAGIC
# MAGIC - The data engineer can combine the flow definitions for all of the tables into one query.

# COMMAND ----------

# MAGIC %md
# MAGIC A data engineer needs to review the events related to their pipeline and the pipeline’s configurations.
# MAGIC
# MAGIC Which of the following approaches can the data engineer take to accomplish this? Select one response.
# MAGIC
# MAGIC - The data engineer can select events of type **user_action** in the resultant DAG.
# MAGIC
# MAGIC - The data engineer can select events of type **user_action** in the output table of the pipeline.
# MAGIC
# MAGIC - The data engineer can query events of type **user_action** from the configured storage location.
# MAGIC
# MAGIC - The data engineer can query events of type **user_action** from the checkpoint directory.
# MAGIC
# MAGIC - The data engineer can query events of type **user_action** from the event log.
