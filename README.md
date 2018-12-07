GitHub: [aiopyrestful](https://github.com/HarryHEi/aiopyrestful)

This is a Specialized version of [pyrestful](https://github.com/rancavil/tornado-rest)
---------

PyRestful
---------

pyRestful is an API to develop restful services with Tornado Web Server.

We made changes from the last version to improve it and make it more easy.

The last version works with Python 2 and 3.

aiopyrestful
---------
Support asyncio.

### Install

```
pip install aiopyrestful
```

### Example


```python
import asyncio

from aiopyrestful.rest import get, mediatypes


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
