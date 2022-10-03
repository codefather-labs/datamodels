# datamodels

Ideomatic and lightweight Python dataclasses inspired by [Pydantic](https://github.com/pydantic/pydantic)

- Installation `pip install git+https://github.com/codefather-labs/datamodels.git`

```pycon
from datamodels import DataModel
from datamodels import exceptions


class Request(DataModel):
    data: dict
    producer: int
    consumer: int
    

request = Request(
    data={},
    producer=1,
    consumer=2,
)
>>> <Request data: dict={}, producer: int=1, consumer: int=2>
```

```pycon
# statictypes by default is True
request = Request(
    data={}, 
    producer=1, 
    consumer="2",
)
>>> datamodels.exceptions.InvalidType: consumer expected <class 'int'> got <class 'str'>

request = Request(
    data={}, 
    producer=1, 
    consumer=2,
)

request.update({
    "producer": "3"
})
>>> datamodels.exceptions.InvalidType: Can't assign undeclared type of attribute 'producer'
```

```pycon
# readonly by default is False
request = Request(
    data={},
    producer=1,
    consumer=2,
)

request.update({
    "producer": 3
})
>>> <Request data: dict={}, producer: int=3, consumer: int=2>

request = Request(
    data={},
    producer=1,
    consumer=2,
    readonly=True
)

request.update({
    "producer": 3
})
>>> datamodels.exceptions.ReadOnlyAccessError: <Request data: dict={}, producer: int=1, consumer: int=2 readonly>
```

More examples at test.py