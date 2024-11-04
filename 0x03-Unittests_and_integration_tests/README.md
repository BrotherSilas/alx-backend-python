# 0x03 - Unittests and Integration Tests

This project focuses on unit and integration testing in Python, including parameterized tests, mocking, and patching. By creating test cases for functions and classes, we ensure that code runs as expected and is resilient against changes.

## Table of Contents
- [Description](#description)
- [Project Requirements](#project-requirements)
- [Files](#files)
- [Tasks](#tasks)
  - [Task 0: Parameterize a Unit Test](#task-0-parameterize-a-unit-test)
  - [Task 1: Test Exceptions with Parameterization](#task-1-test-exceptions-with-parameterization)
  - [Task 2: Mock HTTP Calls](#task-2-mock-http-calls)
  - [Task 3: Parameterize and Patch a Method](#task-3-parameterize-and-patch-a-method)
  - [Task 4: Test a Decorated Method](#task-4-test-a-decorated-method)
  - [Task 5: Mocking a Property](#task-5-mocking-a-property)
  - [Task 6: Additional Patching](#task-6-additional-patching)
  - [Task 7: Parameterized License Test](#task-7-parameterized-license-test)
  - [Task 8: Integration Test with Fixtures](#task-8-integration-test-with-fixtures)
  - [Task 9: Advanced Integration Tests](#task-9-advanced-integration-tests)
- [Usage](#usage)
- [Author](#author)

## Description

In this project, we create unit and integration tests for utility functions and classes to validate code reliability. We use various testing techniques like parameterized testing, mocking, and patching to simulate different scenarios without calling external APIs.

## Project Requirements

- **Python version**: All files are interpreted with `Python 3.7` on Ubuntu 18.04 LTS.
- **Code Style**: Use `pycodestyle` version 2.5.
- **Documentation**:
  - All modules, classes, and functions must have comprehensive docstrings.
  - Docstrings should clearly explain the purpose and functionality.
- **Execution**:
  - All files should have executable permissions.
  - The first line of every file should be `#!/usr/bin/env python3`.

## Files

- **utils.py**: Contains utility functions.
- **client.py**: Contains the `GithubOrgClient` class for interacting with GitHub's API.
- **fixtures.py**: Contains data fixtures for integration testing.
- **test_utils.py**: Unit tests for `utils.py`.
- **test_client.py**: Unit and integration tests for `client.py`.

## Tasks

### Task 0: Parameterize a Unit Test
- Write unit tests for `utils.access_nested_map`.
- Test cases are parameterized with inputs and expected outputs.

### Task 1: Test Exceptions with Parameterization
- Write unit tests for `access_nested_map` to check for `KeyError`.
- Test with parameterized invalid inputs to ensure appropriate exceptions.

### Task 2: Mock HTTP Calls
- Write tests for `utils.get_json` using `unittest.mock.patch`.
- Mock `requests.get` to prevent actual HTTP calls.
- Validate the function output and that the HTTP call was made once.

### Task 3: Parameterize and Patch a Method
- Test memoization using the `utils.memoize` decorator.
- Ensure the decorated method is called only once despite multiple calls.

### Task 4: Test a Decorated Method
- Test `GithubOrgClient.org` using decorators to patch and parameterize.
- Validate that `get_json` is called with expected arguments.

### Task 5: Mocking a Property
- Test `_public_repos_url` using property mocking.
- Patch `GithubOrgClient.org` to return known payloads and validate results.

### Task 6: Additional Patching
- Test `public_repos` by mocking `get_json` and `_public_repos_url`.
- Validate that the method returns the correct list of repositories.

### Task 7: Parameterized License Test
- Test `has_license` with parameterized inputs and expected outputs.
- Ensure the function correctly identifies repositories with a given license.

### Task 8: Integration Test with Fixtures
- Create integration tests for `public_repos` using fixtures from `fixtures.py`.
- Use setup and teardown methods to patch requests and stop patching after tests.

### Task 9: Advanced Integration Tests
- Test `public_repos` and `public_repos_with_license` for expected results based on fixture data.
- Ensure results align with anticipated behavior when specific license types are queried.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/alx-backend-python.git
   cd alx-backend-python/0x03-Unittests_and_integration_tests
2. **Run Tests**:
python3 -m unittest discover -s . -p "test_*.py"

## Author
This project was implemented by Silas Edet as part of the ALX software engineering curriculum.
