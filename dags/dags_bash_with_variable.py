from airflow.operators.bash import BashOperator
from airflow.models import Variable
from airflow import DAG
import pendulum

with DAG(
    dag_id='dags_bash_with_variable',
    schedule='0 8 1 * *',
    start_date=pendulum.datetime(2025, 1, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:
    var_value = Variable.get('sample_key')
    
    bash_var_1 = BashOperator(
        task_id='bash_var_1', 
        bash_command= f'echo {var_value}')
    
    bash_var_2 = BashOperator(
        task_id='bash_var_2', 
        bash_command= "echo variable: {{ var.value.sample_key }}" #template 문법의 방식 권고(스케줄러 부하 경감)
    )