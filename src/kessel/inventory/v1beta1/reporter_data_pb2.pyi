from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReporterData(_message.Message):
    __slots__ = ("reporter_type", "reporter_instance_id", "console_href", "api_href", "resourceid_alias", "reporter_version")
    class Reporter_typeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Reporter_typeEnum_ACM: _ClassVar[ReporterData.Reporter_typeEnum]
        Reporter_typeEnum_HBI: _ClassVar[ReporterData.Reporter_typeEnum]
        Reporter_typeEnum_OCM: _ClassVar[ReporterData.Reporter_typeEnum]
        Reporter_typeEnum_OTHER: _ClassVar[ReporterData.Reporter_typeEnum]
        Reporter_typeEnum_UNKNOWN: _ClassVar[ReporterData.Reporter_typeEnum]
    Reporter_typeEnum_ACM: ReporterData.Reporter_typeEnum
    Reporter_typeEnum_HBI: ReporterData.Reporter_typeEnum
    Reporter_typeEnum_OCM: ReporterData.Reporter_typeEnum
    Reporter_typeEnum_OTHER: ReporterData.Reporter_typeEnum
    Reporter_typeEnum_UNKNOWN: ReporterData.Reporter_typeEnum
    REPORTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPORTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_HREF_FIELD_NUMBER: _ClassVar[int]
    API_HREF_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_ALIAS_FIELD_NUMBER: _ClassVar[int]
    REPORTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    reporter_type: ReporterData.Reporter_typeEnum
    reporter_instance_id: str
    console_href: str
    api_href: str
    resourceid_alias: str
    reporter_version: str
    def __init__(self, reporter_type: _Optional[_Union[ReporterData.Reporter_typeEnum, str]] = ..., reporter_instance_id: _Optional[str] = ..., console_href: _Optional[str] = ..., api_href: _Optional[str] = ..., resourceid_alias: _Optional[str] = ..., reporter_version: _Optional[str] = ...) -> None: ...
