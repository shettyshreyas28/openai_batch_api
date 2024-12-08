# OpenAI Batch API utils

Utilities to ease creating OpenAI Batch API calls, monitor status of submitted jobs and collate results once the tasks are completed

## Requirements
- python-dotenv
- tabulate
- PyYAML
- pandas

## Configuration file setup
* Specify the *input_file* to be processed and the *output_file* after merging the API call outputs
* The columns containing the unique identifier in the *input_file* and the column containing the input data to model are to be specified in *id_column* and *content_column* respectively
* Prompt for processing the input data. Look at the example in the sample config file to understand how to specify prompts that span multiple files
* Data path : Specify the folder where the task files are to be stored
* Current setup assumes json mode output. If you don't need that modify the model_params field in the config.yaml file

## Running the script
* Setup config.yaml
* Update the .env file in the current folder to enable loading the OPENAI_API_KEY
* Run ```python create_batch_and_submit.py```
* Once that above script is run, check the status of jobs by running ```python status_jobs.py```
* Output of the status_jobs script should look like below
![status_jobs.py output](/image/status_jobs_sample.png)
* Once all the batches are complete, run ```python collate_output.py``` script to get the outputs in the file specifed in output_file in the config.yaml
