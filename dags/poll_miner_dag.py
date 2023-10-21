from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'poll_mainer_dag',
    default_args=default_args,
    description='A DAG executes poll_miner function in another VM through SSH every 2 minutes',
    schedule_interval=timedelta(minutes=2),
)

run_remote_script = BashOperator(
    task_id='poll_mainer_task',
    bash_command='ssh -i /home/iliastepanov/.ssh/ssh_key iliastepanov@34.125.37.209 "python3 /home/iliastepanov/poll_miner.py"',
    dag=dag,
)

run_remote_script