# datamodels

Idiomatic Python Dataclasses inspired by Pydantic

```python
from datamodels import DataModel
from datamodels import exceptions


class Request(DataModel):
    data: dict
    producer: int
    consumer: int
    
```
