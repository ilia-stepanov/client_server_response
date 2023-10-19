from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 19),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'remote_script_execution_ssh',
    default_args=default_args,
    description='A simple DAG to execute a script on a remote machine',
    schedule_interval='@once',
)

run_remote_script = BashOperator(
    task_id='run_remote_script_ssh',
    bash_command='ssh -i /home/iliastepanov/.ssh/ssh_key iliastepanov@34.125.37.209 "python3 /home/iliastepanov/server.py"',
    dag=dag,
)

run_remote_script