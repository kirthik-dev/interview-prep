# Content coverage checklist

97 questions across 16 chapters. Every answer contains explanation, example, short answer, detailed answer, follow-up, and mistake.


## Your resume, explained

- [x] [Tell me about yourself](../index.html#resume-q1) — Resume evidence
- [x] [How should I explain the skills section?](../index.html#resume-q2) — Resume evidence
- [x] [How do I explain education and training?](../index.html#resume-q3) — Resume evidence
- [x] [How do I explain the NIT population forecasting internship?](../index.html#resume-q4) — Resume evidence

## YLogx: experience Q&A

- [x] [What is a metadata-driven data quality platform?](../index.html#ylogx-q1) — Resume evidence
- [x] [Which quality checks matter, and how are failures handled?](../index.html#ylogx-q2) — Resume evidence
- [x] [How do I explain the approximately 40% onboarding improvement?](../index.html#ylogx-q3) — Resume evidence
- [x] [What was PMAP and how did schema mapping work?](../index.html#ylogx-q4) — Resume evidence
- [x] [How do Azure Blob, Git, and Azure DevOps fit into ETL generation?](../index.html#ylogx-q5) — Resume evidence
- [x] [What did you do with dbt and Snowflake?](../index.html#ylogx-q6) — Resume evidence
- [x] [How did SQL optimization and AI-assisted SQL review help?](../index.html#ylogx-q7) — Resume evidence
- [x] [What does near-real-time serving with FastAPI and PostgreSQL mean?](../index.html#ylogx-q8) — Resume evidence
- [x] [How do I explain my ownership and business impact?](../index.html#ylogx-q9) — Resume evidence

## Project 1 · Healthcare CDC

- [x] [Explain Healthcare end to end](../index.html#healthcare-q1) — Repository evidence
- [x] [What exactly happens in Bronze, Silver, and Gold?](../index.html#healthcare-q2) — Repository evidence
- [x] [How were CDC events generated and transported?](../index.html#healthcare-q3) — Repository evidence
- [x] [How did Silver merges work?](../index.html#healthcare-q4) — Repository evidence
- [x] [How do checkpoints, replay, and recovery apply here?](../index.html#healthcare-q5) — Repository evidence
- [x] [What are the Gold outputs and the star schema?](../index.html#healthcare-q6) — Repository evidence

## Project 2 · RetailPulse

- [x] [What does the actual RetailPulse repository do?](../index.html#retail-q1) — Repository evidence
- [x] [How would the requested local Delta + Unity Catalog design work?](../index.html#retail-q2) — Proposed design
- [x] [How are batch files and Kafka events ingested?](../index.html#retail-q3) — Repository evidence
- [x] [How do Silver changes and data quality gates work?](../index.html#retail-q4) — Repository evidence
- [x] [What does Airflow orchestrate and what reaches the dashboard?](../index.html#retail-q5) — Repository evidence
- [x] [How would you make RetailPulse production-ready?](../index.html#retail-q6) — Repository evidence

## Project 3 · Olist marketplace analytics

- [x] [Explain the Olist project end to end](../index.html#olist-q1) — Repository evidence
- [x] [What cleaning and derived features were created?](../index.html#olist-q2) — Repository evidence
- [x] [Why can the joined fact table inflate revenue?](../index.html#olist-q3) — Repository evidence
- [x] [What performance techniques were used and what do outputs mean?](../index.html#olist-q4) — Repository evidence

## Data engineering foundations

- [x] [What are ETL and ELT?](../index.html#foundations-q1) — Concept lesson
- [x] [Batch versus streaming: when do I use each?](../index.html#foundations-q2) — Concept lesson
- [x] [Lake, warehouse, and lakehouse: what is the difference?](../index.html#foundations-q3) — Concept lesson
- [x] [How do Bronze, Silver, and Gold differ in a generic pipeline?](../index.html#foundations-q4) — Concept lesson
- [x] [Parquet, Delta, and Iceberg: what are they?](../index.html#foundations-q5) — Concept lesson
- [x] [What do ACID, MERGE, schema evolution, and time travel mean?](../index.html#foundations-q6) — Concept lesson
- [x] [How do storage, catalog, compute, and serving work together?](../index.html#foundations-q7) — Concept lesson
- [x] [How do facts, dimensions, keys, and grain fit together?](../index.html#foundations-q8) — Concept lesson

## SQL interview lab

- [x] [How do INNER, LEFT, and other joins behave?](../index.html#sql-q1) — Concept lesson
- [x] [GROUP BY, WHERE, HAVING, and COUNT: what differs?](../index.html#sql-q2) — Concept lesson
- [x] [How do window functions differ from GROUP BY?](../index.html#sql-q3) — Concept lesson
- [x] [How do I deduplicate or find the latest row?](../index.html#sql-q4) — Concept lesson
- [x] [CTE, subquery, EXISTS, and incremental SQL: how do I use them?](../index.html#sql-q5) — Concept lesson
- [x] [How do SQL NULLs and safe division work?](../index.html#sql-q6) — Concept lesson
- [x] [How do I investigate a slow or incorrect SQL query?](../index.html#sql-q7) — Concept lesson

## Python fundamentals for DE

- [x] [Lists, tuples, dictionaries, and sets: when do I use each?](../index.html#python-q1) — Concept lesson
- [x] [How do functions and exceptions make ETL safer?](../index.html#python-q2) — Concept lesson
- [x] [How do I read files and handle JSON?](../index.html#python-q3) — Concept lesson
- [x] [What is a generator and why is it useful?](../index.html#python-q4) — Concept lesson
- [x] [What is a basic reliable ETL loop?](../index.html#python-q5) — Concept lesson

## Spark & PySpark interview lab

- [x] [Driver, executors, partitions, and lazy evaluation: what happens?](../index.html#spark-q1) — Concept lesson
- [x] [What is a shuffle and why can it be expensive?](../index.html#spark-q2) — Concept lesson
- [x] [Broadcast join versus shuffle join: which should I use?](../index.html#spark-q3) — Concept lesson
- [x] [How do I detect and handle skew?](../index.html#spark-q4) — Concept lesson
- [x] [Repartition, coalesce, cache, and AQE: how do they differ?](../index.html#spark-q5) — Concept lesson
- [x] [How do I deduplicate with PySpark and enforce types?](../index.html#spark-q6) — Concept lesson
- [x] [What should I inspect when a Spark job fails or slows down?](../index.html#spark-q7) — Concept lesson

## CDC & SCD, from the beginning

- [x] [What are the four common ways to capture changes?](../index.html#cdc-scd-q1) — Concept lesson
- [x] [Can you show CDC with a tiny generic example?](../index.html#cdc-scd-q2) — Concept lesson
- [x] [What are SCD Types 0, 1, 2, and 3?](../index.html#cdc-scd-q3) — Concept lesson
- [x] [How does an SCD Type 2 history actually look?](../index.html#cdc-scd-q4) — Concept lesson
- [x] [What are SCD Types 4, 5, 6, and 7?](../index.html#cdc-scd-q5) — Concept lesson
- [x] [How do CDC and SCD work together?](../index.html#cdc-scd-q6) — Concept lesson

## Kafka, Event Hubs & streaming

- [x] [What is Azure Event Hubs?](../index.html#streaming-q1) — Concept lesson
- [x] [What are Kafka topics, partitions, offsets, and consumer groups?](../index.html#streaming-q2) — Concept lesson
- [x] [What do checkpoints and delivery guarantees really mean?](../index.html#streaming-q3) — Concept lesson
- [x] [What are event time, processing time, windows, and watermarks?](../index.html#streaming-q4) — Concept lesson
- [x] [What is a generic Structured Streaming example?](../index.html#streaming-q5) — Concept lesson

## Airflow, dbt, cloud & APIs

- [x] [How does Airflow orchestration work?](../index.html#platform-q1) — Concept lesson
- [x] [What do dbt models, tests, and incremental materializations do?](../index.html#platform-q2) — Concept lesson
- [x] [Snowflake, BigQuery, Dataproc, ADF, and Composer: who does what?](../index.html#platform-q3) — Concept lesson
- [x] [How should a data API be designed?](../index.html#platform-q4) — Concept lesson
- [x] [What does open-source Unity Catalog manage?](../index.html#platform-q5) — Concept lesson

## Production readiness & scenario Q&A

- [x] [How do you take a pipeline from development to production?](../index.html#production-q1) — Practice example
- [x] [What do CI/CD, configuration, and secrets look like?](../index.html#production-q2) — Practice example
- [x] [What if duplicate or out-of-order events arrive?](../index.html#production-q3) — Practice example
- [x] [What if data arrives late or the source schema changes?](../index.html#production-q4) — Practice example
- [x] [What if a merge fails or the job crashes mid-run?](../index.html#production-q5) — Practice example
- [x] [How do you safely publish several PostgreSQL marts?](../index.html#production-q6) — Practice example
- [x] [How do you run a backfill without breaking current data?](../index.html#production-q7) — Practice example
- [x] [What if pipeline lag or freshness fails while tasks are green?](../index.html#production-q8) — Practice example
- [x] [How do you respond to a wrong aggregate or revenue spike?](../index.html#production-q9) — Practice example
- [x] [What are RPO, RTO, rollback, and disaster recovery?](../index.html#production-q10) — Practice example
- [x] [How do you control cost and support production operations?](../index.html#production-q11) — Practice example

## ML forecasting & MLOps

- [x] [How do I describe my ML experience?](../index.html#ml-q1) — User-described experience
- [x] [How does retail demand forecasting relate to stock on hand?](../index.html#ml-q2) — Practice example
- [x] [What features, lags, and rolling statistics are useful?](../index.html#ml-q3) — Practice example
- [x] [How do I validate a forecast and avoid leakage?](../index.html#ml-q4) — Practice example
- [x] [What do MAE, WAPE, and forecast bias mean?](../index.html#ml-q5) — Practice example
- [x] [How does financial inflow/outflow forecasting differ?](../index.html#ml-q6) — Practice example
- [x] [What does an end-to-end MLflow pipeline look like?](../index.html#ml-q7) — Practice example
- [x] [How do batch inference, monitoring, retraining, and rollback work?](../index.html#ml-q8) — Practice example

## RAG & AI workflow Q&A

- [x] [What is RAG and how does a document become an answer?](../index.html#rag-q1) — Resume evidence
- [x] [How do embeddings, Chroma, MongoDB, and GraphDB differ?](../index.html#rag-q2) — Resume evidence
- [x] [What do LangChain and LangGraph do?](../index.html#rag-q3) — Resume evidence
- [x] [How do you evaluate and secure a RAG application?](../index.html#rag-q4) — Practice example

## Last-minute interview revision

- [x] [What should I revise in 30 minutes?](../index.html#revision-q1) — Study guide
- [x] [How should I answer design and incident questions?](../index.html#revision-q2) — Study guide

## Coverage and accuracy policy

- [x] Resume summary, technical skills, four YLogx bullets, NIT internship, three projects, education and training.
- [x] User-described retail demand/inventory, financial flow forecasting and MLflow work.
- [x] Generic code examples, expected outputs and prerequisite notes.
- [x] CDC methods and event/log distinction; SCD 0–7 with naming caveat and history examples.
- [x] Production release, replay, backfill, skew, late data, schema drift, partial publication and recovery.
- [x] RAG, LangChain, LangGraph, Chroma, GraphDB/MCP, MongoDB, APIs and SQL review.
- [x] Prior corrections: Healthcare incomplete baseline, no verified durable recovery, ordinary batch Gold, resume-only infrastructure claims; RetailPulse actual Iceberg versus proposed Delta/OSS catalog, grain and monitoring gaps; Olist counts, join multiplication, metric and performance caveats.
- [x] Glossary, architecture flows, comparison tables and revision guide.
- [x] Public content excludes contact details, private source data and credentials.

This checklist maps all distinct substantive topics available from the conversation and supplied resume. It is an organized reconstruction, not a verbatim transcript or recovery of unavailable employer implementation details.
