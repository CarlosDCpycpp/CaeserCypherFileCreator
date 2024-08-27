import os
import time
import keyboard


def terminate():
    print("Press any key to exit the program...")
    keyboard.read_event()
    exit()


def time_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f'Function "{func.__name__}" took {elapsed_time:.4f} seconds to execute.\n')
        return result  # Return the result of the function
    return wrapper


def prepare(str_):
    return str_.lower().replace(" ", "")


if __name__ == "__main__":
    print("Nothing to see here...")
    terminate()
