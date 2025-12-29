#!/usr/bin/env python
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(message)s")

parser = argparse.ArgumentParser()
parser.add_argument(
    "-l", "--report_name_list", nargs="+", help="<Required> Set flag", required=True
)
args = parser.parse_args()

for report_name in args.report_name_list:
    path = r"assets\notebooks"
    notebook = rf"{path}\{report_name}.ipynb"
    html = rf"{path}_html\{report_name}.html"

    # read source notebook
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)
        logging.info(f"Finished reading notebook {notebook} into memory")

    # execute notebook
    ep = ExecutePreprocessor(timeout=-1, kernel_name="python3")
    ep.preprocess(nb)
    logging.info(f"Finished processing the notebook")

    # export to html
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = True
    html_exporter.exclude_input_prompt = True
    html_exporter.exclude_output_prompt = True
    html_data, _ = html_exporter.from_notebook_node(nb)
    logging.info(f"Finished converting {notebook} to {html}")

    # write to output file
    try:
        with open(html, "w") as f:
            f.write(html_data)
            logging.info(f"Finished writing to {html}")
    except Exception as e:
        logging.exception(e)
        raise e
