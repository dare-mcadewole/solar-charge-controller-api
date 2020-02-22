from utils.mongo import MongoDB


class Power:
    @staticmethod
    def save (power):
        MongoDB.get_db().power.insert_one({
            'power': power
        })

    @staticmethod
    def get ():
        power = MongoDB.get_db().power.find_one()
        if power:
            del power['_id']
        return power
