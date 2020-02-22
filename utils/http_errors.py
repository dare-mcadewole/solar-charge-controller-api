from flask_json import JsonError

InvalidMethod = JsonError(
    description = 'Invalid HTTP method',
    code = 405
)
