# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: buf/validate/priv/private.proto
# Protobuf Python Version: 6.30.0
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
    0,
    '',
    'buf/validate/priv/private.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x62uf/validate/priv/private.proto\x12\x11\x62uf.validate.priv\x1a google/protobuf/descriptor.proto\">\n\x10\x46ieldConstraints\x12*\n\x03\x63\x65l\x18\x01 \x03(\x0b\x32\x1d.buf.validate.priv.Constraint\"=\n\nConstraint\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nexpression\x18\x03 \x01(\t:U\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\x88\t \x01(\x0b\x32#.buf.validate.priv.FieldConstraints\x88\x01\x01\x42w\n\x17\x62uild.buf.validate.privB\x0cPrivateProtoP\x01ZLbuf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate/privb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.priv.private_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027build.buf.validate.privB\014PrivateProtoP\001ZLbuf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate/priv'
  _globals['_FIELDCONSTRAINTS']._serialized_start=88
  _globals['_FIELDCONSTRAINTS']._serialized_end=150
  _globals['_CONSTRAINT']._serialized_start=152
  _globals['_CONSTRAINT']._serialized_end=213
# @@protoc_insertion_point(module_scope)
