# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resourcesecretmap/StorageSecretMap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import airavata_mft_sdk.airavata_mft_sdk.airavata_mft_sdk.CredCommon_pb2 as CredCommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(resourcesecretmap/StorageSecretMap.proto\x12\x33org.apache.airavata.mft.storage.stubs.storagesecret\x1a\x10\x43redCommon.proto\"\x92\x02\n\rStorageSecret\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tstorageId\x18\x02 \x01(\t\x12\x10\n\x08secretId\x18\x03 \x01(\t\x12\\\n\x04type\x18\x04 \x01(\x0e\x32N.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret.StorageType\"r\n\x0bStorageType\x12\x06\n\x02S3\x10\x00\x12\x07\n\x03SCP\x10\x01\x12\x07\n\x03\x46TP\x10\x02\x12\t\n\x05LOCAL\x10\x03\x12\x07\n\x03\x42OX\x10\x04\x12\x0b\n\x07\x44ROPBOX\x10\x05\x12\x07\n\x03GCS\x10\x06\x12\t\n\x05\x41ZURE\x10\x07\x12\t\n\x05SWIFT\x10\x08\x12\t\n\x05ODATA\x10\t\"\xde\x01\n\x1aStorageSecretCreateRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x10\n\x08secretId\x18\x02 \x01(\t\x12\\\n\x04type\x18\x03 \x01(\x0e\x32N.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret.StorageType\x12=\n\nauthzToken\x18\x04 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"g\n\x1aStorageSecretDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"-\n\x1bStorageSecretDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\xb6\x01\n\x1aStorageSecretUpdateRequest\x12Y\n\rstorageSecret\x18\x01 \x01(\x0b\x32\x42.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"x\n\x1bStorageSecretUpdateResponse\x12Y\n\rstorageSecret\x18\x01 \x01(\x0b\x32\x42.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret\"d\n\x17StorageSecretGetRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"\xcc\x01\n\x1aStorageSecretSearchRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\\\n\x04type\x18\x02 \x01(\x0e\x32N.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret.StorageType\x12=\n\nauthzToken\x18\x03 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"x\n\x1bStorageSecretSearchResponse\x12Y\n\rstorageSecret\x18\x01 \x01(\x0b\x32\x42.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret2\x9b\x07\n\x14StorageSecretService\x12\xa4\x01\n\x10getStorageSecret\x12L.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretGetRequest\x1a\x42.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret\x12\xb8\x01\n\x13searchStorageSecret\x12O.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretSearchRequest\x1aP.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretSearchResponse\x12\xaa\x01\n\x13\x63reateStorageSecret\x12O.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretCreateRequest\x1a\x42.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret\x12\xb8\x01\n\x13updateStorageSecret\x12O.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretUpdateRequest\x1aP.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretUpdateResponse\x12\xb8\x01\n\x13\x64\x65leteStorageSecret\x12O.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretDeleteRequest\x1aP.org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretDeleteResponseB\x02P\x01\x62\x06proto3')



_STORAGESECRET = DESCRIPTOR.message_types_by_name['StorageSecret']
_STORAGESECRETCREATEREQUEST = DESCRIPTOR.message_types_by_name['StorageSecretCreateRequest']
_STORAGESECRETDELETEREQUEST = DESCRIPTOR.message_types_by_name['StorageSecretDeleteRequest']
_STORAGESECRETDELETERESPONSE = DESCRIPTOR.message_types_by_name['StorageSecretDeleteResponse']
_STORAGESECRETUPDATEREQUEST = DESCRIPTOR.message_types_by_name['StorageSecretUpdateRequest']
_STORAGESECRETUPDATERESPONSE = DESCRIPTOR.message_types_by_name['StorageSecretUpdateResponse']
_STORAGESECRETGETREQUEST = DESCRIPTOR.message_types_by_name['StorageSecretGetRequest']
_STORAGESECRETSEARCHREQUEST = DESCRIPTOR.message_types_by_name['StorageSecretSearchRequest']
_STORAGESECRETSEARCHRESPONSE = DESCRIPTOR.message_types_by_name['StorageSecretSearchResponse']
_STORAGESECRET_STORAGETYPE = _STORAGESECRET.enum_types_by_name['StorageType']
StorageSecret = _reflection.GeneratedProtocolMessageType('StorageSecret', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRET,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret)
  })
_sym_db.RegisterMessage(StorageSecret)

StorageSecretCreateRequest = _reflection.GeneratedProtocolMessageType('StorageSecretCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETCREATEREQUEST,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretCreateRequest)
  })
_sym_db.RegisterMessage(StorageSecretCreateRequest)

StorageSecretDeleteRequest = _reflection.GeneratedProtocolMessageType('StorageSecretDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETDELETEREQUEST,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretDeleteRequest)
  })
_sym_db.RegisterMessage(StorageSecretDeleteRequest)

StorageSecretDeleteResponse = _reflection.GeneratedProtocolMessageType('StorageSecretDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETDELETERESPONSE,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretDeleteResponse)
  })
_sym_db.RegisterMessage(StorageSecretDeleteResponse)

StorageSecretUpdateRequest = _reflection.GeneratedProtocolMessageType('StorageSecretUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETUPDATEREQUEST,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretUpdateRequest)
  })
_sym_db.RegisterMessage(StorageSecretUpdateRequest)

StorageSecretUpdateResponse = _reflection.GeneratedProtocolMessageType('StorageSecretUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETUPDATERESPONSE,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretUpdateResponse)
  })
_sym_db.RegisterMessage(StorageSecretUpdateResponse)

StorageSecretGetRequest = _reflection.GeneratedProtocolMessageType('StorageSecretGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETGETREQUEST,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretGetRequest)
  })
_sym_db.RegisterMessage(StorageSecretGetRequest)

StorageSecretSearchRequest = _reflection.GeneratedProtocolMessageType('StorageSecretSearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETSEARCHREQUEST,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretSearchRequest)
  })
_sym_db.RegisterMessage(StorageSecretSearchRequest)

StorageSecretSearchResponse = _reflection.GeneratedProtocolMessageType('StorageSecretSearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESECRETSEARCHRESPONSE,
  '__module__' : 'resourcesecretmap.StorageSecretMap_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretSearchResponse)
  })
_sym_db.RegisterMessage(StorageSecretSearchResponse)

_STORAGESECRETSERVICE = DESCRIPTOR.services_by_name['StorageSecretService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _STORAGESECRET._serialized_start=116
  _STORAGESECRET._serialized_end=390
  _STORAGESECRET_STORAGETYPE._serialized_start=276
  _STORAGESECRET_STORAGETYPE._serialized_end=390
  _STORAGESECRETCREATEREQUEST._serialized_start=393
  _STORAGESECRETCREATEREQUEST._serialized_end=615
  _STORAGESECRETDELETEREQUEST._serialized_start=617
  _STORAGESECRETDELETEREQUEST._serialized_end=720
  _STORAGESECRETDELETERESPONSE._serialized_start=722
  _STORAGESECRETDELETERESPONSE._serialized_end=767
  _STORAGESECRETUPDATEREQUEST._serialized_start=770
  _STORAGESECRETUPDATEREQUEST._serialized_end=952
  _STORAGESECRETUPDATERESPONSE._serialized_start=954
  _STORAGESECRETUPDATERESPONSE._serialized_end=1074
  _STORAGESECRETGETREQUEST._serialized_start=1076
  _STORAGESECRETGETREQUEST._serialized_end=1176
  _STORAGESECRETSEARCHREQUEST._serialized_start=1179
  _STORAGESECRETSEARCHREQUEST._serialized_end=1383
  _STORAGESECRETSEARCHRESPONSE._serialized_start=1385
  _STORAGESECRETSEARCHRESPONSE._serialized_end=1505
  _STORAGESECRETSERVICE._serialized_start=1508
  _STORAGESECRETSERVICE._serialized_end=2431
# @@protoc_insertion_point(module_scope)
