from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_python_with_xcom",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    @task(task_id='python_push')
    def python_push_xcom():
        result_dict = {'status': 'Success', 'data': [1,2,3], 'option_cnt': 100}
        return result_dict
    
    bash_pull = BashOperator(
        task_id='bash_pull',
        env={
            'STATUS': '{{ti.xcom_pull(task_ids="python_push")["status"]}}',
            'DATA': '{{ti.xcom_pull(task_ids="python_push")["data"]}}',
            'OPTION_CNT': '{{ti.xcom_pull(task_ids="python_push")["option_cnt"]}}'
        },
        bash_command="echo $STATUS && echo $DATA && echo $OPTION_CNT"
    )
    python_push_xcom() >> bash_pull
    
    bash_push = BashOperator(
        task_id='bash_push',
        bash_command='echo PUSH_START '
            '{{ ti.xcom_push(key="bash_pushed", value=200) }} && '
        'echo PUSH_COMPLETE'
    )
    
    @task(task_id='python_pull')
    def python_pull_xcom(**kwargs):
        ti = kwargs['ti']
        print('status value: ', ti.xcom_pull(key='bash_pushed'))
        print('return value: ', ti.xcom_pull(task_ids='bash_push'))
    
    bash_push >> python_pull_xcom()