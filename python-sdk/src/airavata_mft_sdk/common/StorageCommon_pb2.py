# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/StorageCommon.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63ommon/StorageCommon.proto\x12\x35org.apache.airavata.mft.resource.stubs.storage.common\".\n\x19StorageTypeResolveRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"\xea\x01\n\x1aStorageTypeResolveResponse\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x13\n\x0bstorageName\x18\x02 \x01(\t\x12W\n\x0bstorageType\x18\x03 \x01(\x0e\x32\x42.org.apache.airavata.mft.resource.stubs.storage.common.StorageType\x12K\n\x05\x65rror\x18\x04 \x01(\x0e\x32<.org.apache.airavata.mft.resource.stubs.storage.common.Error\"\xdd\x01\n\x10SecretForStorage\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x10\n\x08secretId\x18\x02 \x01(\t\x12W\n\x0bstorageType\x18\x03 \x01(\x0e\x32\x42.org.apache.airavata.mft.resource.stubs.storage.common.StorageType\x12K\n\x05\x65rror\x18\x04 \x01(\x0e\x32<.org.apache.airavata.mft.resource.stubs.storage.common.Error\"/\n\x1aSecretForStorageGetRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"2\n\x1dSecretForStorageDeleteRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"0\n\x1eSecretForStorageDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x93\x01\n\x10StorageListEntry\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x13\n\x0bstorageName\x18\x02 \x01(\t\x12W\n\x0bstorageType\x18\x03 \x01(\x0e\x32\x42.org.apache.airavata.mft.resource.stubs.storage.common.StorageType\"s\n\x13StorageListResponse\x12\\\n\x0bstorageList\x18\x01 \x03(\x0b\x32G.org.apache.airavata.mft.resource.stubs.storage.common.StorageListEntry\":\n\x12StorageListRequest\x12\x12\n\npageNumber\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05*r\n\x0bStorageType\x12\x06\n\x02S3\x10\x00\x12\x07\n\x03SCP\x10\x01\x12\x07\n\x03\x46TP\x10\x02\x12\t\n\x05LOCAL\x10\x03\x12\x07\n\x03\x42OX\x10\x04\x12\x0b\n\x07\x44ROPBOX\x10\x05\x12\x07\n\x03GCS\x10\x06\x12\t\n\x05\x41ZURE\x10\x07\x12\t\n\x05SWIFT\x10\x08\x12\t\n\x05ODATA\x10\t*?\n\x05\x45rror\x12\r\n\tNOT_FOUND\x10\x00\x12\x11\n\rNO_PERMISSION\x10\x01\x12\x14\n\x10LIMIT_OVERFLOWED\x10\x02\x32\xa6\x07\n\x14StorageCommonService\x12\xb9\x01\n\x12resolveStorageType\x12P.org.apache.airavata.mft.resource.stubs.storage.common.StorageTypeResolveRequest\x1aQ.org.apache.airavata.mft.resource.stubs.storage.common.StorageTypeResolveResponse\x12\xac\x01\n\x18registerSecretForStorage\x12G.org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorage\x1aG.org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorage\x12\xb1\x01\n\x13getSecretForStorage\x12Q.org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorageGetRequest\x1aG.org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorage\x12\xc6\x01\n\x17\x64\x65leteSecretsForStorage\x12T.org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorageDeleteRequest\x1aU.org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorageDeleteResponse\x12\xa5\x01\n\x0clistStorages\x12I.org.apache.airavata.mft.resource.stubs.storage.common.StorageListRequest\x1aJ.org.apache.airavata.mft.resource.stubs.storage.common.StorageListResponseB\x02P\x01\x62\x06proto3')

_STORAGETYPE = DESCRIPTOR.enum_types_by_name['StorageType']
StorageType = enum_type_wrapper.EnumTypeWrapper(_STORAGETYPE)
_ERROR = DESCRIPTOR.enum_types_by_name['Error']
Error = enum_type_wrapper.EnumTypeWrapper(_ERROR)
S3 = 0
SCP = 1
FTP = 2
LOCAL = 3
BOX = 4
DROPBOX = 5
GCS = 6
AZURE = 7
SWIFT = 8
ODATA = 9
NOT_FOUND = 0
NO_PERMISSION = 1
LIMIT_OVERFLOWED = 2


_STORAGETYPERESOLVEREQUEST = DESCRIPTOR.message_types_by_name['StorageTypeResolveRequest']
_STORAGETYPERESOLVERESPONSE = DESCRIPTOR.message_types_by_name['StorageTypeResolveResponse']
_SECRETFORSTORAGE = DESCRIPTOR.message_types_by_name['SecretForStorage']
_SECRETFORSTORAGEGETREQUEST = DESCRIPTOR.message_types_by_name['SecretForStorageGetRequest']
_SECRETFORSTORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['SecretForStorageDeleteRequest']
_SECRETFORSTORAGEDELETERESPONSE = DESCRIPTOR.message_types_by_name['SecretForStorageDeleteResponse']
_STORAGELISTENTRY = DESCRIPTOR.message_types_by_name['StorageListEntry']
_STORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['StorageListResponse']
_STORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['StorageListRequest']
StorageTypeResolveRequest = _reflection.GeneratedProtocolMessageType('StorageTypeResolveRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGETYPERESOLVEREQUEST,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.StorageTypeResolveRequest)
  })
_sym_db.RegisterMessage(StorageTypeResolveRequest)

StorageTypeResolveResponse = _reflection.GeneratedProtocolMessageType('StorageTypeResolveResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGETYPERESOLVERESPONSE,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.StorageTypeResolveResponse)
  })
_sym_db.RegisterMessage(StorageTypeResolveResponse)

SecretForStorage = _reflection.GeneratedProtocolMessageType('SecretForStorage', (_message.Message,), {
  'DESCRIPTOR' : _SECRETFORSTORAGE,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorage)
  })
_sym_db.RegisterMessage(SecretForStorage)

SecretForStorageGetRequest = _reflection.GeneratedProtocolMessageType('SecretForStorageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETFORSTORAGEGETREQUEST,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorageGetRequest)
  })
_sym_db.RegisterMessage(SecretForStorageGetRequest)

SecretForStorageDeleteRequest = _reflection.GeneratedProtocolMessageType('SecretForStorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETFORSTORAGEDELETEREQUEST,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorageDeleteRequest)
  })
_sym_db.RegisterMessage(SecretForStorageDeleteRequest)

SecretForStorageDeleteResponse = _reflection.GeneratedProtocolMessageType('SecretForStorageDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _SECRETFORSTORAGEDELETERESPONSE,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorageDeleteResponse)
  })
_sym_db.RegisterMessage(SecretForStorageDeleteResponse)

StorageListEntry = _reflection.GeneratedProtocolMessageType('StorageListEntry', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTENTRY,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.StorageListEntry)
  })
_sym_db.RegisterMessage(StorageListEntry)

StorageListResponse = _reflection.GeneratedProtocolMessageType('StorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTRESPONSE,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.StorageListResponse)
  })
_sym_db.RegisterMessage(StorageListResponse)

StorageListRequest = _reflection.GeneratedProtocolMessageType('StorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTREQUEST,
  '__module__' : 'common.StorageCommon_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.storage.common.StorageListRequest)
  })
_sym_db.RegisterMessage(StorageListRequest)

_STORAGECOMMONSERVICE = DESCRIPTOR.services_by_name['StorageCommonService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _STORAGETYPE._serialized_start=1072
  _STORAGETYPE._serialized_end=1186
  _ERROR._serialized_start=1188
  _ERROR._serialized_end=1251
  _STORAGETYPERESOLVEREQUEST._serialized_start=85
  _STORAGETYPERESOLVEREQUEST._serialized_end=131
  _STORAGETYPERESOLVERESPONSE._serialized_start=134
  _STORAGETYPERESOLVERESPONSE._serialized_end=368
  _SECRETFORSTORAGE._serialized_start=371
  _SECRETFORSTORAGE._serialized_end=592
  _SECRETFORSTORAGEGETREQUEST._serialized_start=594
  _SECRETFORSTORAGEGETREQUEST._serialized_end=641
  _SECRETFORSTORAGEDELETEREQUEST._serialized_start=643
  _SECRETFORSTORAGEDELETEREQUEST._serialized_end=693
  _SECRETFORSTORAGEDELETERESPONSE._serialized_start=695
  _SECRETFORSTORAGEDELETERESPONSE._serialized_end=743
  _STORAGELISTENTRY._serialized_start=746
  _STORAGELISTENTRY._serialized_end=893
  _STORAGELISTRESPONSE._serialized_start=895
  _STORAGELISTRESPONSE._serialized_end=1010
  _STORAGELISTREQUEST._serialized_start=1012
  _STORAGELISTREQUEST._serialized_end=1070
  _STORAGECOMMONSERVICE._serialized_start=1254
  _STORAGECOMMONSERVICE._serialized_end=2188
# @@protoc_insertion_point(module_scope)
