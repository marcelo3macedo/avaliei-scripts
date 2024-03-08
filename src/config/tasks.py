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