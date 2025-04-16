# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta2/resource_service.proto
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
    'kessel/inventory/v1beta2/resource_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kessel.inventory.v1beta2 import resource_pb2 as kessel_dot_inventory_dot_v1beta2_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/kessel/inventory/v1beta2/resource_service.proto\x12\x18kessel.inventory.v1beta2\x1a\'kessel/inventory/v1beta2/resource.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x62uf/validate/validate.proto\"W\n\x15ReportResourceRequest\x12>\n\x08resource\x18\x01 \x01(\x0b\x32\".kessel.inventory.v1beta2.ResourceR\x08resource\"\x18\n\x16ReportResourceResponse\"z\n\x15\x44\x65leteResourceRequest\x12\x33\n\x11local_resource_id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x0flocalResourceId\x12,\n\rreporter_type\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x0creporterType\"\x18\n\x16\x44\x65leteResourceResponse2\xdd\x02\n\x15KesselResourceService\x12\xa0\x01\n\x0eReportResource\x12/.kessel.inventory.v1beta2.ReportResourceRequest\x1a\x30.kessel.inventory.v1beta2.ReportResourceResponse\"+\x82\xd3\xe4\x93\x02%\" /api/inventory/v1beta2/resources:\x01*\x12\xa0\x01\n\x0e\x44\x65leteResource\x12/.kessel.inventory.v1beta2.DeleteResourceRequest\x1a\x30.kessel.inventory.v1beta2.DeleteResourceResponse\"+\x82\xd3\xe4\x93\x02%* /api/inventory/v1beta2/resources:\x01*Br\n(org.project_kessel.api.inventory.v1beta2P\x01ZDgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta2.resource_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(org.project_kessel.api.inventory.v1beta2P\001ZDgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta2'
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['local_resource_id']._loaded_options = None
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['local_resource_id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['reporter_type']._loaded_options = None
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['reporter_type']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_KESSELRESOURCESERVICE'].methods_by_name['ReportResource']._loaded_options = None
  _globals['_KESSELRESOURCESERVICE'].methods_by_name['ReportResource']._serialized_options = b'\202\323\344\223\002%\" /api/inventory/v1beta2/resources:\001*'
  _globals['_KESSELRESOURCESERVICE'].methods_by_name['DeleteResource']._loaded_options = None
  _globals['_KESSELRESOURCESERVICE'].methods_by_name['DeleteResource']._serialized_options = b'\202\323\344\223\002%* /api/inventory/v1beta2/resources:\001*'
  _globals['_REPORTRESOURCEREQUEST']._serialized_start=177
  _globals['_REPORTRESOURCEREQUEST']._serialized_end=264
  _globals['_REPORTRESOURCERESPONSE']._serialized_start=266
  _globals['_REPORTRESOURCERESPONSE']._serialized_end=290
  _globals['_DELETERESOURCEREQUEST']._serialized_start=292
  _globals['_DELETERESOURCEREQUEST']._serialized_end=414
  _globals['_DELETERESOURCERESPONSE']._serialized_start=416
  _globals['_DELETERESOURCERESPONSE']._serialized_end=440
  _globals['_KESSELRESOURCESERVICE']._serialized_start=443
  _globals['_KESSELRESOURCESERVICE']._serialized_end=792
# @@protoc_insertion_point(module_scope)
