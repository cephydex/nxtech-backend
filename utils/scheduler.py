# scheduler.py
from routes.licensing_system.schema import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv('DATABASE_URL')


import pytz


jobstores = {
    'default': SQLAlchemyJobStore(url=database_url)
}

scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=pytz.timezone('Etc/GMT'))

def start_scheduler():
    scheduler.start()

def stop_scheduler():
    scheduler.shutdown()


def delete_all_jobs():
    scheduler.remove_all_jobs()



def schedule_invoice_creation(data, admin_id):
    from routes.licensing_system.background_tasks import generateInvoice
    run_date = run_date=data.next_invoice_date
    scheduler.add_job(generateInvoice, trigger='date', run_date=run_date, args=[data, admin_id], misfire_grace_time=60)
   


# @scheduler.scheduled_job('date', run_date='2024-05-30 08:51:00')
# def scheduled_job_2():
#     print("scheduled_job_2")

# def test_schedule(data: InvoiceData, admin_id: str):
#     # Set a test date for 8:15 AM today
#     now = datetime.now()
#     test_run_date = now.replace(hour=8, minute=22, second=0, microsecond=0)
    
#     # Ensure the test run date is in the future
#     if test_run_date < now:
#         test_run_date = test_run_date + timedelta(days=1)
    
#     data.next_invoice_date = test_run_date
#     print("Scheduled task at:", data.next_invoice_date, "for admin:", admin_id)
#     schedule_invoice_creation(data, admin_id)

