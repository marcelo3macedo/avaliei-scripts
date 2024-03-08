from dao.user_ratings import UserRatingsDAO
from dao.kpis import KpisDAO

def update_user_ratings(message):
    print(message)
    
    user_ratings_dao = UserRatingsDAO()
    kpis_dao = KpisDAO()

    results = user_ratings_dao.fetch_user_ratings()
    
    for r in results:
        kpis_dao.insert_kpi_data(
            r['userId'],
            r['volDaily'],
            r['volGeneral'],
            r['pontDaily'],
            r['pontGeneral']
        )
