from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators import kubernetes_pod_operator

default_args = {
    'owner': 'Damavis',
    'start_date': datetime(2020, 5, 5),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('etl_dag',
         default_args=default_args,
         schedule_interval=None) as dag:

    extract_tranform = kubernetes_pod_operator.KubernetesPodOperator(
        namespace='airflow',
        image="tonibous/etl-python:1.0",
        cmds=["echo"],
        arguments=["This can be an ETL"],
        labels={"foo": "bar"},
        name="extract-tranform",
        task_id="extract-tranform",
        volumes=[],
        volume_mounts=[],
        get_logs=True
    )

    extract_tranform
