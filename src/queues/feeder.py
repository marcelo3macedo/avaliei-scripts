from modules.rabbitMQ import send_message

def feed_update_user_ratings():
    send_message('update_user_ratings', 'processing')

def feed_generate_reports():
    send_message('generate_reports', 'processing')

def feed_check_subscriptions():
    send_message('check_subscriptions', 'processing')

def feed_remove_access():
    send_message('remove_access', 'processing')