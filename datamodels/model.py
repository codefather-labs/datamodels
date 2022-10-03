from datamodels import exceptions


class DataModel:

    def __init__(self,
                 statictypes: bool = True,
                 allow_none: bool = True,
                 readonly: bool = False,
                 *args, **kwargs):
        self.__data = {}
        self.__statictypes: bool = statictypes
        self.__allow_none: bool = allow_none
        self.__readonly = readonly

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

            self.update_value(k, v)

    def __setitem__(self, key, value):
        if self.readonly:
            raise exceptions.ReadOnlyAccessError(self)

        if self.statictypes:
            if not self.__data.get(key):
                raise exceptions.InvalidType(
                    f"{key} can't assign undeclared "
                    f"attributes after initialization"
                )

            if not isinstance(value, type(self.__data.get(key))):
                raise exceptions.InvalidType(
                    f"Can't assign undeclared type of "
                    f"attribute '{key}'"
                )

        self.__dict__[key] = value

    @property
    def readonly(self) -> bool:
        return self.__readonly

    @property
    def statictypes(self) -> bool:
        return self.__statictypes

    def allow_none(self) -> bool:
        return self.__allow_none

    def update_value(self, k, v):
        self.__setattr__(k, v)
        self.__data.update({k: v})

    def update(self, data: dict):
        if not data:
            return

        if self.readonly:
            raise exceptions.ReadOnlyAccessError(self)

        for key, value in data.items():
            if self.statictypes:
                if not self.__data.get(key):
                    raise exceptions.InvalidType(
                        f"{key} can't assign undeclared "
                        f"attributes after initialization"
                    )

                if not isinstance(value, type(self.__data.get(key))):
                    raise exceptions.InvalidType(
                        f"Can't assign undeclared type of "
                        f"attribute '{key}'"
                    )

            self.update_value(k=key, v=value)

    @property
    def as_dict(self) -> dict:
        return self.__data

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        string = ", ".join([f'{k}: {type(v).__name__}={v}'
                            for k, v in self.as_dict.items()])
        if self.readonly:
            string += ' readonly'

        return f"<{self.__class__.__name__} {string}>"
