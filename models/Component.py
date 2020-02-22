from utils.mongo import MongoDB


class Component:
    @staticmethod
    def save (component, value):
        return MongoDB.get_db().components.find({
            'component': component
        }).upsert().updateOne({
            component: value
        })

    @staticmethod
    def get (component):
        return MongoDB.get_db().components.find_one({
            'component': component
        })
