import subprocess
import sys
import os

def run_analysis_demo():
    """Run a demonstration of the statistical analysis tool"""

    print("Demonstration of Research Statistical Analysis Tool")
    print("="*50)

    # Check if required files exist
    if not os.path.exists("sample_data.csv"):
        print("Error: sample_data.csv not found!")
        return

    if not os.path.exists("research_stats_analyzer.py"):
        print("Error: research_stats_analyzer.py not found!")
        return

    print("\nRunning analysis on sample data...")
    print("Command: python research_stats_analyzer.py sample_data.csv --project-name 'Demo Analysis'")

    try:
        # Run the analysis tool
        result = subprocess.run([
            sys.executable,
            "research_stats_analyzer.py",
            "sample_data.csv",
            "--project-name",
            "Demo Analysis"
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("\n✓ Analysis completed successfully!")
            print(result.stdout)

            # Check if output file was created
            expected_output = "sample_data_analysis.md"
            if os.path.exists(expected_output):
                print(f"\n✓ Report generated: {expected_output}")

                # Show first few lines of the report
                with open(expected_output, 'r') as f:
                    lines = f.readlines()[:10]  # First 10 lines

                print("\nFirst few lines of the report:")
                print("-" * 30)
                for line in lines:
                    print(line.rstrip())

            else:
                print(f"\n⚠ Expected output file {expected_output} was not created")

            # Check if plots directory was created
            if os.path.exists("plots") and os.listdir("plots"):
                print(f"\n✓ Plots generated in 'plots' directory:")
                for plot_file in os.listdir("plots"):
                    print(f"  - {plot_file}")
            else:
                print("\n⚠ No plots were generated")

        else:
            print(f"\n✗ Analysis failed with return code {result.returncode}")
            print("Error output:")
            print(result.stderr)

    except Exception as e:
        print(f"\n✗ An error occurred while running the analysis: {str(e)}")

def run_ttest_demo():
    """Run a demonstration of the t-test functionality"""

    print("\n" + "="*50)
    print("T-Test Demonstration")
    print("="*50)

    print("\nRunning analysis with group comparison...")
    print("Command: python research_stats_analyzer.py sample_data.csv --group-col 'group' --value-col 'income' --project-name 'Group Comparison Demo'")

    try:
        result = subprocess.run([
            sys.executable,
            "research_stats_analyzer.py",
            "sample_data.csv",
            "--group-col", "group",
            "--value-col", "income",
            "--project-name", "Group Comparison Demo"
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("\n✓ T-test analysis completed successfully!")
            print(result.stdout)
        else:
            print(f"\n✗ T-test analysis failed with return code {result.returncode}")
            print("Error output:")
            print(result.stderr)

    except Exception as e:
        print(f"\n✗ An error occurred while running the t-test analysis: {str(e)}")

if __name__ == "__main__":
    run_analysis_demo()
    run_ttest_demo()