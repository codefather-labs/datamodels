from datamodels import DataModel
from datamodels import exceptions


class Request(DataModel):
    data: dict
    producer: int
    consumer: int


try:
    Request(
        data={},
        producer=1,
        consumer=2,
    )
except Exception as e:
    exit(e)

else:
    print("--- Base case works clear")

##########################################

try:
    Request(
        data={}, producer=1, consumer=None, allow_none=False
    )
except exceptions.InvalidType:
    print("--- 'Allow None' option works clear")

##########################################

try:
    Request(
        data={}, producer=1, consumer="2"
    )
except exceptions.InvalidType:
    print("--- 'Static types' option works clear")

##########################################

try:
    Request(
        data={}, producer=1, consumer="2", statictypes=False
    )
except Exception as e:
    print(e)

else:
    print("--- 'Dynamic types' option works clear")
