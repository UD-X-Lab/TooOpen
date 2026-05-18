# DNS Feature Generation

This directory contains two equivalent implementations for generating three DNS query features:

- `features_generation.py`: command-line Python script
- `features_generation.ipynb`: step-by-step Jupyter Notebook

The generated features are:

| Output column | Meaning |
| --- | --- |
| `Dvs` | Number of unique queried domains in the recent `N` requests from the same source IP |
| `Str` | Number of unique source IPs in the recent `M` requests for the same domain |
| `Fth` | Number of occurrences of the current domain in the recent `K` requests from the same source IP |

## Input CSV requirements

Each input CSV file must contain at least these columns:

- `source IP (anonymized)`
- `domain/URL/name`

If your CSV uses `source IP` instead of `source IP (anonymized)`, change `SOURCE_IP_COLUMN` in the script or notebook before running it.

The output files preserve the other input columns and append `Dvs`, `Str`, and `Fth`. 

<!-- If an input file already contains older feature columns such as `Unique Request Count`, `Unique Src IP`, `Domain Query Count`, `Dvs.`, `Str.`, or `Fth.`, they are removed before the new columns are written. -->

## Window sizes

The paper reports `N = 5000`, where the same window size is used for all three features. The code keeps the three windows configurable:

- `N`: window size for `Dvs`
- `M`: window size for `Str`
- `K`: window size for `Fth`

To reproduce the paper setting, use:

```text
N = 5000
M = 5000
K = 5000
```

## File order

Sliding-window state is preserved across files. If the input directory contains more than one CSV file, filenames must sort from the oldest file to the newest file in chronological order. For example:

```text
2025-01-01.csv
2025-01-02.csv
2025-01-03.csv
```

The code processes files with `sorted(input_folder.glob("*.csv"))`, so filename order is the processing order.

## Use the Python script

Run:

```powershell
python3 features_generation.py <input_folder> <output_folder> --n 5000 --m 5000 --k 5000
```

Example:

```powershell
python3 features_generation.py "D:\dns\input" "D:\dns\output" --n 5000 --m 5000 --k 5000
```

Parameters:

| Parameter | Required | Description |
| --- | --- | --- |
| `input_folder` | Yes | Folder containing input CSV files |
| `output_folder` | Yes | Folder where generated CSV files will be written |
| `--n` | No | Window size for `Dvs`; default: `5000` |
| `--m` | No | Window size for `Str`; default: `5000` |
| `--k` | No | Window size for `Fth`; default: `5000` |
| `--overwrite` | No | Overwrite output files that already exist |

Without `--overwrite`, existing output files are skipped.

## Use the Jupyter Notebook

Open `features_generation.ipynb` and run the cells from top to bottom.

In the first code cell, set:

```python
INPUT_FOLDER = Path(r"path/to/input_csv_folder")
OUTPUT_FOLDER = Path(r"path/to/output_csv_folder")
N = 5000
M = 5000
K = 5000
OVERWRITE = False
```

Then continue running the remaining cells in order. The notebook contains the same processing logic as the Python script, but exposes the workflow step by step.
