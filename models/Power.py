from utils.mongo import MongoDB
from datetime import datetime
import pprint


def get_date ():
    today = datetime.now()
    return datetime(
        today.year,
        today.month,
        today.day
    )


class Power:
    @staticmethod
    def save (power):
        MongoDB.get_db().power.insert_one({
            'power': int(power),
            'created_date': datetime.utcnow()
        })

    @staticmethod
    def get ():
        power = MongoDB.get_db().power.find_one()
        if power:
            del power['_id']
        return power

    @staticmethod
    def get_by_date(date = get_date(), end=None):
        query = {
            # 'created_date': {
            #     '$gte': date,
            #     '$lt': end
            # } if end else date
            'power': 34
        }
        results = MongoDB.get_db().power.find(query)
        powerData = list()
        for result in results:
            del result['_id']
            powerData.append(result)
        print('Date: %s', date)
        print('Query: %s', query)
        pprint.pprint(powerData)
        return powerData
