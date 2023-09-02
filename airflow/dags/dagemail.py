from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 5),
    'email': ['eternoaprendiz015@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay':timedelta(seconds=10),
}

dag = DAG('dagemail', description='Testando envio de email',
        default_args = default_args,
        schedule_interval = None,
        catchup = False,
        default_view = 'graph',
        tags = ['teste', 'dagemail']
    )

task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag)
task2 = BashOperator(task_id='tsk2', bash_command='sleep 5', dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', dag=dag)
task4 = BashOperator(task_id='tsk4', bash_command='exit 1', dag=dag)
task5 = BashOperator(task_id='tsk5', bash_command='sleep 5', dag=dag, trigger_rule='none_failed') 
task6 = BashOperator(task_id='tsk6', bash_command='sleep 5', dag=dag, trigger_rule='none_failed')
sendemail = EmailOperator(task_id='sendemail', 
                            to = 'eternoaprendiz015@gmail.com',
                            subject = 'Teste de envio de email',
                            html_content = '<h1>Teste de envio de email</h1>',
                            dag=dag, trigger_rule='one_failed')

task1
task2
[task1, task2] >> task3 
task3 >> task4
task4 >> [task5, task6, sendemail]