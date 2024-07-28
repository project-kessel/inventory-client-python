from kessel.inventory.v1beta1 import common_attributes_reporters_inner_pb2 as _common_attributes_reporters_inner_pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as _reporter_data_pb2
from kessel.inventory.v1beta1 import resource_tag_pb2 as _resource_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.common_attributes_reporters_inner_pb2 import CommonAttributesReportersInner as CommonAttributesReportersInner
from kessel.inventory.v1beta1.reporter_data_pb2 import ReporterData as ReporterData
from kessel.inventory.v1beta1.resource_tag_pb2 import ResourceTag as ResourceTag

DESCRIPTOR: _descriptor.FileDescriptor

class RHELHost(_message.Message):
    __slots__ = ("id", "resource_type", "first_reported", "first_reported_by", "latest_reported", "latest_reported_by", "workspace", "reporter_data", "reporters", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_REPORTED_FIELD_NUMBER: _ClassVar[int]
    FIRST_REPORTED_BY_FIELD_NUMBER: _ClassVar[int]
    LATEST_REPORTED_FIELD_NUMBER: _ClassVar[int]
    LATEST_REPORTED_BY_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    REPORTER_DATA_FIELD_NUMBER: _ClassVar[int]
    REPORTERS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource_type: str
    first_reported: str
    first_reported_by: str
    latest_reported: str
    latest_reported_by: str
    workspace: str
    reporter_data: _reporter_data_pb2.ReporterData
    reporters: _containers.RepeatedCompositeFieldContainer[_common_attributes_reporters_inner_pb2.CommonAttributesReportersInner]
    tags: _containers.RepeatedCompositeFieldContainer[_resource_tag_pb2.ResourceTag]
    def __init__(self, id: _Optional[str] = ..., resource_type: _Optional[str] = ..., first_reported: _Optional[str] = ..., first_reported_by: _Optional[str] = ..., latest_reported: _Optional[str] = ..., latest_reported_by: _Optional[str] = ..., workspace: _Optional[str] = ..., reporter_data: _Optional[_Union[_reporter_data_pb2.ReporterData, _Mapping]] = ..., reporters: _Optional[_Iterable[_Union[_common_attributes_reporters_inner_pb2.CommonAttributesReportersInner, _Mapping]]] = ..., tags: _Optional[_Iterable[_Union[_resource_tag_pb2.ResourceTag, _Mapping]]] = ...) -> None: ...
