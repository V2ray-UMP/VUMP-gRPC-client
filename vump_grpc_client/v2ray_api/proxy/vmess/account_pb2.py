# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/proxy/vmess/account.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...common.protocol import headers_pb2 as v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_headers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/proxy/vmess/account.proto',
  package='v2ray.core.proxy.vmess',
  syntax='proto3',
  serialized_options=_b('\n\032com.v2ray.core.proxy.vmessP\001Z\005vmess\252\002\026V2Ray.Core.Proxy.Vmess'),
  serialized_pb=_b('\n(v2ray.com/core/proxy/vmess/account.proto\x12\x16v2ray.core.proxy.vmess\x1a,v2ray.com/core/common/protocol/headers.proto\"n\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x61lter_id\x18\x02 \x01(\r\x12\x45\n\x11security_settings\x18\x03 \x01(\x0b\x32*.v2ray.core.common.protocol.SecurityConfigB>\n\x1a\x63om.v2ray.core.proxy.vmessP\x01Z\x05vmess\xaa\x02\x16V2Ray.Core.Proxy.Vmessb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_headers__pb2.DESCRIPTOR,])




_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='v2ray.core.proxy.vmess.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v2ray.core.proxy.vmess.Account.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alter_id', full_name='v2ray.core.proxy.vmess.Account.alter_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security_settings', full_name='v2ray.core.proxy.vmess.Account.security_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=114,
  serialized_end=224,
)

_ACCOUNT.fields_by_name['security_settings'].message_type = v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_headers__pb2._SECURITYCONFIG
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'v2ray.com.core.proxy.vmess.account_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vmess.Account)
  ))
_sym_db.RegisterMessage(Account)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
