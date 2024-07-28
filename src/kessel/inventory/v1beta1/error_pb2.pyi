from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("type", "title", "status", "detail", "instance")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    type: str
    title: str
    status: int
    detail: str
    instance: str
    def __init__(self, type: _Optional[str] = ..., title: _Optional[str] = ..., status: _Optional[int] = ..., detail: _Optional[str] = ..., instance: _Optional[str] = ...) -> None: ...
