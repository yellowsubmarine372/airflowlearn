from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_macro",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    @task(task_id='task_using_macro',
          templates_dict={'start_date': '{{ (data_interval_start.in_timezone("Asia/Seoul") + macros.dateutil.relativedelta.relativedelta(months=-1, day=1)) | ds }}',
                          'end_date': '{{ (data_interval_end.in_timezone("Asia/Seoul").replace(day=1) + macros.dateutil.relativedelta.relativedelta(days=-1)) | ds }}'})
    def get_datetime_macro(**kwargs):
        templates_dict = kwargs.get('templates_dict') or {}
        start_date = templates_dict.get('start_date')
        end_date = templates_dict.get('end_date')
        print(f"start_date: {start_date}")
        print(f"end_date: {end_date}")
        
    @task(task_id='task_direct_calc')
    def get_datetime_calc(**kwargs):
        from dateutil.relativedelta import relativedelta
        
        data_interval_end = kwargs.get('data_interval_end')
        prev_month_day_first = data_interval_end.in_timezone("Asia/Seoul") + relativedelta(months=-1, day=1)
        prev_month_day_last = data_interval_end.in_timezone("Asia/Seoul").replace(day=1) + relativedelta(days=-1)
        
        print(f"prev_month_day_first: {prev_month_day_first.strftime('%Y-%m-%d')}")
        print(f"prev_month_day_last: {prev_month_day_last.strftime('%Y-%m-%d')}")
    
    get_datetime_macro() >> get_datetime_calc()
    
    