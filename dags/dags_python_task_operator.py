from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_operator",
    schedule ="0 8 1 * *",
    start_date =pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup =False,
) as dag:
    
    @task(task_id='python_task_1')
    def print_context(some_input):
        print(some_input)
    
    python_task_1 = print_context("executing task_decorator")