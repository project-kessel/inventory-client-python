from google.api import annotations_pb2 as _annotations_pb2
from kessel.inventory.v1beta1 import k8s_cluster_pb2 as _k8s_cluster_pb2
from kessel.inventory.v1beta1 import k8s_cluster_detail_pb2 as _k8s_cluster_detail_pb2
from kessel.inventory.v1beta1 import metadata_pb2 as _metadata_pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as _reporter_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.k8s_cluster_pb2 import K8sCluster as K8sCluster

DESCRIPTOR: _descriptor.FileDescriptor

class CreateK8sClusterRequest(_message.Message):
    __slots__ = ("k8sCluster",)
    K8SCLUSTER_FIELD_NUMBER: _ClassVar[int]
    k8sCluster: _k8s_cluster_pb2.K8sCluster
    def __init__(self, k8sCluster: _Optional[_Union[_k8s_cluster_pb2.K8sCluster, _Mapping]] = ...) -> None: ...

class CreateK8sClusterResponse(_message.Message):
    __slots__ = ("k8sCluster",)
    K8SCLUSTER_FIELD_NUMBER: _ClassVar[int]
    k8sCluster: _k8s_cluster_pb2.K8sCluster
    def __init__(self, k8sCluster: _Optional[_Union[_k8s_cluster_pb2.K8sCluster, _Mapping]] = ...) -> None: ...

class UpdateK8sClusterRequest(_message.Message):
    __slots__ = ("resource", "k8sCluster")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    K8SCLUSTER_FIELD_NUMBER: _ClassVar[int]
    resource: str
    k8sCluster: _k8s_cluster_pb2.K8sCluster
    def __init__(self, resource: _Optional[str] = ..., k8sCluster: _Optional[_Union[_k8s_cluster_pb2.K8sCluster, _Mapping]] = ...) -> None: ...

class UpdateK8sClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteK8sClusterRequest(_message.Message):
    __slots__ = ("resource",)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    def __init__(self, resource: _Optional[str] = ...) -> None: ...

class DeleteK8sClusterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
