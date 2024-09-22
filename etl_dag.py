from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime as dtime

def_args = {
    "owner": "airflow",
    "start_date": dtime(2024, 9, 22)
}

with DAG ("ETL",
          catchup=False,
          default_args=def_args) as dag:
    start = DummyOperator(task_id = "START")
    e = DummyOperator(task_id = "EXTRACT")
    t = DummyOperator(task_id = "TRANSFORM")
    l = DummyOperator(task_id = "LOAD")
    end = DummyOperator(task_id = "END")

start >> e >> t >> l >> end