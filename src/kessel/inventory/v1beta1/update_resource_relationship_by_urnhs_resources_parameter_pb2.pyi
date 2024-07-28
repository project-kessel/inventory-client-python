from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateResourceRelationshipByURNHsResourcesParameter(_message.Message):
    __slots__ = ("subject_resource", "object_resource")
    SUBJECT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    subject_resource: str
    object_resource: str
    def __init__(self, subject_resource: _Optional[str] = ..., object_resource: _Optional[str] = ...) -> None: ...
