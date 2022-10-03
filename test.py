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

try:
    request = Request(
        data={},
        producer=1,
        consumer=2,
        readonly=True
    )
    request.update(data={
        "produced": 3
    })
except exceptions.ReadOnlyAccessError:
    print("--- 'Readonly' option works clear")

request = Request(
    data={},
    producer=1,
    consumer=2,
)
assert request.update(data={}) is None

try:
    request.update({
        "producer": "3"
    })
except exceptions.InvalidType:
    print("--- Invalid types check works clear")

request.update({
    "producer": 3
})

assert request.data == {}
assert request.consumer == 2
assert request.producer == 3
