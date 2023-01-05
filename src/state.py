from abc import abstractmethod, ABC

from tokens import MessageBodyToken, ReplyToToken, Token, FromToken, MessageIdToken


class ParseState(ABC):
    @abstractmethod
    def consume_line(self, line: str):
        pass

    @abstractmethod
    def is_my_state(self, line: str) -> bool:
        pass

    @abstractmethod
    def dump(self) -> Token:
        pass


class MessageIdParseState(ParseState):
    def __init__(self):
        self.val: str = ''

    def consume_line(self, line: str):
        self.val = MessageIdToken.line_match.match(line).group(1)

    def is_my_state(self, line: str) -> bool:
        return MessageIdToken.line_match.match(line) is not None

    def dump(self) -> Token:
        ret = MessageIdToken(val=self.val)
        self.val = ''

        return ret


class FromParseState(ParseState):
    def __init__(self):
        self.val: str = ''

    def consume_line(self, line: str):
        self.val = FromToken.line_match.match(line).group(1)

    def is_my_state(self, line: str) -> bool:
        return FromToken.line_match.match(line) is not None

    def dump(self) -> Token:
        ret = FromToken(val=self.val)
        self.val = ''

        return ret


class ReplyToParseState(ParseState):
    def __init__(self):
        self.val: str = ''

    def consume_line(self, line: str):
        self.val = ReplyToToken.line_match.match(line).group(1)

    def is_my_state(self, line: str) -> bool:
        return ReplyToToken.line_match.match(line) is not None

    def dump(self) -> Token:
        ret = ReplyToToken(val=int(self.val))
        self.val = ''

        return ret


class MessageBodyParseState(ParseState):
    def __init__(self):
        self.val: str = ''

    def consume_line(self, line: str):
        self.val += f'{line}\n'

    def is_my_state(self, line: str) -> bool:
        return True

    def dump(self) -> Token:
        ret = MessageBodyToken(val=self.val.strip())
        self.val = ''

        return ret
