# Statistical Analysis Agent

The Statistical Analysis Agent is an autonomous research tool that performs comprehensive statistical analysis on datasets and generates detailed reports. It can process CSV files, compute various statistical measures, create visualizations, and produce markdown reports.

## Overview

The Statistical Analysis Agent is designed to assist researchers, data scientists, and analysts in performing exploratory data analysis. It automates the process of calculating descriptive statistics, correlation matrices, conducting hypothesis tests, and generating visualizations.

## Capabilities

### Core Functions
- **Data Loading**: Load and parse CSV files with various data types
- **Descriptive Statistics**: Compute mean, median, mode, standard deviation, variance, quartiles, and other summary statistics
- **Correlation Analysis**: Calculate Pearson correlation coefficients between numerical variables
- **Hypothesis Testing**: Perform t-tests to compare means between two groups
- **Data Visualization**: Generate histograms, correlation heatmaps, and other relevant plots
- **Report Generation**: Create comprehensive markdown reports with analysis results

### Input Formats
- Comma-Separated Values (CSV) files
- Tabular data with mixed data types (numerical, categorical)
- Files with missing values (NaN handling)

### Output Formats
- Markdown reports with detailed statistical analysis
- Visualizations in PNG format
- Structured data summaries

## Agent Interface

### Command Line Interface
The agent can be invoked via command line with the following parameters:

```
python research_stats_analyzer.py <input_file.csv> [OPTIONS]
```

#### Parameters
- `<input_file>`: Path to the input CSV file containing the data
- `--group-col`: Column name for grouping variable (for t-test comparison)
- `--value-col`: Column name for value variable (for t-test comparison)
- `--project-name`: Name of the research project (default: "Research Project")
- `--output`: Output markdown file name (auto-generated if not specified)

### Programmatic Interface
The agent can also be imported and used as a module:

```python
from research_stats_analyzer import load_data, descriptive_statistics, correlation_analysis, t_test_analysis

# Load data
df = load_data("my_data.csv")

# Perform analyses
desc_stats = descriptive_statistics(df)
corr_matrix = correlation_analysis(df)
ttest_result = t_test_analysis(df, "group_column", "value_column")
```

## Configuration

### Dependencies
The agent requires the following Python packages:
- pandas (for data manipulation)
- numpy (for numerical computations)
- scipy (for statistical functions)
- matplotlib (for plotting)
- seaborn (for statistical visualizations)

### Environment Setup
```bash
pip install -r requirements.txt
```

## Usage Examples

### Basic Analysis
```bash
python research_stats_analyzer.py data.csv
```
This performs basic descriptive statistics and correlation analysis on the data file.

### Group Comparison Analysis
```bash
python research_stats_analyzer.py data.csv --group-col "Treatment" --value-col "Outcome" --project-name "Clinical Trial Analysis"
```
This compares outcomes between treatment groups using a t-test.

### Custom Report Name
```bash
python research_stats_analyzer.py survey_data.csv --output "results/my_survey_analysis.md"
```
This saves the analysis report to a custom location.

## Agent Behavior

### Processing Steps
1. **Data Validation**: Checks file format and content validity
2. **Data Loading**: Reads CSV file into a DataFrame
3. **Type Detection**: Identifies numerical and categorical columns
4. **Statistical Analysis**: Computes requested statistics based on data properties
5. **Visualization Generation**: Creates plots based on data characteristics
6. **Report Compilation**: Combines all results into a markdown document
7. **Output Delivery**: Saves report and visualization files

### Error Handling
- Validates file existence and format
- Checks for sufficient data for statistical tests
- Handles missing values appropriately
- Provides informative error messages

### Performance Considerations
- Processes datasets efficiently using vectorized pandas operations
- Generates visualizations with appropriate sizing for readability
- Manages memory usage for large datasets

## Integration

### With Research Workflows
The agent can be integrated into research pipelines to automate routine statistical analysis tasks, allowing researchers to focus on interpretation and conclusions.

### As Part of Larger Systems
The modular design allows the agent to be incorporated into larger analytical platforms or automated research systems.

## Limitations

- Currently supports only CSV input format
- T-tests limited to comparing two groups
- Correlation analysis restricted to linear relationships
- Requires sufficient sample sizes for reliable statistical tests
- Cannot infer causation from correlation

## Future Extensions

- Support for additional file formats (Excel, JSON, databases)
- More advanced statistical tests (ANOVA, chi-square, regression)
- Time series analysis capabilities
- Interactive mode for guided analysis
- Export to multiple formats (PDF, HTML, Excel)