import asyncio

from aiopyrestful.rest import RestHandler, get, post, mediatypes, RestService


class BaseHandler(RestHandler):
    def data_received(self, chunk):
        pass


class UserHandler(BaseHandler):
    """
    子网控相关
    """

    @get(_path='/data', _produces=mediatypes.APPLICATION_JSON)
    def get_data_list(self):
        res = []
        for i in range(10):
            res.append({
                'id': i,
                'name': 'user_{}'.format(i)
            })
        return res

    @get(_path='/data/{user_id}', _types=[int], _produces=mediatypes.APPLICATION_JSON)
    def get_data(self, user_id):
        return {
            'id': user_id,
            'name': 'user_{}'.format(user_id)
        }

    @post(_path='/data', _types=[int, bool, str], _produces=mediatypes.APPLICATION_JSON)
    def post_data(self, user_id, checked, name):
        return {
            'user_id': user_id,
            'checked': checked,
            'name': name
        }


REST_SETTING = {
    'cookie_secret': '23423f234342f2342c23423dcd2d3423d23d23e',
    'debug': True
}


application = RestService(
    rest_handlers=[UserHandler],
    **REST_SETTING
)

if __name__ == '__main__':
    application.listen(6767)
    loop = asyncio.get_event_loop()
    loop.run_forever()
