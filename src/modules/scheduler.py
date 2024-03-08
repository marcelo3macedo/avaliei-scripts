import threading
import time

def start_periodic_task(interval, callback):
    """
    Starts a periodic task that runs a callback function at a specified interval.

    :param interval: The interval time in seconds between executions of the callback.
    :param callback: The callback function to execute.
    """
    def task_wrapper():
        while not stop_event.is_set():
            callback()
            time.sleep(interval)

    stop_event = threading.Event()

    task_thread = threading.Thread(target=task_wrapper)
    task_thread.start()

    return stop_event

def stop_periodic_task(stop_event):
    """
    Stops the periodic task.

    :param stop_event: The event object returned by start_periodic_task function used to stop the task.
    """
    stop_event.set()
