# Statistical Analysis Skill - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [Features & Capabilities](#features--capabilities)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Command-Line Interface](#command-line-interface)
6. [Programmatic Interface](#programmatic-interface)
7. [File Structure](#file-structure)
8. [Agent Documentation](#agent-documentation)
9. [GitHub Setup](#github-setup)
10. [Best Practices](#best-practices)

---

## Overview

The Research Statistical Analysis Tool is a Python-based utility that helps researchers perform various statistical analyses on their data. It automates the process of calculating descriptive statistics, correlation matrices, conducting hypothesis tests, and generating comprehensive reports.

### What the Tool Does
- **Descriptive Statistics**: Calculate key statistics (mean, median, standard deviation, etc.)
- **Correlation Analysis**: Analyze relationships between variables
- **Hypothesis Testing**: Compare means between groups using t-tests
- **Data Visualization**: Generate plots to visualize data distributions
- **Report Generation**: Create detailed markdown reports

---

## Features & Capabilities

### Core Functions
- Load and parse CSV files with mixed data types
- Calculate descriptive statistics for numerical variables
- Compute correlation matrices between variables
- Perform t-tests to compare two groups
- Generate visualizations (histograms, correlation heatmaps)
- Create comprehensive markdown reports

### Supported Data Types
- **Numerical**: Integers, floats (for statistical calculations)
- **Categorical**: Strings (for grouping and summaries)
- **Missing Values**: Proper handling of NaN values

### Output Formats
- **Markdown Reports**: Detailed analysis results
- **Visualizations**: PNG format plots
- **Structured Data**: Tables and matrices

---

## Installation

### Prerequisites
- Python 3.6 or higher
- Git (for version control)

### Setup Process
1. **Clone or download** the repository
2. **Install dependencies** using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Required Packages
- pandas (for data manipulation)
- numpy (for numerical computations)
- scipy (for statistical functions)
- matplotlib (for plotting)
- seaborn (for statistical visualizations)

---

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

### Parameters Explained
- `<input_file>`: Path to your CSV data file
- `--group-col`: Column name for grouping (for t-test comparisons)
- `--value-col`: Column name for values (for t-test comparisons)
- `--project-name`: Name for your research project
- `--output`: Custom name for output report file

### Example Commands
```bash
# Basic analysis
python research_stats_analyzer.py data.csv

# Group comparison
python research_stats_analyzer.py data.csv --group-col "Treatment" --value-col "Outcome"

# Custom report
python research_stats_analyzer.py data.csv --project-name "Study 2026" --output "results/study_analysis.md"
```

---

## Command-Line Interface

### Syntax
```
python research_stats_analyzer.py [OPTIONS] <input_file.csv>
```

### Available Options
| Option | Description | Example |
|--------|-------------|---------|
| `--group-col` | Grouping column for t-tests | `--group-col "Gender"` |
| `--value-col` | Value column for t-tests | `--value-col "Income"` |
| `--project-name` | Project identifier | `--project-name "Survey"` |
| `--output` | Custom output file | `--output "report.md"` |

### Sample Workflow
```bash
# 1. Analyze data
python research_stats_analyzer.py sample_data.csv

# 2. Check output
# - Creates sample_data_analysis.md report
# - Generates plots in 'plots/' directory

# 3. View results
# Open sample_data_analysis.md in any markdown viewer
```

---

## Programmatic Interface

### Import Functions
```python
from research_stats_analyzer import (
    load_data,
    descriptive_statistics,
    correlation_analysis,
    t_test_analysis,
    visualize_data
)
```

### Example Usage
```python
import pandas as pd

# Load your data
df = load_data("my_data.csv")

# Perform individual analyses
desc_stats = descriptive_statistics(df)
corr_matrix = correlation_analysis(df)

# Perform t-test (if you have grouping data)
ttest_result = t_test_analysis(df, "group_column", "value_column")
```

---

## File Structure

```
statistical-analysis-skill/
├── research_stats_analyzer.py     # Main Python script
├── STATISTICAL_ANALYSIS_SKILL.md  # Main documentation
├── AGENT.md                      # Agent documentation
├── README.md                     # Project overview
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── sample_data.csv               # Sample dataset
├── demo.py                       # Usage demonstration
└── .git/                         # Git repository
```

### File Descriptions
- **research_stats_analyzer.py**: The core application that performs statistical analysis
- **STATISTICAL_ANALYSIS_SKILL.md**: Comprehensive documentation of the tool
- **AGENT.md**: Documentation treating the tool as an autonomous agent
- **README.md**: Quick start guide and project overview
- **requirements.txt**: List of required Python packages
- **sample_data.csv**: Example dataset to test the tool
- **demo.py**: Script showing how to use the tool

---

## Agent Documentation

### Agent Identity
The Statistical Analysis Agent is an autonomous research tool that independently processes data and generates reports.

### Agent Capabilities
- **Data Processing**: Automatically handles different data types
- **Statistical Analysis**: Performs various statistical computations
- **Decision Making**: Chooses appropriate analysis methods based on data
- **Reporting**: Creates structured, comprehensive reports

### Agent Behavior
1. **Validation**: Checks data quality and format
2. **Analysis**: Applies appropriate statistical methods
3. **Visualization**: Creates relevant plots based on data
4. **Reporting**: Compiles results into readable format

### Integration Points
- Can be embedded in larger data processing pipelines
- Suitable for automated analysis workflows
- Compatible with research automation tools

---

## GitHub Setup

### Prerequisites
- GitHub account
- Git installed locally
- GitHub CLI (optional but recommended)

### Upload Process
1. **Navigate to project directory**:
   ```bash
   cd "D:\Lab AI Skills\statistical-analysis-skill"
   ```

2. **Create GitHub repository**:
   - Go to GitHub.com and create new repository
   - Name it (e.g., "statistical-analysis-skill")

3. **Link and upload**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/statistical-analysis-skill.git
   git branch -M main
   git push -u origin main
   ```

### GitHub Best Practices
- Add relevant topics: `statistics`, `data-analysis`, `python`, `research`
- Pin the repository if it's important
- Consider adding a CONTRIBUTING.md file
- Use GitHub Issues for tracking improvements

---

## Best Practices

### For Researchers
- Always validate your data before analysis
- Use the sample_data.csv as a template for your datasets
- Review the generated reports for reasonableness
- Document any data preprocessing steps separately

### For Developers
- Maintain the modular design for easy extension
- Keep dependencies up to date
- Test with various data formats and sizes
- Follow Python best practices in contributions

### For Educators
- Use the tool to demonstrate statistical concepts
- Assign exercises using the sample workflow
- Encourage students to interpret, not just run, analyses
- Emphasize the importance of understanding statistical assumptions

### Data Preparation Tips
- Ensure CSV files have proper headers
- Handle missing values appropriately before analysis
- Verify data types match expected analysis
- Keep datasets reasonably sized for optimal performance

---

## Troubleshooting

### Common Issues
- **File not found**: Check file paths and permissions
- **Invalid CSV format**: Verify proper CSV formatting
- **Insufficient data**: Ensure adequate sample sizes
- **Memory issues**: Process large datasets in chunks

### Error Messages
- `"File not found"`: Verify file path and permissions
- `"Invalid CSV format"`: Check file formatting
- `"Insufficient data for analysis"`: Ensure adequate sample size
- `"Non-numeric data in specified column"`: Verify column contains numeric values

---

## Getting Help

### Resources
- Review STATISTICAL_ANALYSIS_SKILL.md for comprehensive details
- Check AGENT.md for autonomous agent concepts
- Look at demo.py for usage examples
- Examine sample_data.csv for data format expectations

### Support
- Create GitHub Issues for bugs or feature requests
- Check the documentation for usage examples
- Validate your data format against sample_data.csv

---

*This documentation was created to provide a complete guide to using the Statistical Analysis Skill. For the most up-to-date information, always refer to the files in your repository.*