import threading

def worker(num):
    """Function to be executed by each thread."""
    print(f'Worker: {num}')

if __name__ == '__main__':
    # Create 5 threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("All threads completed.")
