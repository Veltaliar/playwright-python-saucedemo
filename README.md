# Playwright Python SauceDemo

This repository contains automated tests for the SauceDemo website using Playwright and Python. The tests are designed to validate the functionality and visual appearance of the application across various pages and scenarios.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)
- [Visual Testing](#visual-testing)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
playwright-python-saucedemo/
├── conftest.py          # Test fixtures and setup
├── pytest.ini           # Pytest configuration
├── requirements.txt     # Python dependencies
├── setup.cfg            # Code style configuration
├── data/                # Test data (URLs, credentials, error messages, etc.)
├── pages/               # Page Object Model (POM) classes
├── tests/               # Functional tests
├── tests_visual/        # Visual regression tests
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Veltaliar/playwright-python-saucedemo.git
   cd playwright-python-saucedemo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Running Tests

### Functional Tests
To run functional tests:
```bash
pytest tests/
```

### Visual Regression Tests
To run visual regression tests:
```bash
pytest tests_visual/
```

## Visual Testing
Visual regression tests use snapshots to compare the visual appearance of pages. Snapshots are stored in the `tests_visual/snapshots/` directory. If a test fails due to visual differences, you can update the snapshots by running:
```bash
pytest tests_visual/ --update-snapshots
```

## Dependencies
The project uses the following key dependencies:

- [Playwright](https://playwright.dev/python/) for browser automation
- [Pytest](https://docs.pytest.org/) for test execution
- [pytest-playwright](https://github.com/microsoft/playwright-pytest) for Playwright integration with Pytest
- [pytest-playwright-visual](https://github.com/microsoft/playwright-pytest-visual) for visual regression testing

For a full list of dependencies, see [requirements.txt](./requirements.txt).