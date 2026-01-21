from setuptools import setup, find_packages

setup(
    name="research-statistical-analyzer",
    version="1.0.0",
    author="Research Team",
    description="A Python tool for comprehensive statistical analysis of research data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/research/statistical-analysis-tool",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
    ],
    entry_points={
        "console_scripts": [
            "research-stats-analyzer=research_stats_analyzer:main",
        ],
    },
)