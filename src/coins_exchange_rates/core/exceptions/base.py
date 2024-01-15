
class BaseAPIException(Exception):
    status_code = 500
    code = 'exception'
    message = 'Error!'

    def __init__(self, loc=None, **kwargs):
        self.context = kwargs
        self.loc = [['body'] + location for location in loc] if loc else [['body']]

    def to_json(self):
        return {
            'code': self.code,
            'context': self.context,
            'detail': [
                {
                    'location': loc,
                    'message': self.context.get('message', self.message)
                } for loc in self.loc
            ]
        }
