# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta1/resources/rhel_hosts_service.proto
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
    'kessel/inventory/v1beta1/resources/rhel_hosts_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from kessel.inventory.v1beta1.resources import rhel_host_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__host__pb2
from kessel.inventory.v1beta1.resources import reporter_data_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_reporter__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;kessel/inventory/v1beta1/resources/rhel_hosts_service.proto\x12\"kessel.inventory.v1beta1.resources\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x62uf/validate/validate.proto\x1a\x32kessel/inventory/v1beta1/resources/rhel_host.proto\x1a\x36kessel/inventory/v1beta1/resources/reporter_data.proto\"k\n\x15\x43reateRhelHostRequest\x12R\n\trhel_host\x18\x01 \x01(\x0b\x32,.kessel.inventory.v1beta1.resources.RhelHostB\x06\xbaH\x03\xc8\x01\x01R\trhel_host\"\x18\n\x16\x43reateRhelHostResponse\"k\n\x15UpdateRhelHostRequest\x12R\n\trhel_host\x18\x01 \x01(\x0b\x32,.kessel.inventory.v1beta1.resources.RhelHostB\x06\xbaH\x03\xc8\x01\x01R\trhel_host\"\x18\n\x16UpdateRhelHostResponse\"w\n\x15\x44\x65leteRhelHostRequest\x12^\n\rreporter_data\x18\x01 \x01(\x0b\x32\x30.kessel.inventory.v1beta1.resources.ReporterDataB\x06\xbaH\x03\xc8\x01\x01R\rreporter_data\"\x18\n\x16\x44\x65leteRhelHostResponse2\xdd\x04\n\x15KesselRhelHostService\x12\xbf\x01\n\x0e\x43reateRhelHost\x12\x39.kessel.inventory.v1beta1.resources.CreateRhelHostRequest\x1a:.kessel.inventory.v1beta1.resources.CreateRhelHostResponse\"6\x82\xd3\xe4\x93\x02\x30\"+/api/inventory/v1beta1/resources/rhel-hosts:\x01*\x12\xbf\x01\n\x0eUpdateRhelHost\x12\x39.kessel.inventory.v1beta1.resources.UpdateRhelHostRequest\x1a:.kessel.inventory.v1beta1.resources.UpdateRhelHostResponse\"6\x82\xd3\xe4\x93\x02\x30\x1a+/api/inventory/v1beta1/resources/rhel-hosts:\x01*\x12\xbf\x01\n\x0e\x44\x65leteRhelHost\x12\x39.kessel.inventory.v1beta1.resources.DeleteRhelHostRequest\x1a:.kessel.inventory.v1beta1.resources.DeleteRhelHostResponse\"6\x82\xd3\xe4\x93\x02\x30*+/api/inventory/v1beta1/resources/rhel-hosts:\x01*B\x86\x01\n2org.project_kessel.api.inventory.v1beta1.resourcesP\x01ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resourcesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.resources.rhel_hosts_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n2org.project_kessel.api.inventory.v1beta1.resourcesP\001ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resources'
  _globals['_CREATERHELHOSTREQUEST'].fields_by_name['rhel_host']._loaded_options = None
  _globals['_CREATERHELHOSTREQUEST'].fields_by_name['rhel_host']._serialized_options = b'\272H\003\310\001\001'
  _globals['_UPDATERHELHOSTREQUEST'].fields_by_name['rhel_host']._loaded_options = None
  _globals['_UPDATERHELHOSTREQUEST'].fields_by_name['rhel_host']._serialized_options = b'\272H\003\310\001\001'
  _globals['_DELETERHELHOSTREQUEST'].fields_by_name['reporter_data']._loaded_options = None
  _globals['_DELETERHELHOSTREQUEST'].fields_by_name['reporter_data']._serialized_options = b'\272H\003\310\001\001'
  _globals['_KESSELRHELHOSTSERVICE'].methods_by_name['CreateRhelHost']._loaded_options = None
  _globals['_KESSELRHELHOSTSERVICE'].methods_by_name['CreateRhelHost']._serialized_options = b'\202\323\344\223\0020\"+/api/inventory/v1beta1/resources/rhel-hosts:\001*'
  _globals['_KESSELRHELHOSTSERVICE'].methods_by_name['UpdateRhelHost']._loaded_options = None
  _globals['_KESSELRHELHOSTSERVICE'].methods_by_name['UpdateRhelHost']._serialized_options = b'\202\323\344\223\0020\032+/api/inventory/v1beta1/resources/rhel-hosts:\001*'
  _globals['_KESSELRHELHOSTSERVICE'].methods_by_name['DeleteRhelHost']._loaded_options = None
  _globals['_KESSELRHELHOSTSERVICE'].methods_by_name['DeleteRhelHost']._serialized_options = b'\202\323\344\223\0020*+/api/inventory/v1beta1/resources/rhel-hosts:\001*'
  _globals['_CREATERHELHOSTREQUEST']._serialized_start=266
  _globals['_CREATERHELHOSTREQUEST']._serialized_end=373
  _globals['_CREATERHELHOSTRESPONSE']._serialized_start=375
  _globals['_CREATERHELHOSTRESPONSE']._serialized_end=399
  _globals['_UPDATERHELHOSTREQUEST']._serialized_start=401
  _globals['_UPDATERHELHOSTREQUEST']._serialized_end=508
  _globals['_UPDATERHELHOSTRESPONSE']._serialized_start=510
  _globals['_UPDATERHELHOSTRESPONSE']._serialized_end=534
  _globals['_DELETERHELHOSTREQUEST']._serialized_start=536
  _globals['_DELETERHELHOSTREQUEST']._serialized_end=655
  _globals['_DELETERHELHOSTRESPONSE']._serialized_start=657
  _globals['_DELETERHELHOSTRESPONSE']._serialized_end=681
  _globals['_KESSELRHELHOSTSERVICE']._serialized_start=684
  _globals['_KESSELRHELHOSTSERVICE']._serialized_end=1289
# @@protoc_insertion_point(module_scope)
