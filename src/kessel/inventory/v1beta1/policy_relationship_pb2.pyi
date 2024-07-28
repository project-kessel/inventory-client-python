from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicyRelationship(_message.Message):
    __slots__ = ("relationship_type", "policy_id", "cluster_id", "status")
    class StatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        StatusEnum_COMPLIANT: _ClassVar[PolicyRelationship.StatusEnum]
        StatusEnum_NON_COMPLIANT: _ClassVar[PolicyRelationship.StatusEnum]
        StatusEnum_OTHER: _ClassVar[PolicyRelationship.StatusEnum]
        StatusEnum_UNKNOWN: _ClassVar[PolicyRelationship.StatusEnum]
    StatusEnum_COMPLIANT: PolicyRelationship.StatusEnum
    StatusEnum_NON_COMPLIANT: PolicyRelationship.StatusEnum
    StatusEnum_OTHER: PolicyRelationship.StatusEnum
    StatusEnum_UNKNOWN: PolicyRelationship.StatusEnum
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    relationship_type: str
    policy_id: str
    cluster_id: str
    status: PolicyRelationship.StatusEnum
    def __init__(self, relationship_type: _Optional[str] = ..., policy_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., status: _Optional[_Union[PolicyRelationship.StatusEnum, str]] = ...) -> None: ...
