import pytest, logging
def pytest_collection_modifyitems(config, items):

    for item in items:
        if "sequential" in item.name:
            item.add_marker(pytest.mark.sequential)
        else:
            item.add_marker(pytest.mark.parallel)


@pytest.fixture(scope="session", autouse=True)
def setup_logging(request):
    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d][%(levelname)s]:[%(filename)s][%(lineno)s] - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Determine worker ID for pytest-xdist
    worker_id = request.config.workerinput['workerid'] if hasattr(request.config, 'workerinput') else 'master'
    
    file_handler = logging.FileHandler(filename=f'pytest_worker_{worker_id}.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s.%(msecs)03d][%(levelname)s]:[%(filename)s][%(lineno)s] - %(message)s'))
    logging.getLogger().addHandler(file_handler)