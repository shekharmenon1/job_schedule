import threading, time, random
from errors import JobExecutionError
class Executor:
        def __init__(self, jobs):
                self.jobs = jobs
                self.lock = threading.Lock()
        def run_job(self, job):
                try:
                        job.start()
                        print(f"Executing job {job.job_id}...<br>")
                        time.sleep(random.uniform(1, 3))
                        if random.random() < 0.5:
                                raise JobExecutionError(job.job_id)
                        job.execute()
                except JobExecutionError as e:
                        if job.retries > 2:
                                print(f"Error: {e}\n")
                        else:
                                print("reached retry")
                                job.retry()
                print(f"Completed job {job.job_id} in {job.retries} retries.<br>")
                job.end()
                print(f"job finished in {job.excecution_time()}<br>")
        def run(self):
                threads = []
                for job in self.jobs:
                        t = threading.Thread(target=self.run_job, args=(job,))
                        threads.append(t)
                        t.start()
                for t in threads:
                        t.join()
