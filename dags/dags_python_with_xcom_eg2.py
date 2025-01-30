from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg2",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    @task(task_id='python_xcom_push_by_return')
    def xcom_push_result(**kwargs):
        return 'Success'
        
    @task(task_id='python_xcom_pull_1')
    def xcom_pull_1(**kwargs):
        ti = kwargs['ti']
        value1 = ti.xcom_pull(task_ids='python_xcom_push_by_return')
        print(f"xcom_pull method return value: {value1}")
    
    @task(task_id='python_xcom_pull_2')
    def xcom_pull_2(status, **kwargs):
        print(f"method input value: {status}")
        
    python_xcom_push_by_return = xcom_push_result() #단순 string이 아닌 airflow 객체
    xcom_pull_2(python_xcom_push_by_return)
    python_xcom_push_by_return >> xcom_pull_1()
