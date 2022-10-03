# datamodels

Ideomatic and lightweight Python dataclasses inspired by Pydantic

- Installation `pip install git+https://github.com/codefather-labs/datamodels.git`

```python
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
```
