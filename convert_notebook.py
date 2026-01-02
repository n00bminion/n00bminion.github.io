import argparse
import logging

import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(message)s")

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-n", "--report_name")
group.add_argument("-l", "--report_name_list", nargs="+")

args = parser.parse_args()

if args.report_name:
    args.report_name_list = [args.report_name]

for report_name in args.report_name_list:
    path = r"assets\notebooks"
    notebook = rf"{path}\{report_name}.ipynb"
    html_dir = rf"{path}_html"
    output_dir = rf"--output-dir='{html_dir}'"
    logging.info(f"Begin converting to html for {notebook}")
    command = (
        f"jupyter nbconvert {output_dir} --to html --no-input --no-prompt {notebook}  "
    )
    logging.info(f"Running command: {command}")
    os.system(command)
    logging.info(f"Finish converting notebook to {html_dir}")
