import logging
from dao.user_ratings import UserRatingsDAO
from dao.kpis import KpisDAO

def update_user_ratings(message):
    logging.info(f"update_user_ratings - {message}")
    
    user_ratings_dao = UserRatingsDAO()
    kpis_dao = KpisDAO()

    results = user_ratings_dao.fetch_user_ratings()

    if results is None:
        return
    
    for r in results:
        logging.info(f"update_user_ratings - {r['userId']}")

        kpis_dao.insert_kpi_data(
            r['userId'],
            r['volDaily'],
            r['volGeneral'],
            r['pontDaily'],
            r['pontGeneral']
        )
