from apscheduler.schedulers.blocking import BlockingScheduler


class SchedulerManager:
    def __init__(self):
        self.scheduler = BlockingScheduler(timezone='Asia/Seoul')

    def add_schedule(self, job, interval):
        self.scheduler.add_job(job, 'interval', seconds=interval)

    def start_scheduler(self):
        self.scheduler.start()
