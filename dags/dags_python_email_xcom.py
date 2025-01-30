from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id='dags_python_email_xcom',
    schedule='0 8 1 * *',
    start_date=pendulum.datetime(2025, 1, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:
    @task(task_id='something_task')
    def some_logic(**kwargs):
        from random import choice
        return choice(['success', 'failure'])
    
    send_email = EmailOperator(
        task_id='send_email',
        to='yellowsubmarine372@naver.com',
        subject='{{ data_interval_end.in_timezone("Asia/Seoul") | ds }} some_logic result',
        html_content='{{ data_interval_end.in_timezone("Asia/Seoul") | ds }} result: <br/> \
            {{ti.xcom_pull(task_ids="something_task")}} finished. <br/> '
    )
    
    some_logic() >> send_email