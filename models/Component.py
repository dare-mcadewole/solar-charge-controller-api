from utils.mongo import MongoDB

id = {
    '_id': '5e50976ee7ec260b92208aef'
}


class Component:
    @staticmethod
    def save (components):
        MongoDB.get_db().components.replace_one(id, components, True)

    @staticmethod
    def get ():
        foundComponent = MongoDB.get_db().components.find_one(id)
        if foundComponent:
            del foundComponent['_id']
        return foundComponent
