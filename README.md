# openai_batch_api

The **openai_batch_api** python package enables batch processing with OpenAI Batch API. It includes functionalities for:
- Creating and submitting batches
- Monitoring batch statuses
- Collating outputs

---

## Features

1. **Batch Creation and Submission**  
   Automatically create batches from input data and submit them to OpenAI's API.
   
2. **Batch Status Monitoring**  
   Monitor the status of submitted batches and retrieve their details.

3. **Result Collation**  
   Collate and process results from completed batches, saving them in a user-defined format.

4. **Delete intermediate task files**
   Delete the intermediate task files created

---

## Installation

To install the module, clone this repository and install it using pip:

```bash
git clone https://github.com/shettyshreyas28/openai_batch_api
cd openai_batch_api
pip install .
```

# Prerequisites
**Python dependencies**
Ensure that you have python 3.10 or later installted. All required dependencies will be installed automatically during the module installation.

**Environment Variables**
```bash
export OPENAI_API_KEY="<your_api_key>"
```

**config.yaml**
The ```config.yaml``` file is not included in the repository. You must create this file and provide its path when running the scripts. Below is 
an example of the ```config.yaml``` structure:
```yaml
input_file: "path/to/input.csv"
id_column: "id"
content_column: "content"
image_url: "column containing image url for the input row"
prompt: "Your prompt here"
batch_size: 50
model_params:
  model: gpt-4o-min
  temperature: 0
  response_format:
    type: json_object
output_file: "path/to/output.pkl"
data_path: "path/to/data/folder"
```
* input_file: Path to the input file (CSV or PKL).
* id_column: Column name for unique identifiers in the input file.
* content_column: Column name for task content.
* image_url_column: Column name for image urls corresponding to each row. Can be left unspecified
* prompt: Prompt to be used for task generation.
* batch_size: Number of tasks per batch.
* model_params: Parameters for the OpenAI model (e.g., temperature, max_tokens).
* output_file: Path for the final output file.
* data_path: Path to folder for saving intermediate task files


# Usage

**Create and submit batches**
```python
create-batch --config path/to/config.yaml
```

**Check Batch Status**
```python
status-jobs --config path/to/config.yaml
```
Output of ```status-jobs``` should look like below
![status_jobs.py output](/image/status_jobs_sample.png)

**Collate Results**
```python
collate-output --config path/to/config.yaml
```

**Delete task files**
```python
delete-tasks --config path/to/config.yaml
```

# Directory Structure

### Explanation of Key Files:
- `openai_batch_api`: The main package directory containing the core functionalities.
  - `create_batch_and_submit.py`: Script to create and submit tasks in batches.
  - `status_jobs.py`: Script to check the status of submitted jobs.
  - `collate_output.py`: Script to collate the outputs of completed jobs.
  - `delete_tasks.py` : Script to delete intermediate task outputs.
  - `utils.py`: Utility functions for common operations like loading configurations and creating tasks.
- `setup.py`: Contains the configuration for packaging and distribution.
- `README.md`: Documentation for the repository.
- `requirements.txt`: List of dependencies required to run the module.

