# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Using the Delta Live Tables UI
# MAGIC
# MAGIC This demo will explore the DLT UI. By the end of this lesson you will be able to: 
# MAGIC
# MAGIC * Deploy a DLT pipeline
# MAGIC * Explore the resultant DAG
# MAGIC * Execute an update of the pipeline

# COMMAND ----------

# MAGIC %md
# MAGIC ## Classroom Setup
# MAGIC
# MAGIC Run the following cell to configure your working environment for this course.

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-04.1

# COMMAND ----------

# MAGIC %md ## Generate Pipeline Configuration
# MAGIC Configuring this pipeline will require parameters unique to a given user.
# MAGIC
# MAGIC In the code cell below, specify which language to use by uncommenting the appropriate line.
# MAGIC
# MAGIC Then, run the cell to print out values you'll use to configure your pipeline in subsequent steps.

# COMMAND ----------

# pipeline_language = "SQL"
pipeline_language = "Python"
DA.print_pipeline_config(pipeline_language)

# COMMAND ----------

# MAGIC %md
# MAGIC In this lesson, we deploy a pipeline with a single notebook, specified as Notebook #1 in the cell output above. 
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_24.png"> **HINT:**  You'll want to refer back to the paths above when we add Notebook #2 and #3 to the pipeline in later lessons.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create and Configure a Pipeline
# MAGIC
# MAGIC Let's start by creating a pipeline with a single notebook (Notebook #1).
# MAGIC
# MAGIC Steps:
# MAGIC 1. Click the **Workflows** button on the sidebar, click the **Delta Live Tables** tab, and click **Create Pipeline**. 
# MAGIC 2. Configure the pipeline as specified below. You'll need the values provided in the cell output above for this step.
# MAGIC
# MAGIC | Setting | Instructions |
# MAGIC |--|--|
# MAGIC | Pipeline name | Enter the **Pipeline Name** provided above |
# MAGIC | Product edition | Choose **Advanced** |
# MAGIC | Pipeline mode | Choose **Triggered** |
# MAGIC | Cluster policy | Choose the **Policy** provided above |
# MAGIC | Notebook libraries | Use the navigator to select or enter the **Notebook # 1 Path** provided above |
# MAGIC | Storage location | Enter the **Storage Location** provided above |
# MAGIC | Target schema | Enter the **Target** database name provided above |
# MAGIC | Cluster mode | Choose **Fixed size** to disable auto scaling for your cluster |
# MAGIC | Workers | Enter **0** to use a Single Node cluster |
# MAGIC | Photon Acceleration | Check this checkbox to enable |
# MAGIC | Configuration | Click **Advanced** to view additional settings,<br>Click **Add Configuration** to input the **Key** and **Value** for row #1 in the table below,<br>Click **Add Configuration** to input the **Key** and **Value** for row #2 in the table below |
# MAGIC | Channel | Choose **Current** to use the current runtime version |
# MAGIC
# MAGIC | Configuration | Key                 | Value                                      |
# MAGIC | ------------- | ------------------- | ------------------------------------------ |
# MAGIC | #1            | **`spark.master`**  | **`local[*]`**                             |
# MAGIC | #2            | **`source`** | Enter the **source** provided above |
# MAGIC
# MAGIC <br>
# MAGIC
# MAGIC 3. Click the **Create** button.
# MAGIC 4. Verify that the pipeline mode is set to **Development**.

# COMMAND ----------

DA.validate_pipeline_config(pipeline_language)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Additional Notes on Pipeline Configuration
# MAGIC Here are a few notes regarding the pipeline settings above:
# MAGIC
# MAGIC - **Pipeline mode** - This specifies how the pipeline will be run. Choose the mode based on latency and cost requirements.
# MAGIC   - `Triggered` pipelines run once and then shut down until the next manual or scheduled update.
# MAGIC   - `Continuous` pipelines run continuously, ingesting new data as it arrives.
# MAGIC - **Notebook libraries** - Even though this document is a standard Databricks Notebook, the SQL syntax is specialized to DLT table declarations. We will be exploring the syntax in the exercise that follows.
# MAGIC - **Storage location** - This optional field allows the user to specify a location to store logs, tables, and other information related to pipeline execution. If not specified, DLT will automatically generate a directory.
# MAGIC - **Target** - If this optional field is not specified, tables will not be registered to a metastore, but will still be available in the DBFS. See <a href="https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-user-guide.html#publish-tables" target="_blank">documentation</a> for more information on this option.
# MAGIC - **Cluster mode**, **Min Workers**, **Max Workers** - These fields control the worker configuration for the underlying cluster processing the pipeline. Here, we set the number of workers to 0. This works in conjunction with the **spark.master** parameter defined above to configure the cluster as a Single Node cluster.
# MAGIC - **source** - These keys are caps sensitive. Make sure you've got all lower case letters for the word "source"!

# COMMAND ----------

# MAGIC %md
# MAGIC ## Run a Pipeline
# MAGIC
# MAGIC With a pipeline created, you will now run the pipeline.
# MAGIC
# MAGIC 1. Select **Development** to run the pipeline in development mode. Development mode provides for more expeditious iterative development by reusing the cluster (as opposed to creating a new cluster for each run) and disabling retries so that you can readily identify and fix errors. Refer to the <a href="https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-user-guide.html#optimize-execution" target="_blank">documentation</a> for more information on this feature.
# MAGIC 2. Click **Start**.
# MAGIC
# MAGIC The initial run will take several minutes while a cluster is provisioned. Subsequent runs will be appreciably quicker.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Explore the DAG
# MAGIC
# MAGIC As the pipeline completes, the execution flow is graphed. 
# MAGIC
# MAGIC Selecting the tables reviews the details.
# MAGIC
# MAGIC Select **orders_silver**. Notice the results reported in the **Data Quality** section. 
# MAGIC
# MAGIC With each triggered update, all newly arriving data will be processed through your pipeline. Metrics will always be reported for current run.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Land another batch of data
# MAGIC
# MAGIC Run the cell below to land more data in the source directory, then manually trigger a pipeline update.

# COMMAND ----------

DA.dlt_data_factory.load()

# COMMAND ----------

# MAGIC %md
# MAGIC As we continue through the course, you can return to this notebook and use the method provided above to land new data.
# MAGIC
# MAGIC Running this entire notebook again will delete the underlying data files for both the source data and your DLT Pipeline. 
# MAGIC
# MAGIC If you get disconnected from your cluster or have some other event where you wish to land more data without deleting things, refer to the <a href="$./DE 4.99 - Land New Data" target="_blank">DE 4.99 - Land New Data</a> notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC # Validate Your Knowledge

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A data engineer is configuring a new DLT pipeline and is unsure what mode to choose. They are working with a small batch of unchanging data and need to minimize the costs associated with the pipeline.
# MAGIC
# MAGIC Which of the following modes do they need to use and why? Select one response
# MAGIC
# MAGIC - Triggered; triggered pipelines run once and then shut down until the next manual or scheduled update.
# MAGIC
# MAGIC - Continuous; continuous pipelines ingest new data as it arrives.
# MAGIC
# MAGIC - Triggered; triggered pipelines update once and cannot be updated again until they are manually run.
# MAGIC
# MAGIC - Triggered; triggered pipelines update once and cannot be updated again for 24 hours.
# MAGIC
# MAGIC - Continuous; continuous pipelines run at set intervals and then shut down until the next manual or scheduled update.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A data engineer needs to identify the cloud provider and region of origin for each event within their DLT pipeline.
# MAGIC
# MAGIC Which of the following approaches allows the data engineer to view this information? Select one response. 
# MAGIC
# MAGIC - The data engineer can load the contents of the event log into a view and display the view.
# MAGIC
# MAGIC - The data engineer can use a utility command in Python to list information about each update made to a particular data object.
# MAGIC
# MAGIC - The data engineer can use a **SELECT** query to directly query the **cloud_details** field of the event.
# MAGIC
# MAGIC - The data engineer can view this information in the Task Details page for each task in the pipeline.
# MAGIC
# MAGIC - The data engineer can view the event details for the pipeline from the resultant Directed Acyclic Graph (DAG).

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A data engineer needs to add a file path to their DLT pipeline. They want to use the file path throughout the pipeline as a parameter for various statements and functions.
# MAGIC
# MAGIC Which of the following options can be specified during the configuration of a DLT pipeline in order to allow this? Select one response.
# MAGIC
# MAGIC - They can set the variable in a notebook command and then perform a variable substitution of the file path.
# MAGIC
# MAGIC - They can add a widget to the notebook and then perform a string substitution of the file path.
# MAGIC
# MAGIC - They can add a key-value pair in the Configurations field and then perform a string substitution of the file path.
# MAGIC
# MAGIC - They can add a parameter when scheduling the pipeline job and then perform a variable substitution of the file path.
# MAGIC
# MAGIC - They can specify the file path in the job scheduler when deploying the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A data engineer has built and deployed a DLT pipeline. They want to perform an update that writes a batch of data to the output directory. 
# MAGIC
# MAGIC Which of the following statements about performing this update is true? Select one response.
# MAGIC
# MAGIC - With each triggered update, all newly arriving data will be processed through their pipeline. Metrics will always be reported for the current run.
# MAGIC
# MAGIC - All newly arriving data will be continuously processed through their pipeline. Metrics will be reported for the current run if specified during pipeline deployment.
# MAGIC
# MAGIC - All newly arriving data will be continuously processed through their pipeline. Metrics will always be reported for the current run.
# MAGIC
# MAGIC - With each triggered update, all newly arriving data will be processed through their pipeline. Metrics will be reported if specified during pipeline deployment.
# MAGIC
# MAGIC - With each triggered update, all newly arriving data will be processed through their pipeline. Metrics will not be reported for the current run.
