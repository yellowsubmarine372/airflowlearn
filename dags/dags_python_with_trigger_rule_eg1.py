from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from airflow.exceptions import AirflowException
import pendulum

with DAG(
    dag_id='dags_python_with_trigger_rule_eg1',
    schedule='0 8 1 * *',
    start_date=pendulum.datetime(2025, 1, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:
    bash_upstream_1 = BashOperator(
        task_id='bash_upstream_1',
        bash_command='echo "upstream_1"'
    )
    
    @task(task_id= 'python_upstream_1')
    def python_upstream_1():
        raise AirflowException('python_upstream_1 excpetion')
        
    @task(task_id= 'python_upstream_2')
    def python_upstream_2():
        print('success')
        
    @task(task_id='python_downstream_1', trigger_rule='all_done')
    def python_downstream_1():
        print('success')
        
    [bash_upstream_1, python_upstream_1(), python_upstream_2()] >> python_downstream_1()