# T20 World Cup 2024 Data Analysis Project

This project performs an exploratory data analysis (EDA) of simulated match and player statistics from the ICC Men's T20 World Cup 2024.

## Project Goal
To uncover insights into team and player performance, understand match dynamics, and identify key trends from the tournament data.

## Project Structure
- `data/`: Contains raw and processed datasets.
  - `raw/`: Original simulated CSV files (`t20wc_2024_matches.csv`, `t20wc_2024_player_stats.csv`).
  - `processed/`: Cleaned and preprocessed data (generated during analysis).
- `notebooks/`: Jupyter notebooks for data ingestion, cleaning, and exploratory analysis.
  - `01_data_ingestion_cleaning.ipynb`: Loads raw data, performs initial cleaning, and saves processed data.
  - `02_eda_and_insights.ipynb`: Conducts exploratory data analysis and visualizes key insights.
- `src/`: Python scripts containing reusable functions.
  - `data_utils.py`: Utility functions for data loading and basic transformations.
  - `analysis_utils.py`: Helper functions for specific analytical tasks.
- `reports/`: Stores analysis summaries and visualizations.
  - `t20wc_2024_summary.md`: Markdown report summarizing key findings.
- `.venv/`: Python virtual environment (ignored by Git).
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Specifies files/directories to be ignored by Git.

## How to Run the Project

### 1. Clone the Repository (Simulated)
First, make sure you have all the files and folders from this project setup in your local directory.

### 2. Set Up Virtual Environment
Navigate to the project root directory in your terminal and run:
```bash
python -m venv .venv