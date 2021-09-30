# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wine_quality.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wine_quality.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12wine_quality.proto\"n\n\x12WineQualityRequest\x12\x15\n\rfixed_acidity\x18\x01 \x01(\x02\x12\x18\n\x10volatile_acidity\x18\x02 \x01(\x02\x12\x16\n\x0e\x63itric_acidity\x18\x03 \x01(\x02\x12\x0f\n\x07\x61lcohol\x18\x04 \x01(\x02\"+\n\x13WineQualityResponse\x12\x14\n\x0cwine_quality\x18\x01 \x01(\x05\x32H\n\x0bWineQuality\x12\x39\n\x0cwine_quality\x12\x13.WineQualityRequest\x1a\x14.WineQualityResponseb\x06proto3'
)




_WINEQUALITYREQUEST = _descriptor.Descriptor(
  name='WineQualityRequest',
  full_name='WineQualityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixed_acidity', full_name='WineQualityRequest.fixed_acidity', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volatile_acidity', full_name='WineQualityRequest.volatile_acidity', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='citric_acidity', full_name='WineQualityRequest.citric_acidity', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alcohol', full_name='WineQualityRequest.alcohol', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=132,
)


_WINEQUALITYRESPONSE = _descriptor.Descriptor(
  name='WineQualityResponse',
  full_name='WineQualityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wine_quality', full_name='WineQualityResponse.wine_quality', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=134,
  serialized_end=177,
)

DESCRIPTOR.message_types_by_name['WineQualityRequest'] = _WINEQUALITYREQUEST
DESCRIPTOR.message_types_by_name['WineQualityResponse'] = _WINEQUALITYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WineQualityRequest = _reflection.GeneratedProtocolMessageType('WineQualityRequest', (_message.Message,), {
  'DESCRIPTOR' : _WINEQUALITYREQUEST,
  '__module__' : 'wine_quality_pb2'
  # @@protoc_insertion_point(class_scope:WineQualityRequest)
  })
_sym_db.RegisterMessage(WineQualityRequest)

WineQualityResponse = _reflection.GeneratedProtocolMessageType('WineQualityResponse', (_message.Message,), {
  'DESCRIPTOR' : _WINEQUALITYRESPONSE,
  '__module__' : 'wine_quality_pb2'
  # @@protoc_insertion_point(class_scope:WineQualityResponse)
  })
_sym_db.RegisterMessage(WineQualityResponse)



_WINEQUALITY = _descriptor.ServiceDescriptor(
  name='WineQuality',
  full_name='WineQuality',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=179,
  serialized_end=251,
  methods=[
  _descriptor.MethodDescriptor(
    name='wine_quality',
    full_name='WineQuality.wine_quality',
    index=0,
    containing_service=None,
    input_type=_WINEQUALITYREQUEST,
    output_type=_WINEQUALITYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WINEQUALITY)

DESCRIPTOR.services_by_name['WineQuality'] = _WINEQUALITY

# @@protoc_insertion_point(module_scope)
