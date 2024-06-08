# Sequential-Parallel-Execution-Pytest

This project demonstrates how to use subprocesses in pytest, manage logging, and run tests in parallel and sequential both.

## Project Structure

The project consists of the following files:

main_test/
├── conftest.py
├── execute.py
└── test_cases.py


conftest.py

This file configures pytest to mark test cases for sequential and parallel execution and sets up logging for each worker thread.

test_example.py

This file contains the test cases that demonstrate the use of sequential and parallel markers.

execute.py
This file runs the sequential tests on a single worker and the parallel tests on multiple workers.

To run these tests, execute:
python execute.py


cat pytest_worker_0.log
cat pytest_worker_1.log
# And so on, depending on how many workers were used
