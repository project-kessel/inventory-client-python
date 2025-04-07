# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta1/resources/k8s_policies_service.proto
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
    'kessel/inventory/v1beta1/resources/k8s_policies_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from kessel.inventory.v1beta1.resources import k8s_policy_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_k8s__policy__pb2
from kessel.inventory.v1beta1.resources import reporter_data_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_reporter__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=kessel/inventory/v1beta1/resources/k8s_policies_service.proto\x12\"kessel.inventory.v1beta1.resources\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x62uf/validate/validate.proto\x1a\x33kessel/inventory/v1beta1/resources/k8s_policy.proto\x1a\x36kessel/inventory/v1beta1/resources/reporter_data.proto\"o\n\x16\x43reateK8sPolicyRequest\x12U\n\nk8s_policy\x18\x01 \x01(\x0b\x32-.kessel.inventory.v1beta1.resources.K8sPolicyB\x06\xbaH\x03\xc8\x01\x01R\nk8s_policy\"\x19\n\x17\x43reateK8sPolicyResponse\"o\n\x16UpdateK8sPolicyRequest\x12U\n\nk8s_policy\x18\x01 \x01(\x0b\x32-.kessel.inventory.v1beta1.resources.K8sPolicyB\x06\xbaH\x03\xc8\x01\x01R\nk8s_policy\"\x19\n\x17UpdateK8sPolicyResponse\"x\n\x16\x44\x65leteK8sPolicyRequest\x12^\n\rreporter_data\x18\x01 \x01(\x0b\x32\x30.kessel.inventory.v1beta1.resources.ReporterDataB\x06\xbaH\x03\xc8\x01\x01R\rreporter_data\"\x19\n\x17\x44\x65leteK8sPolicyResponse2\xed\x04\n\x16KesselK8sPolicyService\x12\xc4\x01\n\x0f\x43reateK8sPolicy\x12:.kessel.inventory.v1beta1.resources.CreateK8sPolicyRequest\x1a;.kessel.inventory.v1beta1.resources.CreateK8sPolicyResponse\"8\x82\xd3\xe4\x93\x02\x32\"-/api/inventory/v1beta1/resources/k8s-policies:\x01*\x12\xc4\x01\n\x0fUpdateK8sPolicy\x12:.kessel.inventory.v1beta1.resources.UpdateK8sPolicyRequest\x1a;.kessel.inventory.v1beta1.resources.UpdateK8sPolicyResponse\"8\x82\xd3\xe4\x93\x02\x32\x1a-/api/inventory/v1beta1/resources/k8s-policies:\x01*\x12\xc4\x01\n\x0f\x44\x65leteK8sPolicy\x12:.kessel.inventory.v1beta1.resources.DeleteK8sPolicyRequest\x1a;.kessel.inventory.v1beta1.resources.DeleteK8sPolicyResponse\"8\x82\xd3\xe4\x93\x02\x32*-/api/inventory/v1beta1/resources/k8s-policies:\x01*B\x86\x01\n2org.project_kessel.api.inventory.v1beta1.resourcesP\x01ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resourcesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.resources.k8s_policies_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n2org.project_kessel.api.inventory.v1beta1.resourcesP\001ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resources'
  _globals['_CREATEK8SPOLICYREQUEST'].fields_by_name['k8s_policy']._loaded_options = None
  _globals['_CREATEK8SPOLICYREQUEST'].fields_by_name['k8s_policy']._serialized_options = b'\272H\003\310\001\001'
  _globals['_UPDATEK8SPOLICYREQUEST'].fields_by_name['k8s_policy']._loaded_options = None
  _globals['_UPDATEK8SPOLICYREQUEST'].fields_by_name['k8s_policy']._serialized_options = b'\272H\003\310\001\001'
  _globals['_DELETEK8SPOLICYREQUEST'].fields_by_name['reporter_data']._loaded_options = None
  _globals['_DELETEK8SPOLICYREQUEST'].fields_by_name['reporter_data']._serialized_options = b'\272H\003\310\001\001'
  _globals['_KESSELK8SPOLICYSERVICE'].methods_by_name['CreateK8sPolicy']._loaded_options = None
  _globals['_KESSELK8SPOLICYSERVICE'].methods_by_name['CreateK8sPolicy']._serialized_options = b'\202\323\344\223\0022\"-/api/inventory/v1beta1/resources/k8s-policies:\001*'
  _globals['_KESSELK8SPOLICYSERVICE'].methods_by_name['UpdateK8sPolicy']._loaded_options = None
  _globals['_KESSELK8SPOLICYSERVICE'].methods_by_name['UpdateK8sPolicy']._serialized_options = b'\202\323\344\223\0022\032-/api/inventory/v1beta1/resources/k8s-policies:\001*'
  _globals['_KESSELK8SPOLICYSERVICE'].methods_by_name['DeleteK8sPolicy']._loaded_options = None
  _globals['_KESSELK8SPOLICYSERVICE'].methods_by_name['DeleteK8sPolicy']._serialized_options = b'\202\323\344\223\0022*-/api/inventory/v1beta1/resources/k8s-policies:\001*'
  _globals['_CREATEK8SPOLICYREQUEST']._serialized_start=269
  _globals['_CREATEK8SPOLICYREQUEST']._serialized_end=380
  _globals['_CREATEK8SPOLICYRESPONSE']._serialized_start=382
  _globals['_CREATEK8SPOLICYRESPONSE']._serialized_end=407
  _globals['_UPDATEK8SPOLICYREQUEST']._serialized_start=409
  _globals['_UPDATEK8SPOLICYREQUEST']._serialized_end=520
  _globals['_UPDATEK8SPOLICYRESPONSE']._serialized_start=522
  _globals['_UPDATEK8SPOLICYRESPONSE']._serialized_end=547
  _globals['_DELETEK8SPOLICYREQUEST']._serialized_start=549
  _globals['_DELETEK8SPOLICYREQUEST']._serialized_end=669
  _globals['_DELETEK8SPOLICYRESPONSE']._serialized_start=671
  _globals['_DELETEK8SPOLICYRESPONSE']._serialized_end=696
  _globals['_KESSELK8SPOLICYSERVICE']._serialized_start=699
  _globals['_KESSELK8SPOLICYSERVICE']._serialized_end=1320
# @@protoc_insertion_point(module_scope)
