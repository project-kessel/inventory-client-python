from kessel.inventory.v1beta1 import resource_tag_pb2 as _resource_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.resource_tag_pb2 import ResourceTag as ResourceTag

DESCRIPTOR: _descriptor.FileDescriptor

class K8sClusterDetailNodesInner(_message.Message):
    __slots__ = ("name", "cpu", "memory", "labels")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    cpu: str
    memory: str
    labels: _containers.RepeatedCompositeFieldContainer[_resource_tag_pb2.ResourceTag]
    def __init__(self, name: _Optional[str] = ..., cpu: _Optional[str] = ..., memory: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_resource_tag_pb2.ResourceTag, _Mapping]]] = ...) -> None: ...
