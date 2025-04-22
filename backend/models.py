import time
class Job:
	def __init__(self, job_id, description):
		self.job_id = job_id
		self.description = description
		self.status = "pending"
		self.__log = []
		self.retries = 0
	def start(self):
		self.start_time = time.time()
	def end(self):
		self.end_time = time.time()
	def excecution_time(self):
		if self.end_time and self.start_time:
			return self.end_time - self.start_time
	def execute(self):
		raise NotImplementedError("Each job must implement its own execution logic.")
	def add_log(self, message):
		self.__log.append(message)
	def get_log(self):
		return self.__log
	def retry(self):
		self.retries = self.retries + 1
		self.execute()
	def mark_done(self):
		self.status = "completed"
		self.add_log(f"Mark as {self.status}")
class EmailJob(Job):
	def __init__(self, job_id, recipient):
		super().__init__(job_id, f"Send email to {recipient}\n")
		self.recipient = recipient
	def execute(self):
		print(f"Sending email to {self.recipient}...\n")
		self.mark_done()
class DataProcessingJob(Job):
	def __init__(self, job_id, dataset):
		super().__init__(job_id, f"Process dataset {dataset}\n")
		self.dataset = dataset
	def execute(self):
		print(f"Processing dataset {self.dataset}...\n")
		self.mark_done()
class PriorityJob(Job):
	def __init__(self, job_id, description, priority):
		super().__init__(job_id, description)
		self.priority = priority
	def execute(self):
		print(f"Priority: {self.priority}, Description: {self.description}\n")
		self.mark_done()


class JobFactory:
       @staticmethod
       def create_job(job_id, job_type, param):
              if job_type == "email":
                     return EmailJob(job_id, param)
              elif job_type == "dataprocessing":
                     return DataProcessingJob(job_id, param)
              elif job_type == "priority":
                     return PriorityJob(job_id, param)
              else:
                     raise ValueError("Not a valid job")