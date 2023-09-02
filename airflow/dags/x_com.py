from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


dag = DAG('x_com', description='Testando x_com',
        schedule_interval=None,start_date=datetime(2023, 3, 5),
        catchup=False
    )

def task_write(**kwargs):
    kwargs['ti'].xcom_push(key = 'valorxcom1', value = 10)

task1 = PythonOperator(task_id ='tsk1', python_callable = task_write, dag = dag)

def task_read(**kwargs):
    value = kwargs['ti'].xcom_pull(key = 'valorxcom1')

task2 = PythonOperator(task_id ='tsk2', python_callable = task_read, dag = dag)


task1 >> task2