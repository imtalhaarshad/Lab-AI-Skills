# Research Statistical Analysis Tool

This tool performs comprehensive statistical analysis on research project data and generates detailed reports in markdown format.

## Overview

The Research Statistical Analysis Tool is a Python-based utility that helps researchers perform various statistical analyses on their data, including:

- Descriptive statistics (mean, median, standard deviation, quartiles, etc.)
- Correlation analysis between numerical variables
- Hypothesis testing (t-tests for comparing two groups)
- Data visualization (histograms, correlation heatmaps)
- Comprehensive markdown reporting

## Features

- **Descriptive Statistics**: Calculate key statistics for numerical variables
- **Correlation Analysis**: Analyze relationships between variables
- **Hypothesis Testing**: Compare means between two groups using t-tests
- **Visualizations**: Generate plots to visualize data distributions and relationships
- **Markdown Reports**: Save results in a well-formatted markdown document
- **Flexible Input**: Accepts CSV files with various data types

## Prerequisites

- Python 3.6 or higher
- Required packages:
  - pandas
  - numpy
  - scipy
  - matplotlib
  - seaborn

Install dependencies using:
```bash
pip install pandas numpy scipy matplotlib seaborn
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

## Supported Data Types

The tool automatically handles:
- Numerical data (integers, floats) - for statistical calculations
- Categorical data (strings) - for grouping and descriptive summaries
- Missing values (NaN) - with appropriate handling in calculations

## Report Sections

The generated markdown report includes:

- **Dataset Overview**: Basic information about the dataset
- **Descriptive Statistics**: Detailed statistics for each numerical variable
- **Correlation Analysis**: Relationship matrix between variables
- **Hypothesis Testing**: Statistical analysis comparing groups

## Hypothesis Testing
The tool supports various hypothesis testing methods:

- **Independent T-Test**: Compare means between two independent groups
- **Paired T-Test**: Compare means between two related groups (when specified)
- **Statistical Significance**: Results include p-values, confidence intervals, and effect sizes
- **Assumption Checks**: Tests for normality and equal variances where applicable

The output includes:
- Null and alternative hypotheses
- Test statistic value
- Degrees of freedom
- P-value and significance interpretation
- Confidence intervals for mean differences

## Error Handling
The tool implements robust error handling for:

- **File Errors**: Invalid file paths, unreadable files, incorrect file formats
- **Data Validation**: Empty datasets, insufficient data for statistical tests
- **Column Issues**: Missing specified columns, incorrect column names
- **Statistical Errors**: Violation of test assumptions, non-numeric data in numeric operations
- **Memory Issues**: Large datasets that exceed available memory

Common error messages include:
- "File not found: [filename]" - Check file path and permissions
- "Invalid CSV format" - Verify the file contains properly formatted CSV data
- "Insufficient data for analysis" - Ensure adequate sample sizes for statistical tests
- "Non-numeric data in specified column" - Verify column contains numeric values for statistical operations

## Security Considerations
- **Input Validation**: The tool validates file inputs to prevent path traversal attacks
- **Data Privacy**: Handles sensitive data responsibly; consider anonymizing personal information before analysis
- **File Access**: Runs with minimal required permissions to access only specified data files
- **Dependency Security**: Keep all Python packages updated to address known vulnerabilities

## Limitations
- **Sample Size Requirements**: Statistical tests require adequate sample sizes for reliable results
- **Assumption Dependencies**: Parametric tests assume normal distribution and equal variances
- **Correlation vs. Causation**: The tool identifies correlations but cannot infer causation
- **Missing Data**: Statistical analyses may be affected by high percentages of missing values
- **Variable Type Restrictions**: Limited to numerical and categorical data types
- **Single Comparison Tests**: Currently supports only two-group comparisons (t-tests), not ANOVA for multiple groups

## Future Enhancements
- **Advanced Statistical Tests**: ANOVA, chi-square tests, regression analysis
- **Non-parametric Alternatives**: Mann-Whitney U, Wilcoxon signed-rank tests
- **Time Series Analysis**: Support for temporal data patterns
- **Interactive Mode**: Command-line wizard for users unfamiliar with parameters
- **Export Options**: Additional formats (PDF, HTML, Excel)
- **Custom Visualizations**: User-configurable plot types and styling
- **Data Preprocessing**: Built-in data cleaning and transformation tools

## Troubleshooting
**Q: The correlation matrix shows NaN values**
A: This occurs when there are insufficient paired observations or non-numeric data in the columns. Check your data for non-numeric entries or missing values.

**Q: T-test returns "p-value = NaN"**
A: This indicates insufficient data points in one or both groups, or identical values in a group. Verify that each group has multiple unique values and sufficient sample size.

**Q: Tool crashes with large datasets**
A: For large datasets, consider sampling a subset of your data or increasing system memory allocation.

**Q: Installation fails with dependency conflicts**
A: Try installing in a clean virtual environment: `python -m venv stats_env && source stats_env/bin/activate && pip install ...`

**Q: Plots don't save correctly**
A: Ensure the output directory has write permissions and sufficient disk space.