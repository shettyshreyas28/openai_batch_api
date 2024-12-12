from setuptools import setup, find_packages

setup(
	name="openai_batch_api",
	version="0.1",
	description="A python module to enable easy submission of OpenAI Batch API jobs, monitor progress and collating outputs",
	author="Shreyas Shetty",
	author_email="shreyas.shetty@allen.in",
	packages=find_packages(),
	install_requires=[
		"pandas",
		"pyyaml",
		"tabulate",
		"python-dotenv",
		"openai",
		"requests"
	],
	python_requires=">=3.10",
	entry_points={
	    "console_scripts": [
            "create-batch=openai_batch_api.create_batch_and_submit:main",
            "status-jobs=openai_batch_api.status_jobs:main",
            "collate-output=openai_batch_api.collate_output:main",
            "delete-tasks=openai_batch_api.delete_tasks:main",
        ],
	},
	include_package_data=True,
	package_data={
		"openai-batch-api": [],
	}
)
