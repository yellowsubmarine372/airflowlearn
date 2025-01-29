from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_task_1 = BashOperator(
        task_id="bash_task_1",
        env={'START_DATE': '{{ data_interval_start.in_timezone("Asia/Seoul") | ds }}', 
             'END_DATE': '{{ data_interval_end.in_timezone("Asia/Seoul") | ds }}',
             'START_DATE_mac': '{{ (data_interval_start.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1)) | ds }}',
             'END_DATE_mac': '{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1)) | ds }}'},
        bash_command="echo $START_DATE && echo $END_DATE && echo $START_DATE_mac && echo $END_DATE_mac",
    )
    
    bash_task_1