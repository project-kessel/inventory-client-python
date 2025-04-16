from google.api import annotations_pb2 as _annotations_pb2
from kessel.inventory.v1beta2 import common_pb2 as _common_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckRequest(_message.Message):
    __slots__ = ("parent", "relation", "subject")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    parent: _common_pb2.ObjectReference
    relation: str
    subject: _common_pb2.SubjectReference
    def __init__(self, parent: _Optional[_Union[_common_pb2.ObjectReference, _Mapping]] = ..., relation: _Optional[str] = ..., subject: _Optional[_Union[_common_pb2.SubjectReference, _Mapping]] = ...) -> None: ...

class CheckResponse(_message.Message):
    __slots__ = ("allowed",)
    class Allowed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALLOWED_UNSPECIFIED: _ClassVar[CheckResponse.Allowed]
        ALLOWED_TRUE: _ClassVar[CheckResponse.Allowed]
        ALLOWED_FALSE: _ClassVar[CheckResponse.Allowed]
    ALLOWED_UNSPECIFIED: CheckResponse.Allowed
    ALLOWED_TRUE: CheckResponse.Allowed
    ALLOWED_FALSE: CheckResponse.Allowed
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    allowed: CheckResponse.Allowed
    def __init__(self, allowed: _Optional[_Union[CheckResponse.Allowed, str]] = ...) -> None: ...

class CheckForUpdateRequest(_message.Message):
    __slots__ = ("parent", "relation", "subject")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    parent: _common_pb2.ObjectReference
    relation: str
    subject: _common_pb2.SubjectReference
    def __init__(self, parent: _Optional[_Union[_common_pb2.ObjectReference, _Mapping]] = ..., relation: _Optional[str] = ..., subject: _Optional[_Union[_common_pb2.SubjectReference, _Mapping]] = ...) -> None: ...

class CheckForUpdateResponse(_message.Message):
    __slots__ = ("allowed",)
    class Allowed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALLOWED_UNSPECIFIED: _ClassVar[CheckForUpdateResponse.Allowed]
        ALLOWED_TRUE: _ClassVar[CheckForUpdateResponse.Allowed]
        ALLOWED_FALSE: _ClassVar[CheckForUpdateResponse.Allowed]
    ALLOWED_UNSPECIFIED: CheckForUpdateResponse.Allowed
    ALLOWED_TRUE: CheckForUpdateResponse.Allowed
    ALLOWED_FALSE: CheckForUpdateResponse.Allowed
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    allowed: CheckForUpdateResponse.Allowed
    def __init__(self, allowed: _Optional[_Union[CheckForUpdateResponse.Allowed, str]] = ...) -> None: ...
