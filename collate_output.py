import os

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

from utils import load_config, load_input_file, parse_result_output

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

config = load_config("config.yaml")
input_file = config["input_file"]
id_column = config["id_column"]
output_file = config["output_file"]

batch_data_file = config["batch_submit_data"]
data_path = config["data_path"]
batch_file = os.path.join(data_path, batch_data_file)
batch_df = pd.read_csv(batch_file)

results_data = []
for idx, row in batch_df.iterrows():
    batch_id = row["batch_id"]
    batch_job = client.batches.retrieve(batch_id=batch_id)
    result_file_id = batch_job.output_file_id
    result = client.files.content(result_file_id).content
    result = result.decode("utf-8")
    result = result.splitlines()
    for line in result:
        results_data.append((parse_result_output(line)))

results_data_df = pd.DataFrame(results_data, columns=[f"{id_column}", "api_output"])
input_df = load_input_file(input_file)

# To account for possible alphanumeric id's
input_df[id_column] = input_df[id_column].astype(str)

output_df = pd.merge(input_df, results_data_df, on=id_column, how="left")
output_df.to_pickle(output_file)
