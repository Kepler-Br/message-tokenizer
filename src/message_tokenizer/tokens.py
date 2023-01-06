import re
from abc import ABC, abstractmethod


class Token(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass


class MessageIdToken(Token):
    line_match = re.compile(r'^---- (\d+)$')
    keyword = '----'

    def __init__(self, val: str):
        self.val = val

    def serialize(self) -> str:
        return f'{self.keyword}{self.val}'


class FromToken(Token):
    line_match = re.compile(r'^-- (.*)$')
    keyword = '--'

    def __init__(self, val: str):
        self.val = val

    def serialize(self) -> str:
        return f'{self.keyword}{self.val}'


class ReplyToToken(Token):
    line_match = re.compile(r'^>> (\d+)$')
    keyword = '>>'

    def __init__(self, val: int):
        self.val = val

    def serialize(self) -> str:
        return f'{self.keyword}{self.val}'


class MessageBodyToken(Token):
    def __init__(self, val: str):
        self.val = val

    def serialize(self) -> str:
        return self.val
