from controllers.component import ComponentController
from controllers.power import PowerController

class Router:
    @staticmethod
    def setup (app):
        # API rule for /api/component
        app.add_url_rule(
            '/api/component',
            'component',
            ComponentController.handle_component,
            methods=[ 'GET', 'POST' ]
        )

        # API rule for /api/power
        app.add_url_rule(
            '/api/power',
            'power',
            PowerController.handle_power
        )
