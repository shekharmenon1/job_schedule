from models import EmailJob, DataProcessingJob, PriorityJob, JobFactory
from task_manager import TaskManager
from executor import Executor
jobs = [EmailJob(1, "user@example.com"), DataProcessingJob(2, "dataset_A"), EmailJob(3, "admin@example.com"), DataProcessingJob(4, "dataset_B")]
manager = TaskManager()
for job in jobs:
        manager.add_job(job)
executor = Executor(jobs)
executor.run()


job1 = PriorityJob(1, "High Priority job", 1)
job2 = PriorityJob(2, "Low Priority job", 3)
job3 = PriorityJob(3, "Medium Priority job", 2)

# Sort by priority before passing to executor
priority_jobs = sorted([job1, job2, job3], key=lambda j: j.priority)
for pjob in priority_jobs:
    print(f"Job: {pjob.job_id}, Priority: {pjob.priority}<br>")


executorpriority = Executor(priority_jobs)
executorpriority.run()

for job in jobs:
        print (f"Logs for job {job.job_id}:")
        for log in job.get_log() :
                print("-", log)
                print("<br>")
              
jobtypes = [(0, "email", "good@gmail.com"), (3, "dataprocessing", "gooddata")]

for typejob in jobtypes:
        JobFactory.create_job(*typejob)