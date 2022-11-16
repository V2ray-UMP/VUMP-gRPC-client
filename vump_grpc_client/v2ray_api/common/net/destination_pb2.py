# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/common/net/destination.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import network_pb2 as v2ray_dot_com_dot_core_dot_common_dot_net_dot_network__pb2
from . import address_pb2 as v2ray_dot_com_dot_core_dot_common_dot_net_dot_address__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/common/net/destination.proto',
  package='v2ray.core.common.net',
  syntax='proto3',
  serialized_options=_b('\n\031com.v2ray.core.common.netP\001Z\003net\252\002\025V2Ray.Core.Common.Net'),
  serialized_pb=_b('\n+v2ray.com/core/common/net/destination.proto\x12\x15v2ray.core.common.net\x1a\'v2ray.com/core/common/net/network.proto\x1a\'v2ray.com/core/common/net/address.proto\"}\n\x08\x45ndpoint\x12/\n\x07network\x18\x01 \x01(\x0e\x32\x1e.v2ray.core.common.net.Network\x12\x32\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x03 \x01(\rB:\n\x19\x63om.v2ray.core.common.netP\x01Z\x03net\xaa\x02\x15V2Ray.Core.Common.Netb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_net_dot_network__pb2.DESCRIPTOR,v2ray_dot_com_dot_core_dot_common_dot_net_dot_address__pb2.DESCRIPTOR,])




_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='v2ray.core.common.net.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='v2ray.core.common.net.Endpoint.network', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='v2ray.core.common.net.Endpoint.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='v2ray.core.common.net.Endpoint.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=277,
)

_ENDPOINT.fields_by_name['network'].enum_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_network__pb2._NETWORK
_ENDPOINT.fields_by_name['address'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_address__pb2._IPORDOMAIN
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), dict(
  DESCRIPTOR = _ENDPOINT,
  __module__ = 'v2ray.com.core.common.net.destination_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.net.Endpoint)
  ))
_sym_db.RegisterMessage(Endpoint)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
