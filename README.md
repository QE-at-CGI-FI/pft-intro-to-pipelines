# pft-intro-to-pipelines
Setting up GitHub actions pipeline for running of tests.

## Project Overview
This repository demonstrates how to set up a GitHub Actions pipeline for running Python Playwright tests.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:
   ```bash
   playwright install chromium
   ```

3. Run tests locally:
   ```bash
   pytest tests/ --verbose
   ```

## GitHub Actions Pipeline
The pipeline is configured in `.github/workflows/playwright.yml` and will:
- Set up Python 3.11
- Install dependencies from `requirements.txt`
- Install Playwright browsers
- Run all tests in the `tests/` directory
- Upload test results as artifacts

## Test Structure
- `tests/test_example.py` - Example Playwright tests demonstrating basic functionality
- Tests include page navigation, HTTP endpoint testing, and title validation

## Configuration
- `pyproject.toml` - Pytest configuration
- `requirements.txt` - Python dependencies
- `.gitignore` - Excludes test artifacts and build files
