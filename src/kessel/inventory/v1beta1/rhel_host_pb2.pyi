from google.api import field_behavior_pb2 as _field_behavior_pb2
from validate import validate_pb2 as _validate_pb2
from kessel.inventory.v1beta1 import metadata_pb2 as _metadata_pb2
from kessel.inventory.v1beta1 import resource_tag_pb2 as _resource_tag_pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as _reporter_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.metadata_pb2 import Metadata as Metadata
from kessel.inventory.v1beta1.reporter_data_pb2 import ReporterData as ReporterData

DESCRIPTOR: _descriptor.FileDescriptor

class RHELHost(_message.Message):
    __slots__ = ("metadata", "reporter_data", "reporters")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REPORTER_DATA_FIELD_NUMBER: _ClassVar[int]
    REPORTERS_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.Metadata
    reporter_data: _reporter_data_pb2.ReporterData
    reporters: _containers.RepeatedCompositeFieldContainer[_reporter_data_pb2.ReporterData]
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ..., reporter_data: _Optional[_Union[_reporter_data_pb2.ReporterData, _Mapping]] = ..., reporters: _Optional[_Iterable[_Union[_reporter_data_pb2.ReporterData, _Mapping]]] = ...) -> None: ...
