from google.api import annotations_pb2 as _annotations_pb2
from kessel.inventory.v1beta1 import rhel_host_pb2 as _rhel_host_pb2
from kessel.inventory.v1beta1 import metadata_pb2 as _metadata_pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as _reporter_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.rhel_host_pb2 import RHELHost as RHELHost

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRHELHostRequest(_message.Message):
    __slots__ = ("host",)
    HOST_FIELD_NUMBER: _ClassVar[int]
    host: _rhel_host_pb2.RHELHost
    def __init__(self, host: _Optional[_Union[_rhel_host_pb2.RHELHost, _Mapping]] = ...) -> None: ...

class CreateRHELHostResponse(_message.Message):
    __slots__ = ("host",)
    HOST_FIELD_NUMBER: _ClassVar[int]
    host: _rhel_host_pb2.RHELHost
    def __init__(self, host: _Optional[_Union[_rhel_host_pb2.RHELHost, _Mapping]] = ...) -> None: ...

class UpdateRHELHostRequest(_message.Message):
    __slots__ = ("resource", "host")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    resource: str
    host: _rhel_host_pb2.RHELHost
    def __init__(self, resource: _Optional[str] = ..., host: _Optional[_Union[_rhel_host_pb2.RHELHost, _Mapping]] = ...) -> None: ...

class UpdateRHELHostResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRHELHostRequest(_message.Message):
    __slots__ = ("resource",)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    def __init__(self, resource: _Optional[str] = ...) -> None: ...

class DeleteRHELHostResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
