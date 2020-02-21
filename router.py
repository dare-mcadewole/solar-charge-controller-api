from controllers.component import ComponentController

class Router:
    @staticmethod
    def setup (app):
        app.add_url_rule('/api/component', 'component', ComponentController.get_controller)
