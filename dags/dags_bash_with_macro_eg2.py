from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg2",
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_task_2 = BashOperator(
        task_id="bash_task_2",
        env={
            'START_DATE_o': '{{ (data_interval_start.in_timezone("Asia/Seoul")) | ds }}',
            'START_DATE': '{{ (data_interval_start.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=16)) | ds }}',
            'END_DATE_o': '{{ (data_interval_end.in_timezone("Asia/Seoul")) | ds }}',
            'END_DATE': '{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=11)) | ds }}'
        },
        bash_command="echo $START_DATE_o && echo $START_DATE && echo $END_DATE_o && echo $END_DATE",
    )

    bash_task_2 