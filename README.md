GitHub: [aio-pyrestful](https://github.com/HarryHEi/aio-pyrestful)

This is a Specialized version of [pyrestful](https://github.com/rancavil/tornado-rest)
---------

PyRestful
---------

pyRestful is an API to develop restful services with Tornado Web Server.

We made changes from the last version to improve it and make it more easy.

The last version works with Python 2 and 3.

aio_pyrestful
---------
Support asyncio.

### Install

```
pip install aio_pyrestful
```

### Example


```python
import asyncio

from aio_pyrestful.rest import get, mediatypes


@asyncio.coroutine
async def async_fun():
    await asyncio.sleep(10)
    return 'text'


@get(_path='/configure', _produces=mediatypes.APPLICATION_JSON)
@asyncio.coroutine
async def post_configure(self):
    text = await async_fun()
    return {
        'text': text
    }
```
