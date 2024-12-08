import json
import sys

import pandas as pd
import yaml


def message_builder(system_prompt, content, image_url=False, image_detail="low"):
    """
    Utility to construct messages for the API call.
    In case of image inputs, the fidelity param is chosen as low by default
    """
    messages = []
    messages.append({"role": "system", "content": system_prompt})
    if not image_url:
        messages.append({"role": "user", "content": content})
    else:
        if content:
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": content},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url, "detail": image_detail},
                        },
                    ],
                }
            )
        else:
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url, "detail": image_detail},
                        }
                    ],
                }
            )
    return messages


def load_config(config_file):
    with open(config_file) as f:
        config = yaml.safe_load(f)
    return config


def create_task(_id, prompt, content, model_params):
    task = {
        "custom_id": f"task:{_id}",  # First 5 letters are task: and the rest is identifier for each task
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {**model_params, "messages": message_builder(prompt, content)},
    }
    return task


def parse_result_output(result):
    # Based on the function to create batches, first 5 characters are "task:".
    # Refer to create_task() function
    result = json.loads(result)
    _id = result["custom_id"][5:]
    content = result["response"]["body"]["choices"][0]["message"]["content"]
    return _id, content


def load_input_file(input_file):
    # Load the input data file
    # Depending on the file type, load it appropriately
    if ".pkl" in input_file:
        df = pd.read_pickle(input_file)
    elif ".csv" in input_file:
        df = pd.read_csv(input_file)
    else:
        print(
            "We support only pkl or csv files. Please input the right input file format"
        )
        sys.exit(1)
    return df
