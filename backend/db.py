from models import EmailJob, DataProcessingJob
from task_manager import TaskManager
from executor import Executor
from db import save_job
jobs = [EmailJob(1, "user@example.com"), DataProcessingJob(2, "dataset_A"), EmailJob(3, "admin@example.com"), DataProcessingJob(4, "dataset_B")]
manager = TaskManager()
for job in jobs:
        manager.add_job(job)
executor = Executor(jobs)
executor.run()
for job in jobs:
        save_job(job)
