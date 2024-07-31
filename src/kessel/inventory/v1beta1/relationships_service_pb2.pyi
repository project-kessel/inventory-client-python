from google.api import annotations_pb2 as _annotations_pb2
from kessel.inventory.v1beta1 import policy_relationship_pb2 as _policy_relationship_pb2
from kessel.inventory.v1beta1 import update_resource_relationship_by_urnhs_resources_parameter_pb2 as _update_resource_relationship_by_urnhs_resources_parameter_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.policy_relationship_pb2 import PolicyRelationship as PolicyRelationship
from kessel.inventory.v1beta1.update_resource_relationship_by_urnhs_resources_parameter_pb2 import UpdateResourceRelationshipByURNHsResourcesParameter as UpdateResourceRelationshipByURNHsResourcesParameter

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePolicyRelationshipRequest(_message.Message):
    __slots__ = ("policyRelationship",)
    POLICYRELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    policyRelationship: _policy_relationship_pb2.PolicyRelationship
    def __init__(self, policyRelationship: _Optional[_Union[_policy_relationship_pb2.PolicyRelationship, _Mapping]] = ...) -> None: ...

class CreatePolicyRelationshipResponse(_message.Message):
    __slots__ = ("policyRelationship",)
    POLICYRELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    policyRelationship: _policy_relationship_pb2.PolicyRelationship
    def __init__(self, policyRelationship: _Optional[_Union[_policy_relationship_pb2.PolicyRelationship, _Mapping]] = ...) -> None: ...

class UpdateResourceRelationshipByURNHsRequest(_message.Message):
    __slots__ = ("resources", "policyRelationship")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    POLICYRELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    resources: _update_resource_relationship_by_urnhs_resources_parameter_pb2.UpdateResourceRelationshipByURNHsResourcesParameter
    policyRelationship: _policy_relationship_pb2.PolicyRelationship
    def __init__(self, resources: _Optional[_Union[_update_resource_relationship_by_urnhs_resources_parameter_pb2.UpdateResourceRelationshipByURNHsResourcesParameter, _Mapping]] = ..., policyRelationship: _Optional[_Union[_policy_relationship_pb2.PolicyRelationship, _Mapping]] = ...) -> None: ...

class UpdateResourceRelationshipByURNResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteResourceRelationshipByURNRequest(_message.Message):
    __slots__ = ("resources",)
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    resources: _update_resource_relationship_by_urnhs_resources_parameter_pb2.UpdateResourceRelationshipByURNHsResourcesParameter
    def __init__(self, resources: _Optional[_Union[_update_resource_relationship_by_urnhs_resources_parameter_pb2.UpdateResourceRelationshipByURNHsResourcesParameter, _Mapping]] = ...) -> None: ...

class DeleteResourceRelationshipByURNResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
