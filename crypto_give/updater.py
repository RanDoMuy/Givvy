from .task import add_to_Transactions
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler= BackgroundScheduler()
    scheduler.add_job(add_to_Transactions, 'interval', seconds=10000000000)
    scheduler.start()