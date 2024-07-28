from google.api import annotations_pb2 as _annotations_pb2
from kessel.inventory.v1beta1 import error_pb2 as _error_pb2
from kessel.inventory.v1beta1 import policy_pb2 as _policy_pb2
from kessel.inventory.v1beta1 import common_attributes_reporters_inner_pb2 as _common_attributes_reporters_inner_pb2
from kessel.inventory.v1beta1 import policy_detail_pb2 as _policy_detail_pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as _reporter_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.error_pb2 import Error as Error
from kessel.inventory.v1beta1.policy_pb2 import Policy as Policy

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePolicyRequest(_message.Message):
    __slots__ = ("policy",)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: _policy_pb2.Policy
    def __init__(self, policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class CreatePolicyResponse(_message.Message):
    __slots__ = ("policy",)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: _policy_pb2.Policy
    def __init__(self, policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ("resource", "policy")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    resource: str
    policy: _policy_pb2.Policy
    def __init__(self, resource: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class UpdatePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ("resource",)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    def __init__(self, resource: _Optional[str] = ...) -> None: ...

class DeletePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
