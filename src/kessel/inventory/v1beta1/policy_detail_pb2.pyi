from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicyDetail(_message.Message):
    __slots__ = ("disabled", "severity")
    class SeverityEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SeverityEnum_LOW: _ClassVar[PolicyDetail.SeverityEnum]
        SeverityEnum_MEDIUM: _ClassVar[PolicyDetail.SeverityEnum]
        SeverityEnum_HIGH: _ClassVar[PolicyDetail.SeverityEnum]
        SeverityEnum_CRITICAL: _ClassVar[PolicyDetail.SeverityEnum]
        SeverityEnum_OTHER: _ClassVar[PolicyDetail.SeverityEnum]
    SeverityEnum_LOW: PolicyDetail.SeverityEnum
    SeverityEnum_MEDIUM: PolicyDetail.SeverityEnum
    SeverityEnum_HIGH: PolicyDetail.SeverityEnum
    SeverityEnum_CRITICAL: PolicyDetail.SeverityEnum
    SeverityEnum_OTHER: PolicyDetail.SeverityEnum
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    severity: PolicyDetail.SeverityEnum
    def __init__(self, disabled: bool = ..., severity: _Optional[_Union[PolicyDetail.SeverityEnum, str]] = ...) -> None: ...
