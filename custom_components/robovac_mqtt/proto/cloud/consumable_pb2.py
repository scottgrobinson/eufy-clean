# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/cloud/consumable.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproto/cloud/consumable.proto\x12\x0bproto.cloud\"\xe4\x01\n\x11\x43onsumableRequest\x12\x38\n\x0breset_types\x18\x01 \x03(\x0e\x32#.proto.cloud.ConsumableRequest.Type\"\x94\x01\n\x04Type\x12\x0e\n\nSIDE_BRUSH\x10\x00\x12\x11\n\rROLLING_BRUSH\x10\x01\x12\x0f\n\x0b\x46ILTER_MESH\x10\x02\x12\n\n\x06SCRAPE\x10\x03\x12\n\n\x06SENSOR\x10\x04\x12\x07\n\x03MOP\x10\x05\x12\x0b\n\x07\x44USTBAG\x10\x06\x12\x13\n\x0f\x44IRTY_WATERTANK\x10\x07\x12\x15\n\x11\x44IRTY_WATERFILTER\x10\x08\"\xe7\x04\n\x11\x43onsumableRuntime\x12;\n\nside_brush\x18\x01 \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12>\n\rrolling_brush\x18\x02 \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12<\n\x0b\x66ilter_mesh\x18\x03 \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12\x37\n\x06scrape\x18\x04 \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12\x37\n\x06sensor\x18\x05 \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12\x34\n\x03mop\x18\x06 \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12\x38\n\x07\x64ustbag\x18\x07 \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12@\n\x0f\x64irty_watertank\x18\n \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12\x42\n\x11\x64irty_waterfilter\x18\x0b \x01(\x0b\x32\'.proto.cloud.ConsumableRuntime.Duration\x12\x11\n\tlast_time\x18\x14 \x01(\x04\x1a\x1c\n\x08\x44uration\x12\x10\n\x08\x64uration\x18\x01 \x01(\r\"E\n\x12\x43onsumableResponse\x12/\n\x07runtime\x18\x01 \x01(\x0b\x32\x1e.proto.cloud.ConsumableRuntimeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.cloud.consumable_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONSUMABLEREQUEST._serialized_start=46
  _CONSUMABLEREQUEST._serialized_end=274
  _CONSUMABLEREQUEST_TYPE._serialized_start=126
  _CONSUMABLEREQUEST_TYPE._serialized_end=274
  _CONSUMABLERUNTIME._serialized_start=277
  _CONSUMABLERUNTIME._serialized_end=892
  _CONSUMABLERUNTIME_DURATION._serialized_start=864
  _CONSUMABLERUNTIME_DURATION._serialized_end=892
  _CONSUMABLERESPONSE._serialized_start=894
  _CONSUMABLERESPONSE._serialized_end=963
# @@protoc_insertion_point(module_scope)
