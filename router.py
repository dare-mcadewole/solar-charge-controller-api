from controllers.component import ComponentController
from controllers.power import PowerController

class Router:
    @staticmethod
    def initialize (app):
        # API rule for /api/component
        app.add_url_rule(
            '/api/component/<component>',
            'get-component',
            ComponentController.get_component,
            methods=[ 'GET' ]
        )

        # API rule for /api/component/update
        app.add_url_rule(
            '/api/component/update/<component>',
            'update-component',
            ComponentController.update_component,
            methods=[ 'GET', 'PUT', 'PATCH' ]
        )

        # API rule for /api/components
        app.add_url_rule(
            '/api/components',
            'get-components',
            ComponentController.get_components,
            methods=[ 'GET' ]
        )

        # API rule for /api/components
        app.add_url_rule(
            '/api/components/update',
            'update-components',
            ComponentController.update_components,
            methods=[ 'GET', 'PUT', 'PATCH' ]
        )

        # API rule for /api/power
        app.add_url_rule(
            '/api/power',
            'get-power',
            PowerController.get_power,
            methods=[ 'GET' ]
        )

        # API rule for /api/power/update
        app.add_url_rule(
            '/api/power/add',
            'add-power',
            PowerController.add,
            methods=[ 'GET', 'POST' ]
        )
