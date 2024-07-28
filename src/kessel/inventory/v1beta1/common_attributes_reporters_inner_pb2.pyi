from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommonAttributesReportersInner(_message.Message):
    __slots__ = ("Type", "reporter_instance_id", "created", "last_updated")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REPORTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    Type: str
    reporter_instance_id: str
    created: str
    last_updated: str
    def __init__(self, Type: _Optional[str] = ..., reporter_instance_id: _Optional[str] = ..., created: _Optional[str] = ..., last_updated: _Optional[str] = ...) -> None: ...
