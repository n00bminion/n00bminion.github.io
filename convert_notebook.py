import argparse
import logging

import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(message)s")

parser = argparse.ArgumentParser()
parser.add_argument(
    "-l", "--report_name_list", nargs="+", help="<Required> Set flag", required=True
)
args = parser.parse_args()


for report_name in args.report_name_list:
    path = r"assets\notebooks"
    notebook = rf"{path}\{report_name}.ipynb"
    html = rf"{path}_html"
    output_dir = rf"--output-dir='{html}'"
    logging.info(f"Begin converting to html for {notebook}")
    command = (
        f"jupyter nbconvert {output_dir} --to html --no-input --no-prompt {notebook}  "
    )
    logging.info(f"Running command: {command}")
    os.system(command)
    logging.info(f"Finish converting notebook to {html}")
