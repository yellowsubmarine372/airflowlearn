from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_import_func",
    schedule ="0 8 1 * *",
    start_date =pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup =False,
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id="task_get_sftp",
        python_callable=get_sftp,
    )
    
    task_get_sftp