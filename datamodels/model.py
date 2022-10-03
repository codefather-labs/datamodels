from datamodels import exceptions


class DataModel:

    def __init__(self,
                 statictypes: bool = True,
                 allow_none: bool = True,
                 *args, **kwargs):
        if args:
            raise exceptions.PositionalArgumentsError(
                "Datamodels not support positional args now."
                "Please use named args only."
            )

        argspec = self.__class__.__dict__.get('__annotations__')
        for k, v in kwargs.items():
            if k not in argspec:
                raise exceptions.UnknownModelAttribute(k)

            if statictypes and not isinstance(v, argspec[k]):
                if v is None and allow_none:
                    ...

                else:
                    raise exceptions.InvalidType(f"{k} expected {argspec[k]} got {type(v)}")

            setattr(self, k, v)
