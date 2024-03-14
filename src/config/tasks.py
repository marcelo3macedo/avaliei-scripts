from queues.feeder import feed_update_user_ratings, feed_generate_reports, feed_check_subscriptions, feed_get_metrics
from queues.update_user_ratings import update_user_ratings
from queues.generate_reports import generate_reports
from queues.check_subscriptions import check_subscriptions
from queues.remove_access import remove_access
from queues.get_metrics import get_metrics

queue_names = {
    'update_user_ratings': update_user_ratings,
    'generate_reports': generate_reports,
    'check_subscriptions': check_subscriptions,
    'remove_access': remove_access,
    'get_metrics': get_metrics,
}

schedules = {
    'update_user_ratings': { 
        'function': feed_update_user_ratings,
        'frequency': 3600
    },
    'generate_reports': { 
        'function': feed_generate_reports,
        'frequency': 3600
    },
    'check_subscriptions': { 
        'function': feed_check_subscriptions,
        'frequency': 3600
    },
    'get_metrics': { 
        'function': feed_get_metrics,
        'frequency': 86400
    }
}