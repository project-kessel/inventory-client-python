from kessel.inventory.v1beta1 import resource_tag_pb2 as _resource_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.resource_tag_pb2 import ResourceTag as ResourceTag

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceTags(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[_resource_tag_pb2.ResourceTag]
    def __init__(self, tags: _Optional[_Iterable[_Union[_resource_tag_pb2.ResourceTag, _Mapping]]] = ...) -> None: ...
