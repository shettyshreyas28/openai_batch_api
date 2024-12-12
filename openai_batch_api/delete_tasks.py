import argparse
import os
import shutil

import pandas as pd

from openai_batch_api.utils import load_config


def main():
    parser = argparse.ArgumentParser(description="Delete the intermediate task files")
    parser.add_argument("--config", required=True, help="Path to configuration YAML")
    args = parser.parse_args()

    config_file = args.config
    config = load_config(config_file)
    data_path = config["data_path"]

    # Check if we are purging files after collation is done
    collation_status_file = os.path.join(data_path, "collation.done")

    if not os.path.exists(data_path):
        print("No tasks created yet. Nothing to delete")
        return

    if os.path.exists(collation_status_file):
        check = input(f"Are you sure you want to delete {data_path}")
        if check == "y" or check == "Y":
            shutil.rmtree(data_path)
    else:
        print(
            "Looks like you have not yet collated the results. Please run collate and then purge"
        )
        return


if __name__ == "__main__":
    main()
