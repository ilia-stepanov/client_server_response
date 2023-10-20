from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from main_server.calculate_sum_hashrate import calculate_sum_hashrate
import psycopg2

default_args = {
    'owner': 'iliastepanov',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),  
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)}

dag = DAG(
    'calculate_sum_hashrate_dag',
    default_args=default_args,
	description='A DAG calculates sum hashrate per each miner_type every 5 minutes',
    schedule_interval=timedelta(minutes=5)
)

capture_hashrate_task = PythonOperator(
    task_id='calculate_sum_hashrate_task',
    python_callable=calculate_sum_hashrate,
    dag=dag)
