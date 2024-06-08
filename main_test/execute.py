import subprocess

# Run sequential tests on a single worker
seq_process = subprocess.Popen(["pytest", "-n", "1", "-m", "sequential", ".\main_test"])

# Run parallel tests on multiple workers
par_process = subprocess.Popen(["pytest", "-n", "3", "-m", "parallel", ".\main_test"])

# Wait for both processes to complete
seq_process.wait()
par_process.wait()
