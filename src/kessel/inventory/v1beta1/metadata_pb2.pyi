from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from kessel.inventory.v1beta1 import resource_tag_pb2 as _resource_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.resource_tag_pb2 import ResourceTag as ResourceTag

DESCRIPTOR: _descriptor.FileDescriptor

class Metadata(_message.Message):
    __slots__ = ("id", "resource_type", "first_reported", "last_reported", "first_reported_by", "last_reported_by", "workspace", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_REPORTED_FIELD_NUMBER: _ClassVar[int]
    LAST_REPORTED_FIELD_NUMBER: _ClassVar[int]
    FIRST_REPORTED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_REPORTED_BY_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    resource_type: str
    first_reported: _timestamp_pb2.Timestamp
    last_reported: _timestamp_pb2.Timestamp
    first_reported_by: str
    last_reported_by: str
    workspace: str
    tags: _containers.RepeatedCompositeFieldContainer[_resource_tag_pb2.ResourceTag]
    def __init__(self, id: _Optional[int] = ..., resource_type: _Optional[str] = ..., first_reported: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_reported: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_reported_by: _Optional[str] = ..., last_reported_by: _Optional[str] = ..., workspace: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[_resource_tag_pb2.ResourceTag, _Mapping]]] = ...) -> None: ...
