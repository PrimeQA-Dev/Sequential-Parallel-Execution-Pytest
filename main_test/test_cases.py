import logging
import time

def test_sequential_1():
    logging.info("test_sequential_1")
    time.sleep(2) 
    assert True
    
def test_sequential_2():
    logging.info("test_sequential_2")
    time.sleep(2) 
    assert True

def test_parallel_1():
    logging.info("test_parallel_1")
    time.sleep(2)  
    assert True

def test_parallel_2():
    logging.info("test_parallel_2")
    time.sleep(2) 
    assert True

def test_parallel_3():
    logging.info("test_parallel_3")
    time.sleep(2)  
    assert True


