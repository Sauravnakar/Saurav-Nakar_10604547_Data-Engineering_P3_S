from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="credit_card_batch_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    ingest = BashOperator(
        task_id="ingest_data",
        bash_command="python /ingestion/producer.py"
    )

    process = BashOperator(
        task_id="process_data",
        bash_command="spark-submit /processing/spark_job.py"
    )

    aggregate = BashOperator(
        task_id="aggregate_data",
        bash_command="spark-submit /aggregation/aggregation_job.py"
    )

    ingest >> process >> aggregate
