from kessel.inventory.v1beta1 import k8s_cluster_detail_nodes_inner_pb2 as _k8s_cluster_detail_nodes_inner_pb2
from kessel.inventory.v1beta1 import resource_tag_pb2 as _resource_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from kessel.inventory.v1beta1.k8s_cluster_detail_nodes_inner_pb2 import K8sClusterDetailNodesInner as K8sClusterDetailNodesInner

DESCRIPTOR: _descriptor.FileDescriptor

class K8sClusterDetail(_message.Message):
    __slots__ = ("external_cluster_id", "cluster_status", "kube_version", "kube_vendor", "vendor_version", "cloud_platform", "Nodes")
    class Cluster_statusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Cluster_statusEnum_READY: _ClassVar[K8sClusterDetail.Cluster_statusEnum]
        Cluster_statusEnum_FAILED: _ClassVar[K8sClusterDetail.Cluster_statusEnum]
        Cluster_statusEnum_OFFLINE: _ClassVar[K8sClusterDetail.Cluster_statusEnum]
        Cluster_statusEnum_UNKNOWN: _ClassVar[K8sClusterDetail.Cluster_statusEnum]
    Cluster_statusEnum_READY: K8sClusterDetail.Cluster_statusEnum
    Cluster_statusEnum_FAILED: K8sClusterDetail.Cluster_statusEnum
    Cluster_statusEnum_OFFLINE: K8sClusterDetail.Cluster_statusEnum
    Cluster_statusEnum_UNKNOWN: K8sClusterDetail.Cluster_statusEnum
    class Kube_vendorEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Kube_vendorEnum_AKS: _ClassVar[K8sClusterDetail.Kube_vendorEnum]
        Kube_vendorEnum_EKS: _ClassVar[K8sClusterDetail.Kube_vendorEnum]
        Kube_vendorEnum_IKS: _ClassVar[K8sClusterDetail.Kube_vendorEnum]
        Kube_vendorEnum_OPENSHIFT: _ClassVar[K8sClusterDetail.Kube_vendorEnum]
        Kube_vendorEnum_GKE: _ClassVar[K8sClusterDetail.Kube_vendorEnum]
        Kube_vendorEnum_OTHER: _ClassVar[K8sClusterDetail.Kube_vendorEnum]
        Kube_vendorEnum_UNKNOWN: _ClassVar[K8sClusterDetail.Kube_vendorEnum]
    Kube_vendorEnum_AKS: K8sClusterDetail.Kube_vendorEnum
    Kube_vendorEnum_EKS: K8sClusterDetail.Kube_vendorEnum
    Kube_vendorEnum_IKS: K8sClusterDetail.Kube_vendorEnum
    Kube_vendorEnum_OPENSHIFT: K8sClusterDetail.Kube_vendorEnum
    Kube_vendorEnum_GKE: K8sClusterDetail.Kube_vendorEnum
    Kube_vendorEnum_OTHER: K8sClusterDetail.Kube_vendorEnum
    Kube_vendorEnum_UNKNOWN: K8sClusterDetail.Kube_vendorEnum
    class Cloud_platformEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Cloud_platformEnum_BAREMETAL_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_BAREMETAL_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_AWS_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_AWS_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_AZURE_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_AZURE_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_IBMCLOUD_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_IBMCLOUD_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_KUBEVIRT_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_OPENSTACK_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_OPENSTACK_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_GCP_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_GCP_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_NUTANIX_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_NUTANIX_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_VSPHERE_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_VSPHERE_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_OVIRT_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_UNKNOWN_IPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
        Cloud_platformEnum_NONE_UPI_: _ClassVar[K8sClusterDetail.Cloud_platformEnum]
    Cloud_platformEnum_BAREMETAL_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_BAREMETAL_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_AWS_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_AWS_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_AZURE_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_AZURE_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_IBMCLOUD_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_IBMCLOUD_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_KUBEVIRT_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_OPENSTACK_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_OPENSTACK_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_GCP_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_GCP_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_NUTANIX_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_NUTANIX_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_VSPHERE_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_VSPHERE_UPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_OVIRT_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_UNKNOWN_IPI_: K8sClusterDetail.Cloud_platformEnum
    Cloud_platformEnum_NONE_UPI_: K8sClusterDetail.Cloud_platformEnum
    EXTERNAL_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    KUBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    KUBE_VENDOR_FIELD_NUMBER: _ClassVar[int]
    VENDOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    external_cluster_id: str
    cluster_status: K8sClusterDetail.Cluster_statusEnum
    kube_version: str
    kube_vendor: K8sClusterDetail.Kube_vendorEnum
    vendor_version: str
    cloud_platform: K8sClusterDetail.Cloud_platformEnum
    Nodes: _containers.RepeatedCompositeFieldContainer[_k8s_cluster_detail_nodes_inner_pb2.K8sClusterDetailNodesInner]
    def __init__(self, external_cluster_id: _Optional[str] = ..., cluster_status: _Optional[_Union[K8sClusterDetail.Cluster_statusEnum, str]] = ..., kube_version: _Optional[str] = ..., kube_vendor: _Optional[_Union[K8sClusterDetail.Kube_vendorEnum, str]] = ..., vendor_version: _Optional[str] = ..., cloud_platform: _Optional[_Union[K8sClusterDetail.Cloud_platformEnum, str]] = ..., Nodes: _Optional[_Iterable[_Union[_k8s_cluster_detail_nodes_inner_pb2.K8sClusterDetailNodesInner, _Mapping]]] = ...) -> None: ...
