from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from kessel.inventory.v1beta1 import notifications_integration_pb2 as _notifications_integration_pb2
from kessel.inventory.v1beta1 import metadata_pb2 as _metadata_pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as _reporter_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.notifications_integration_pb2 import NotificationsIntegration as NotificationsIntegration

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNotificationsIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: _notifications_integration_pb2.NotificationsIntegration
    def __init__(self, integration: _Optional[_Union[_notifications_integration_pb2.NotificationsIntegration, _Mapping]] = ...) -> None: ...

class CreateNotificationsIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: _notifications_integration_pb2.NotificationsIntegration
    def __init__(self, integration: _Optional[_Union[_notifications_integration_pb2.NotificationsIntegration, _Mapping]] = ...) -> None: ...

class UpdateNotificationsIntegrationRequest(_message.Message):
    __slots__ = ("resource", "integration")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    resource: str
    integration: _notifications_integration_pb2.NotificationsIntegration
    def __init__(self, resource: _Optional[str] = ..., integration: _Optional[_Union[_notifications_integration_pb2.NotificationsIntegration, _Mapping]] = ...) -> None: ...

class UpdateNotificationsIntegrationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteNotificationsIntegrationRequest(_message.Message):
    __slots__ = ("resource",)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    def __init__(self, resource: _Optional[str] = ...) -> None: ...

class DeleteNotificationsIntegrationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
