import threading, logging
from config.logger import setup_logging
from config.tasks import queue_names, schedules
from modules.rabbitMQ import listen_queue
from modules.scheduler import start_periodic_task

def main():
    for queue_name, func in queue_names.items():
        listener_thread = threading.Thread(target=listen_queue, args=(queue_name, func))
        listener_thread.daemon = True
        listener_thread.start()

    start_all_tasks(schedules)
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        logging.info("Stopped by user.")

def start_all_tasks(schedules):
    stop_events = {}
    for task_name, task_info in schedules.items():
        logging.info(f"Starting task: {task_name}")
        stop_event = start_periodic_task(task_info['frequency'], task_info['function'])
        stop_events[task_name] = stop_event
    return stop_events

if __name__ == "__main__":
    setup_logging()
    main()
