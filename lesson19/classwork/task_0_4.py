from typing import ClassVar


class Validator1:
    def __call__(self) -> None:
        raise NotImplementedError


def do_something(validator_class: type[Validator1]) -> None:
    raise NotImplementedError


do_something(Validator1)


################################################################


class Example:
    available_extensions: ClassVar[tuple[str, ...]] = ("some.csv",)


ex1 = Example()
print(ex1.available_extensions)
