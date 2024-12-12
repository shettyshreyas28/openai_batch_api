.PHONY: format # Declares format as a phony target, ensuring it always runs even if a file named format exists.

format:
	isort create_batch_and_submit.py
	black create_batch_and_submit.py
	isort status_jobs.py
	black status_jobs.py
	isort collate_output.py
	black collate_output.py
	isort utils.py
	black utils.py
	isort delete_tasks.py
	black delete_tasks.py
