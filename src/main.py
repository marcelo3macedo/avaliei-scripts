import threading
from modules.rabbitMQ import listen_queue
from modules.scheduler import start_periodic_task
from queues.feeder import feed_update_user_ratings, feed_generate_reports
from queues.update_user_ratings import update_user_ratings
from queues.generate_reports import generate_reports
from queues.check_subscriptions import check_subscriptions
from queues.remove_access import remove_access

queue_names = {
    'update_user_ratings': update_user_ratings,
    'generate_reports': generate_reports,
    'check_subscriptions': check_subscriptions,
    'remove_access': remove_access,
}

schedules = {
    'update_user_ratings': { 
        'function': feed_update_user_ratings,
        'frequency': 3600
    },
    'generate_reports': { 
        'function': feed_generate_reports,
        'frequency': 3600
    }
}

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
        print("Stopped by user.")

def start_all_tasks(schedules):
    stop_events = {}
    for task_name, task_info in schedules.items():
        print(f"Starting task: {task_name}")
        stop_event = start_periodic_task(task_info['frequency'], task_info['function'])
        stop_events[task_name] = stop_event
    return stop_events

if __name__ == "__main__":
    main()
