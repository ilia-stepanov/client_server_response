from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.ssh_operator import SSHOperator

# Define the default_args dictionary
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'execute_remote_script',
    default_args=default_args,
    description='DAG to execute a remote Python script',
    schedule_interval=timedelta(days=1),  # Adjust as needed
    catchup=False,
)

# Define the SSHOperator
execute_script = SSHOperator(
    task_id='execute_script',
    ssh_conn_id='ssh_connector_to_surveyor_server',  # Define your SSH connection in Airflow
    command='python3 /home/iliastepanov/server.py',  # Adjust path and script name
    dag=dag,
)