# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/common/protocol/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..serial import typed_message_pb2 as v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/common/protocol/user.proto',
  package='v2ray.core.common.protocol',
  syntax='proto3',
  serialized_options=_b('\n\036com.v2ray.core.common.protocolP\001Z\010protocol\252\002\032V2Ray.Core.Common.Protocol'),
  serialized_pb=_b('\n)v2ray.com/core/common/protocol/user.proto\x12\x1av2ray.core.common.protocol\x1a\x30v2ray.com/core/common/serial/typed_message.proto\"]\n\x04User\x12\r\n\x05level\x18\x01 \x01(\r\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x37\n\x07\x61\x63\x63ount\x18\x03 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessageBI\n\x1e\x63om.v2ray.core.common.protocolP\x01Z\x08protocol\xaa\x02\x1aV2Ray.Core.Common.Protocolb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='v2ray.core.common.protocol.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='v2ray.core.common.protocol.User.level', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='v2ray.core.common.protocol.User.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='v2ray.core.common.protocol.User.account', index=2,
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
  serialized_start=123,
  serialized_end=216,
)

_USER.fields_by_name['account'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'v2ray.com.core.common.protocol.user_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.protocol.User)
  ))
_sym_db.RegisterMessage(User)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
