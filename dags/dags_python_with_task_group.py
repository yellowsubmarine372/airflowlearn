from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task, task_group
from airflow.utils.task_group import TaskGroup
import pendulum

with DAG(
    dag_id='dags_python_with_task_group',
    schedule='0 8 1 * *',
    start_date=pendulum.datetime(2025, 1, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:
    def inner_func(**kwargs):
        msg = kwargs.get('msg') or ''
        print(msg)
        
    @task_group(group_id='first_group')
    def group_1():
        '''taks_group decorator first group''' #docstring = tooltip
        
        @task(task_id='inner_function_1')
        def inner_func1():
            print('first task from first task group')
            
        inner_function2 = PythonOperator(
            task_id='inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg': 'second task from first task group'}
        )
        
        inner_func1() >> inner_function2
        
    with TaskGroup(group_id='second_group', tooltip='second group') as group_2:
        '''this docstring will not be shown'''
        @task(task_id='inner_function1')
        def inner_func1(**kwargs):
            print('first task from second task group')
        
        inner_function2 = PythonOperator(
            task_id='inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg': 'second task from second task group'}
        )
        
        inner_func1() >> inner_function2
        
    group_1() >> group_2