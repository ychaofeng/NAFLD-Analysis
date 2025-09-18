# Project Overview

The **MASH Analysis** project is designed for analyzing RNA-seq data from the GSE167523 dataset. This project includes data downloading, preprocessing, analysis, and visualization of results.

## Project Structure

- **data/**: Contains all data-related files.
  - **raw/**: Directory for raw data files.
  - **processed/**: Directory for cleaned and transformed data files.
  - **results/**: Directory for storing analysis results.

- **notebooks/**: Jupyter notebooks for interactive analysis.
  - **01_data_download.ipynb**: Downloads the GSE167523 dataset.
  - **02_preprocessing.ipynb**: Preprocesses the downloaded data.
  - **03_analysis.ipynb**: Analyzes the processed data.

- **src/**: Source code for data processing and analysis.
  - **data/**: Contains data preprocessing scripts.
    - **preprocessing.py**: Functions for cleaning and normalizing data.
  - **analysis/**: Contains analysis scripts.
    - **differential_expression.py**: Functions for differential expression analysis.
  - **visualization/**: Contains visualization scripts.
    - **plots.py**: Functions for generating plots and charts.

- **tests/**: Contains unit tests for the project.
  - **test_preprocessing.py**: Tests for the preprocessing functions.

- **environment.yml**: Conda environment configuration file.

- **requirements.txt**: Lists required Python packages.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/ychaofeng/mash-analysis.git
   cd mash-analysis
   ```

2. Create a conda environment using the `environment.yml` file:
   ```
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```
   conda activate mash-analysis
   ```

4. Install additional packages if needed using `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

- Use the Jupyter notebooks for interactive data analysis.
- Run the notebooks in the order provided to ensure proper data flow.
- Refer to the scripts in the `src` directory for reusable functions and methods.
- Use the `tests` directory to run unit tests and ensure code reliability.

## License

This project is licensed under the MIT License.