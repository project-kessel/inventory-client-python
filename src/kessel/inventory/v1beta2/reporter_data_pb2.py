# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta2/reporter_data.proto
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
    'kessel/inventory/v1beta2/reporter_data.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,kessel/inventory/v1beta2/reporter_data.proto\x12\x18kessel.inventory.v1beta2\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1b\x62uf/validate/validate.proto\"\xea\x02\n\x0cReporterData\x12,\n\rreporter_type\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x0creporterType\x12\x39\n\x14reporter_instance_id\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x12reporterInstanceId\x12)\n\x10reporter_version\x18\x08 \x01(\tR\x0freporterVersion\x12\x33\n\x11local_resource_id\x18\x04 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x0flocalResourceId\x12\"\n\x08\x61pi_href\x18\x05 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x07\x61piHref\x12*\n\x0c\x63onsole_href\x18\x06 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x0b\x63onsoleHref\x12\x41\n\rresource_data\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xbaH\x00R\x0cresourceDataBr\n(org.project_kessel.api.inventory.v1beta2P\x01ZDgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta2.reporter_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(org.project_kessel.api.inventory.v1beta2P\001ZDgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta2'
  _globals['_REPORTERDATA'].fields_by_name['reporter_type']._loaded_options = None
  _globals['_REPORTERDATA'].fields_by_name['reporter_type']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_REPORTERDATA'].fields_by_name['reporter_instance_id']._loaded_options = None
  _globals['_REPORTERDATA'].fields_by_name['reporter_instance_id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_REPORTERDATA'].fields_by_name['local_resource_id']._loaded_options = None
  _globals['_REPORTERDATA'].fields_by_name['local_resource_id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_REPORTERDATA'].fields_by_name['api_href']._loaded_options = None
  _globals['_REPORTERDATA'].fields_by_name['api_href']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_REPORTERDATA'].fields_by_name['console_href']._loaded_options = None
  _globals['_REPORTERDATA'].fields_by_name['console_href']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_REPORTERDATA'].fields_by_name['resource_data']._loaded_options = None
  _globals['_REPORTERDATA'].fields_by_name['resource_data']._serialized_options = b'\272H\000'
  _globals['_REPORTERDATA']._serialized_start=134
  _globals['_REPORTERDATA']._serialized_end=496
# @@protoc_insertion_point(module_scope)
