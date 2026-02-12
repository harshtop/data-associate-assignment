# Data Associate Assignment – Harsh Tosawad

## Objective
To design an end-to-end analytics workflow integrating public health and economic datasets to support MEAL insights.

## Data Sources
1. World Bank Open Data API
2. Our World in Data (GDP per capita dataset)

## Indicators Used
- Maternal Mortality Ratio
- Health Expenditure per Capita
- Skilled Birth Attendance
- GDP per Capita

## Workflow
- Extracted data using APIs (Python)
- Standardized country codes and years
- Filtered 2010–2022 data
- Removed nulls and duplicates
- Designed analytical dataset
- Queried data using SQL
- Built interactive Power BI dashboard

## Key Insights
- Higher health expenditure correlates with lower maternal mortality.
- Skilled birth attendance improves maternal outcomes.
- Economic context explains structural disparities.

## Setup Instructions
Install dependencies:
pip install pandas requests

Run:
python data_extraction.py 

## Output

The processed dataset (processed_health_data.csv) is automatically generated when running:

python data_extraction.py

The file will be created in the project directory after execution.
