import os, logging, stripe
from dao.users import UsersDAO

def check_subscriptions(message):
    logging.info(f"check_subscriptions - {message}")
    
    users_dao = UsersDAO()

    stripe.api_key = os.getenv('STRIPE_KEY', '')
    charges = stripe.Charge.list(limit=100)

    for charge in charges.get('data', []):
        if not charge.get('paid', False):
            return
        
        email = charge.get('billing_details', {}).get('email', None)
        users_dao.update_user_profile(email)

