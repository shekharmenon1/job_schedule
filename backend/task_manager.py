from collections import defaultdict
from models import Job

class TaskManager:
	def __init__(self):
		self.jobs_by_status = defaultdict(list)
	def add_job(self, job):
		self.jobs_by_status[job.status].append(job)
	def get_all(self):
		return self.jobs_by_status
