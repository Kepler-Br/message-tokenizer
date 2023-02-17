# Message tokenizer

Serialized message format:
```
----- MESSAGE_ID
--- FROM_USER_NAME
>> REPLY_TO_MESSAGE_ID
MESSAGE BODY
```

Serialized example:
```
---- 10020147
-- Horizon
>> 10020146
Причём тут Тодд
```

## How to use

Serialization
```python
from message_tokenizer.tokenizer import data_to_tokenized_text

data_to_tokenized_text(message_id=10020147,
                       text="Причём тут Тодд",
                       username="Horizon",
                       reply_to_message=10020146)
```

Deserialization
```python
from message_tokenizer.tokenizer import TextToTokenSeqParser

tokenizer = TextToTokenSeqParser()

tokenized_message = """
---- 10020147
-- Horizon
>> 10020146
Причём тут Тодд
""".strip()

parsed = tokenizer.parse(tokenized_message)
```
