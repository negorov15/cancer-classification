#!/usr/bin/env python3
"""Execute a Jupyter notebook and write an executed copy.

Usage: python3 scripts/run_notebook.py path/to/notebook.ipynb [output.ipynb]
"""
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def main():
    if len(sys.argv) < 2:
        print("Usage: run_notebook.py notebook.ipynb [output.ipynb]")
        sys.exit(2)

    nb_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else nb_path.replace('.ipynb', '_executed.ipynb')

    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=1200, kernel_name='python3')

    try:
        ep.preprocess(nb, {'metadata': {'path': '.'}})
    except Exception as e:
        print(f"Notebook execution failed: {e}")

    with open(out_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"Executed notebook written to: {out_path}")


if __name__ == '__main__':
    main()