from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule ="0 8 1 * *",
    start_date =pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup =False,
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id="regist2_t1",
        python_callable=regist2,
        op_args=["sen","f",'kr','seoul'],
        op_kwargs={"email":"sen@gmail.com","phone":"010-1234-5678"},
    )
    
    regist2_t1
    