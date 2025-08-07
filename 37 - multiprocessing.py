import multiprocessing

def worker(num):
    """Function to be executed by each process."""
    print(f'Worker: {num}')

if __name__ == '__main__':
    # Create 5 processes
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All processes completed.")


import multiprocessing

def test(n):
    print(f"Number {n}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=test, args=(123,))
    p2 = multiprocessing.Process(target=test, args=(456,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("All processes completed.")

