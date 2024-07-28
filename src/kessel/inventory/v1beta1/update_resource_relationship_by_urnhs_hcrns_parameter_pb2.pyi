from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateResourceRelationshipByURNHsHcrnsParameter(_message.Message):
    __slots__ = ("subjectURN", "objectURN")
    SUBJECTURN_FIELD_NUMBER: _ClassVar[int]
    OBJECTURN_FIELD_NUMBER: _ClassVar[int]
    subjectURN: str
    objectURN: str
    def __init__(self, subjectURN: _Optional[str] = ..., objectURN: _Optional[str] = ...) -> None: ...
