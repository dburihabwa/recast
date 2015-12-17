# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playcloud.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='playcloud.proto',
  package='',
  syntax='proto3',
  serialized_pb=b'\n\x0fplaycloud.proto\"\xa0\x01\n\rEncodeRequest\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x43\n\x13\x65ncoding_parameters\x18\x02 \x03(\x0b\x32&.EncodeRequest.EncodingParametersEntry\x1a\x39\n\x17\x45ncodingParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"!\n\x0b\x45ncodeReply\x12\x12\n\nenc_blocks\x18\x01 \x01(\x0c\"\xa3\x01\n\rDecodeRequest\x12\x12\n\nenc_blocks\x18\x01 \x03(\x0c\x12\x43\n\x13\x64\x65\x63oding_parameters\x18\x02 \x03(\x0b\x32&.DecodeRequest.DecodingParametersEntry\x1a\x39\n\x17\x44\x65\x63odingParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\" \n\x0b\x44\x65\x63odeReply\x12\x11\n\tdec_block\x18\x01 \x01(\x0c\x32\x64\n\x0e\x45ncoderDecoder\x12(\n\x06\x45ncode\x12\x0e.EncodeRequest\x1a\x0c.EncodeReply\"\x00\x12(\n\x06\x44\x65\x63ode\x12\x0e.DecodeRequest\x1a\x0c.DecodeReply\"\x00\x62\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENCODEREQUEST_ENCODINGPARAMETERSENTRY = _descriptor.Descriptor(
  name='EncodingParametersEntry',
  full_name='EncodeRequest.EncodingParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EncodeRequest.EncodingParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='EncodeRequest.EncodingParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=180,
)

_ENCODEREQUEST = _descriptor.Descriptor(
  name='EncodeRequest',
  full_name='EncodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='EncodeRequest.payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encoding_parameters', full_name='EncodeRequest.encoding_parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENCODEREQUEST_ENCODINGPARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=180,
)


_ENCODEREPLY = _descriptor.Descriptor(
  name='EncodeReply',
  full_name='EncodeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enc_blocks', full_name='EncodeReply.enc_blocks', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=215,
)


_DECODEREQUEST_DECODINGPARAMETERSENTRY = _descriptor.Descriptor(
  name='DecodingParametersEntry',
  full_name='DecodeRequest.DecodingParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DecodeRequest.DecodingParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DecodeRequest.DecodingParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=381,
)

_DECODEREQUEST = _descriptor.Descriptor(
  name='DecodeRequest',
  full_name='DecodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enc_blocks', full_name='DecodeRequest.enc_blocks', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decoding_parameters', full_name='DecodeRequest.decoding_parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DECODEREQUEST_DECODINGPARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=381,
)


_DECODEREPLY = _descriptor.Descriptor(
  name='DecodeReply',
  full_name='DecodeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dec_block', full_name='DecodeReply.dec_block', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=415,
)

_ENCODEREQUEST_ENCODINGPARAMETERSENTRY.containing_type = _ENCODEREQUEST
_ENCODEREQUEST.fields_by_name['encoding_parameters'].message_type = _ENCODEREQUEST_ENCODINGPARAMETERSENTRY
_DECODEREQUEST_DECODINGPARAMETERSENTRY.containing_type = _DECODEREQUEST
_DECODEREQUEST.fields_by_name['decoding_parameters'].message_type = _DECODEREQUEST_DECODINGPARAMETERSENTRY
DESCRIPTOR.message_types_by_name['EncodeRequest'] = _ENCODEREQUEST
DESCRIPTOR.message_types_by_name['EncodeReply'] = _ENCODEREPLY
DESCRIPTOR.message_types_by_name['DecodeRequest'] = _DECODEREQUEST
DESCRIPTOR.message_types_by_name['DecodeReply'] = _DECODEREPLY

EncodeRequest = _reflection.GeneratedProtocolMessageType('EncodeRequest', (_message.Message,), dict(

  EncodingParametersEntry = _reflection.GeneratedProtocolMessageType('EncodingParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENCODEREQUEST_ENCODINGPARAMETERSENTRY,
    __module__ = 'playcloud_pb2'
    # @@protoc_insertion_point(class_scope:EncodeRequest.EncodingParametersEntry)
    ))
  ,
  DESCRIPTOR = _ENCODEREQUEST,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:EncodeRequest)
  ))
_sym_db.RegisterMessage(EncodeRequest)
_sym_db.RegisterMessage(EncodeRequest.EncodingParametersEntry)

EncodeReply = _reflection.GeneratedProtocolMessageType('EncodeReply', (_message.Message,), dict(
  DESCRIPTOR = _ENCODEREPLY,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:EncodeReply)
  ))
_sym_db.RegisterMessage(EncodeReply)

DecodeRequest = _reflection.GeneratedProtocolMessageType('DecodeRequest', (_message.Message,), dict(

  DecodingParametersEntry = _reflection.GeneratedProtocolMessageType('DecodingParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _DECODEREQUEST_DECODINGPARAMETERSENTRY,
    __module__ = 'playcloud_pb2'
    # @@protoc_insertion_point(class_scope:DecodeRequest.DecodingParametersEntry)
    ))
  ,
  DESCRIPTOR = _DECODEREQUEST,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:DecodeRequest)
  ))
_sym_db.RegisterMessage(DecodeRequest)
_sym_db.RegisterMessage(DecodeRequest.DecodingParametersEntry)

DecodeReply = _reflection.GeneratedProtocolMessageType('DecodeReply', (_message.Message,), dict(
  DESCRIPTOR = _DECODEREPLY,
  __module__ = 'playcloud_pb2'
  # @@protoc_insertion_point(class_scope:DecodeReply)
  ))
_sym_db.RegisterMessage(DecodeReply)


_ENCODEREQUEST_ENCODINGPARAMETERSENTRY.has_options = True
_ENCODEREQUEST_ENCODINGPARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
_DECODEREQUEST_DECODINGPARAMETERSENTRY.has_options = True
_DECODEREQUEST_DECODINGPARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterEncoderDecoderServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Decode(self, request, context):
    raise NotImplementedError()
class EarlyAdopterEncoderDecoderServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterEncoderDecoderStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request):
    raise NotImplementedError()
  Encode.async = None
  @abc.abstractmethod
  def Decode(self, request):
    raise NotImplementedError()
  Decode.async = None
def early_adopter_create_EncoderDecoder_server(servicer, port, private_key=None, certificate_chain=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  method_service_descriptions = {
    "Decode": alpha_utilities.unary_unary_service_description(
      servicer.Decode,
      playcloud_pb2.DecodeRequest.FromString,
      playcloud_pb2.DecodeReply.SerializeToString,
    ),
    "Encode": alpha_utilities.unary_unary_service_description(
      servicer.Encode,
      playcloud_pb2.EncodeRequest.FromString,
      playcloud_pb2.EncodeReply.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("EncoderDecoder", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_EncoderDecoder_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  method_invocation_descriptions = {
    "Decode": alpha_utilities.unary_unary_invocation_description(
      playcloud_pb2.DecodeRequest.SerializeToString,
      playcloud_pb2.DecodeReply.FromString,
    ),
    "Encode": alpha_utilities.unary_unary_invocation_description(
      playcloud_pb2.EncodeRequest.SerializeToString,
      playcloud_pb2.EncodeReply.FromString,
    ),
  }
  return early_adopter_implementations.stub("EncoderDecoder", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaEncoderDecoderServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Decode(self, request, context):
    raise NotImplementedError()

class BetaEncoderDecoderStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Encode(self, request, timeout):
    raise NotImplementedError()
  Encode.future = None
  @abc.abstractmethod
  def Decode(self, request, timeout):
    raise NotImplementedError()
  Decode.future = None

def beta_create_EncoderDecoder_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  request_deserializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeRequest.FromString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeRequest.FromString,
  }
  response_serializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeReply.SerializeToString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeReply.SerializeToString,
  }
  method_implementations = {
    ('EncoderDecoder', 'Decode'): face_utilities.unary_unary_inline(servicer.Decode),
    ('EncoderDecoder', 'Encode'): face_utilities.unary_unary_inline(servicer.Encode),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_EncoderDecoder_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  import playcloud_pb2
  request_serializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeRequest.SerializeToString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeRequest.SerializeToString,
  }
  response_deserializers = {
    ('EncoderDecoder', 'Decode'): playcloud_pb2.DecodeReply.FromString,
    ('EncoderDecoder', 'Encode'): playcloud_pb2.EncodeReply.FromString,
  }
  cardinalities = {
    'Decode': cardinality.Cardinality.UNARY_UNARY,
    'Encode': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'EncoderDecoder', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
