# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta1/resources/k8s_cluster.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'kessel/inventory/v1beta1/resources/k8s_cluster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from kessel.inventory.v1beta1.resources import k8s_cluster_detail_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_k8s__cluster__detail__pb2
from kessel.inventory.v1beta1.resources import metadata_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_metadata__pb2
from kessel.inventory.v1beta1.resources import reporter_data_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_reporter__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4kessel/inventory/v1beta1/resources/k8s_cluster.proto\x12\"kessel.inventory.v1beta1.resources\x1a\x1b\x62uf/validate/validate.proto\x1a;kessel/inventory/v1beta1/resources/k8s_cluster_detail.proto\x1a\x31kessel/inventory/v1beta1/resources/metadata.proto\x1a\x36kessel/inventory/v1beta1/resources/reporter_data.proto\"\xa0\x02\n\nK8sCluster\x12H\n\x08metadata\x18\x01 \x01(\x0b\x32,.kessel.inventory.v1beta1.resources.MetadataR\x08metadata\x12\x61\n\rreporter_data\x18\xc8\xd0\xfat \x01(\x0b\x32\x30.kessel.inventory.v1beta1.resources.ReporterDataB\x06\xbaH\x03\xc8\x01\x01R\rreporter_data\x12\x65\n\rresource_data\x18\xca\xc7\x81\x01 \x01(\x0b\x32\x34.kessel.inventory.v1beta1.resources.K8sClusterDetailB\x06\xbaH\x03\xc8\x01\x01R\rresource_dataB\x97\x01\n2org.project_kessel.api.inventory.v1beta1.resourcesB\x0fK8sClusterProtoP\x01ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resourcesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.resources.k8s_cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n2org.project_kessel.api.inventory.v1beta1.resourcesB\017K8sClusterProtoP\001ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resources'
  _globals['_K8SCLUSTER'].fields_by_name['reporter_data']._loaded_options = None
  _globals['_K8SCLUSTER'].fields_by_name['reporter_data']._serialized_options = b'\272H\003\310\001\001'
  _globals['_K8SCLUSTER'].fields_by_name['resource_data']._loaded_options = None
  _globals['_K8SCLUSTER'].fields_by_name['resource_data']._serialized_options = b'\272H\003\310\001\001'
  _globals['_K8SCLUSTER']._serialized_start=290
  _globals['_K8SCLUSTER']._serialized_end=578
# @@protoc_insertion_point(module_scope)
