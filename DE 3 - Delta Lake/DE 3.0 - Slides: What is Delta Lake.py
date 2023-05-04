# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC Delta Lake is an open-source project that enables building a data lakehouse on top of existing storage systems

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Delta Lake Is Not...
# MAGIC - Proprietary technology
# MAGIC - Storage format
# MAGIC - Storage medium
# MAGIC - Database service or data warehouse

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC Delta Lake Is...
# MAGIC - Open source
# MAGIC - Builds upon standard data formats
# MAGIC - Optimized for cloud object storage
# MAGIC - Built for scalable metadata handling

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC Delta Lake brings ACID to object storage
# MAGIC - Atomicity
# MAGIC - Consistency 
# MAGIC - Isolation
# MAGIC - Durability
# MAGIC
# MAGIC ![test](../Media/DeltaLakeLogo.png)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Problems solved by ACID
# MAGIC 1. Hard to append data
# MAGIC 2. Modification of existing data difficult
# MAGIC 3. Jobs failing mid way
# MAGIC 4. Real-time operations hard
# MAGIC 5. Costly to keep historical data versions

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Validate Your Knowledge

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **1) Which of the following problems are solved by the guarantee of ACID transactions? Select two responses.**
# MAGIC
# MAGIC 1. ACID transactions are guaranteed to either succeed or fail completely, so jobs will never fail mid way.
# MAGIC 2. ACID transactions support the creation of interactive visualization queries.
# MAGIC 3. ACID transactions combine compute and storage scaling to reduce costs.
# MAGIC 4. ACID transactions guarantee that appends will not fail due to conflict, even when writing from multiple sources at the same time.
# MAGIC 5. ACID transactions guarantee the use of proprietary storage formats.
