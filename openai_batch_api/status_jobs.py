import argparse
import os
from datetime import datetime

import pandas as pd
import requests
from tabulate import tabulate

from openai_batch_api.utils import load_config


def fetch_batches(api_key):
    """Fetches all batches from the API and returns them as a list."""
    url = "https://api.openai.com/v1/batches"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("Failed to fetch batches")
        return []


def fetch_batch_details(api_key, batch_id):
    """Fetches and displays details of a specific batch."""
    url = f"https://api.openai.com/v1/batches/{batch_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        batch = response.json()
        return batch
    else:
        print("Failed to fetch batch details")
        return None


def display_batches(batches, batch_submit_data):
    batch_details = []
    for batch in batches:
        try:
            in_progress_at = datetime.fromtimestamp(batch["in_progress_at"])
        except TypeError:
            in_progress_at = None
        batch_data = (
            batch["id"],
            batch["status"],
            datetime.fromtimestamp(batch["created_at"]),
            in_progress_at,
            batch["request_counts"]["completed"],
            batch["request_counts"]["failed"],
            batch["request_counts"]["total"],
        )
        batch_details.append(batch_data)
    headers = [
        "batch_id",
        "status",
        "created_at",
        "in_progress_at",
        "completed",
        "failed",
        "total",
    ]
    batch_details = pd.DataFrame(batch_details, columns=headers)
    batch_subset = pd.read_csv(batch_submit_data)
    batch_ids = list(batch_subset["batch_id"])
    batch_details = batch_details[
        batch_details["batch_id"].isin(batch_ids)
    ]  # Filter out results based on current submitted data
    table = tabulate(batch_details, headers=headers, tablefmt="fancy_grid")
    print(table)


def main():
    parser = argparse.ArgumentParser(description="Create and submit batch tasks.")
    parser.add_argument("--config", required=True, help="Path to configuration YAML")
    args = parser.parse_args()

    config_file = args.config
    config = load_config(config_file)
    data_path = config["data_path"]
    batch_data_path = f"{data_path}/batch_submit_data.csv"

    if not os.path.exists(batch_data_path):
        print("Looks like you have not submitted any jobs yet")
        return

    API_KEY = os.getenv("OPENAI_API_KEY")

    if API_KEY is None:
        print("Error: OPENAI_API_KEY environment variable not set.")
        return

    batches = fetch_batches(API_KEY)
    display_batches(batches, batch_data_path)


if __name__ == "__main__":
    main()
