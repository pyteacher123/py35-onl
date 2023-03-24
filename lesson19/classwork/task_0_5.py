from typing import Callable, Any


class Validator:
    def __call__(self, value: str) -> None:
        raise NotImplementedError


def validator2(value: str) -> None:
    raise NotImplementedError


def validator3(value: int) -> str:
    raise NotImplementedError


def some_business_logic1(validator: Callable[[str], None]) -> None:
    validator("Hello")


def some_business_logic(validator: Callable[..., Any]) -> None:
    validator("Hello")


some_business_logic(Validator())
some_business_logic(validator2)
some_business_logic(validator3)
