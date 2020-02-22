from utils.mongo import MongoDB


class Component:
    @staticmethod
    def save (component, value):
        MongoDB.get_db().components.replace_one({
            'component': component
        }, {
            'component': component,
            'value': value
        }, True)

    @staticmethod
    def get (component):
        foundComponent = MongoDB.get_db().components.find_one({
            'component': component
        })
        if foundComponent:
            del foundComponent['_id']
        return foundComponent
