# Research Statistical Analysis Skill

This repository contains a Python-based tool for performing comprehensive statistical analysis on research project data.

## Overview

The Research Statistical Analysis Tool helps researchers perform various statistical analyses on their data, including:

- Descriptive statistics (mean, median, standard deviation, quartiles, etc.)
- Correlation analysis between numerical variables
- Hypothesis testing (t-tests for comparing two groups)
- Data visualization (histograms, correlation heatmaps)
- Comprehensive markdown reporting

## Prerequisites

- Python 3.6 or higher
- Required packages listed in `requirements.txt`

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage
```bash
python research_stats_analyzer.py <input_file.csv>
```

### Advanced Usage
```bash
python research_stats_analyzer.py <input_file.csv> \
  --group-col <group_column> \
  --value-col <value_column> \
  --project-name "My Research Project" \
  --output "my_analysis_report.md"
```

### Parameters

- `<input_file>`: Path to the input CSV file containing your research data
- `--group-col`: Column name for grouping variable (for t-test comparison)
- `--value-col`: Column name for value variable (for t-test comparison)
- `--project-name`: Name of the research project (default: "Research Project")
- `--output`: Output markdown file name (auto-generated if not specified)

## Output

The tool generates:

1. A comprehensive markdown report with:
   - Dataset overview
   - Descriptive statistics tables
   - Correlation matrix
   - Hypothesis test results
   - Analysis recommendations
2. Visualization files (PNG format) referenced in the markdown report

## Example

```bash
python research_stats_analyzer.py survey_data.csv --project-name "Survey Analysis" --output "survey_analysis.md"
```

This will create a `survey_analysis.md` file with complete statistical analysis of the survey data.

## Contributing

Feel free to submit issues or pull requests to improve this tool.

## License

This project is available for use under the terms specified by the owner.