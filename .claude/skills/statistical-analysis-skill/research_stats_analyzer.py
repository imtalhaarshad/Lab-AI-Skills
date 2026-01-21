import argparse
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

def load_data(file_path):
    """Load data from CSV file"""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Invalid CSV format: {str(e)}")

def descriptive_statistics(df):
    """Calculate descriptive statistics for numerical columns"""
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numerical_cols:
        return pd.DataFrame()

    desc_stats = df[numerical_cols].describe()
    return desc_stats

def correlation_analysis(df):
    """Perform correlation analysis on numerical columns"""
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numerical_cols) < 2:
        return None

    corr_matrix = df[numerical_cols].corr()
    return corr_matrix

def t_test_analysis(df, group_col, value_col):
    """Perform t-test between two groups"""
    if group_col not in df.columns or value_col not in df.columns:
        raise ValueError(f"Specified columns '{group_col}' or '{value_col}' not found in data")

    # Get unique groups (limit to 2 for t-test)
    groups = df[group_col].dropna().unique()
    if len(groups) != 2:
        raise ValueError("T-test requires exactly 2 groups")

    group1_data = df[df[group_col] == groups[0]][value_col].dropna()
    group2_data = df[df[group_col] == groups[1]][value_col].dropna()

    if len(group1_data) < 2 or len(group2_data) < 2:
        raise ValueError("Each group must have at least 2 data points for t-test")

    # Perform t-test
    t_stat, p_value = stats.ttest_ind(group1_data, group2_data)

    # Calculate means and standard deviations
    mean1, std1 = group1_data.mean(), group1_data.std()
    mean2, std2 = group2_data.mean(), group2_data.std()

    # Effect size (Cohen's d)
    pooled_std = np.sqrt(((len(group1_data)-1)*std1**2 + (len(group2_data)-1)*std2**2) /
                         (len(group1_data) + len(group2_data) - 2))
    cohens_d = (mean1 - mean2) / pooled_std if pooled_std != 0 else 0

    results = {
        'groups': groups,
        'group1_name': groups[0],
        'group2_name': groups[1],
        'group1_size': len(group1_data),
        'group2_size': len(group2_data),
        'group1_mean': mean1,
        'group2_mean': mean2,
        'group1_std': std1,
        'group2_std': std2,
        't_statistic': t_stat,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'significant': p_value < 0.05
    }

    return results

def visualize_data(df, output_dir):
    """Create visualizations for the dataset"""
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numerical_cols:
        print("No numerical columns found for visualization.")
        return []

    plot_files = []

    # Create histograms for numerical columns
    for col in numerical_cols[:4]:  # Limit to first 4 numerical columns to avoid too many plots
        plt.figure(figsize=(8, 6))
        plt.hist(df[col].dropna(), bins=30, edgecolor='black')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')

        filename = os.path.join(output_dir, f'{col}_histogram.png')
        plt.savefig(filename)
        plt.close()
        plot_files.append(filename)

    # Create correlation heatmap if there are multiple numerical columns
    if len(numerical_cols) > 1:
        plt.figure(figsize=(10, 8))
        corr_matrix = df[numerical_cols].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                    square=True, fmt='.2f')
        plt.title('Correlation Heatmap')

        filename = os.path.join(output_dir, 'correlation_heatmap.png')
        plt.savefig(filename)
        plt.close()
        plot_files.append(filename)

    return plot_files

def generate_markdown_report(df, desc_stats, corr_matrix, t_test_results, plot_files, project_name):
    """Generate a markdown report with analysis results"""
    report = f"""# Statistical Analysis Report

**Project Name:** {project_name}
**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Dataset Shape:** {df.shape}

## Dataset Overview

The dataset contains {df.shape[0]} rows and {df.shape[1]} columns. Here are the column names and data types:

| Column Name | Data Type |
|-------------|-----------|
"""

    for col, dtype in df.dtypes.items():
        report += f"| {col} | {dtype} |\n"

    # Add descriptive statistics
    if not desc_stats.empty:
        report += f"""

## Descriptive Statistics

Descriptive statistics for numerical variables:

| Statistic | {' | '.join(desc_stats.columns)} |
|-----------|{'|'.join(['--------' for _ in desc_stats.columns])}|
"""
        for stat in desc_stats.index:
            row_values = [f"{val:.3f}" if isinstance(val, float) else str(val) for val in desc_stats.loc[stat]]
            report += f"| {stat} | {' | '.join(row_values)} |\n"

    # Add correlation analysis
    if corr_matrix is not None:
        report += f"""

## Correlation Analysis

Correlation matrix for numerical variables:

| Variable | {' | '.join(corr_matrix.columns)} |
|----------|{'|'.join(['--------' for _ in corr_matrix.columns])}|
"""
        for idx, row in corr_matrix.iterrows():
            row_values = [f"{val:.3f}" if not pd.isna(val) else "N/A" for val in row.values]
            report += f"| {idx} | {' | '.join(row_values)} |\n"

    # Add t-test results if available
    if t_test_results is not None:
        report += f"""

## Hypothesis Testing

We conducted an independent samples t-test to compare the means of '{t_test_results['group1_name']}' and '{t_test_results['group2_name']}' on the variable '{list(t_test_results.keys())[list(t_test_results.values()).index(t_test_results['group1_mean'])-5]}'.

### Results:

- **Group 1 ('{t_test_results['group1_name']}'):** Mean = {t_test_results['group1_mean']:.3f}, Std = {t_test_results['group1_std']:.3f}, n = {t_test_results['group1_size']}
- **Group 2 ('{t_test_results['group2_name']}'):** Mean = {t_test_results['group2_mean']:.3f}, Std = {t_test_results['group2_std']:.3f}, n = {t_test_results['group2_size']}
- **t-statistic:** {t_test_results['t_statistic']:.3f}
- **p-value:** {t_test_results['p_value']:.3f}
- **Effect size (Cohen's d):** {t_test_results['cohens_d']:.3f}
- **Significant difference:** {'Yes' if t_test_results['significant'] else 'No'}

Based on the p-value {(t_test_results['p_value']:.3f)}, we {'reject' if t_test_results['significant'] else 'fail to reject'} the null hypothesis at α = 0.05.
"""

    # Add visualization section
    if plot_files:
        report += f"""

## Visualizations

The following plots were generated as part of the analysis:

"""
        for plot_file in plot_files:
            # Extract just the filename for the markdown link
            filename = os.path.basename(plot_file)
            report += f"- ![{filename}]({filename})\n"

    # Add conclusion
    report += f"""

## Conclusion

This analysis provides a comprehensive overview of the dataset. The findings suggest areas for further investigation and highlight important statistical relationships within the data.

For questions about this analysis, please contact the research team.
"""

    return report

def main():
    parser = argparse.ArgumentParser(description='Research Statistical Analysis Tool')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('--group-col', dest='group_col', help='Column name for grouping variable (for t-test comparison)')
    parser.add_argument('--value-col', dest='value_col', help='Column name for value variable (for t-test comparison)')
    parser.add_argument('--project-name', dest='project_name', default='Research Project',
                        help='Name of the research project (default: "Research Project")')
    parser.add_argument('--output', dest='output_file', help='Output markdown file name (auto-generated if not specified)')

    args = parser.parse_args()

    try:
        # Load data
        df = load_data(args.input_file)
        print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

        # Create output directory
        output_dir = "plots"
        os.makedirs(output_dir, exist_ok=True)

        # Perform analyses
        desc_stats = descriptive_statistics(df)
        corr_matrix = correlation_analysis(df)

        # Perform t-test if specified
        t_test_results = None
        if args.group_col and args.value_col:
            try:
                t_test_results = t_test_analysis(df, args.group_col, args.value_col)
            except ValueError as e:
                print(f"T-test error: {str(e)}")

        # Generate visualizations
        plot_files = visualize_data(df, output_dir)
        print(f"Generated {len(plot_files)} visualization files in '{output_dir}/' directory.")

        # Generate report
        report = generate_markdown_report(df, desc_stats, corr_matrix, t_test_results, plot_files, args.project_name)

        # Determine output filename
        if args.output_file:
            output_filename = args.output_file
        else:
            base_name = os.path.splitext(os.path.basename(args.input_file))[0]
            output_filename = f"{base_name}_analysis.md"

        # Write report
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"Analysis report saved to '{output_filename}'")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()