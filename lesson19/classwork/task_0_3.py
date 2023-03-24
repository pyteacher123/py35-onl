from typing import TypeAlias


SelfExammple: TypeAlias = 'Example'


class Example:
    def __iter__(self) -> SelfExammple:
        return self

    def test1(self) -> SelfExammple:
        return self

    def test2(self) -> SelfExammple:
        return self
