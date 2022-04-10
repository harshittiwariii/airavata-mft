# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MFTTransferApi.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from airavata_mft_sdk.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from airavata_mft_sdk.google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import airavata_mft_sdk.CredCommon_pb2 as CredCommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14MFTTransferApi.proto\x12#org.apache.airavata.mft.api.service\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x10\x43redCommon.proto\"\x9b\x01\n\x10\x43\x61llbackEndpoint\x12P\n\x04type\x18\x01 \x01(\x0e\x32\x42.org.apache.airavata.mft.api.service.CallbackEndpoint.CallbackType\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\"#\n\x0c\x43\x61llbackType\x12\x08\n\x04HTTP\x10\x00\x12\t\n\x05KAFKA\x10\x01\"\xbc\x04\n\x12TransferApiRequest\x12\x18\n\x10sourceResourceId\x18\x01 \x01(\t\x12\x1f\n\x17sourceChildResourcePath\x18\x02 \x01(\t\x12\x12\n\nsourceType\x18\x03 \x01(\t\x12\x13\n\x0bsourceToken\x18\x04 \x01(\t\x12\x1d\n\x15\x64\x65stinationResourceId\x18\x05 \x01(\t\x12$\n\x1c\x64\x65stinationChildResourcePath\x18\x06 \x01(\t\x12\x17\n\x0f\x64\x65stinationType\x18\x07 \x01(\t\x12\x18\n\x10\x64\x65stinationToken\x18\x08 \x01(\t\x12\x18\n\x10\x61\x66\x66inityTransfer\x18\t \x01(\x08\x12_\n\x0ctargetAgents\x18\n \x03(\x0b\x32I.org.apache.airavata.mft.api.service.TransferApiRequest.TargetAgentsEntry\x12H\n\x15mftAuthorizationToken\x18\x0b \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\x12P\n\x11\x63\x61llbackEndpoints\x18\x0c \x03(\x0b\x32\x35.org.apache.airavata.mft.api.service.CallbackEndpoint\x1a\x33\n\x11TargetAgentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\")\n\x13TransferApiResponse\x12\x12\n\ntransferId\x18\x01 \x01(\t\"\xed\x01\n\x14HttpUploadApiRequest\x12\x1d\n\x15\x64\x65stinationResourceId\x18\x01 \x01(\t\x12$\n\x1c\x64\x65stinationResourceChildPath\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stinationToken\x18\x03 \x01(\t\x12\x17\n\x0f\x64\x65stinationType\x18\x04 \x01(\t\x12\x13\n\x0btargetAgent\x18\x05 \x01(\t\x12H\n\x15mftAuthorizationToken\x18\x06 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"9\n\x15HttpUploadApiResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0btargetAgent\x18\x02 \x01(\t\"\xdb\x01\n\x16HttpDownloadApiRequest\x12\x18\n\x10sourceResourceId\x18\x01 \x01(\t\x12\x1f\n\x17sourceResourceChildPath\x18\x02 \x01(\t\x12\x13\n\x0bsourceToken\x18\x03 \x01(\t\x12\x12\n\nsourceType\x18\x04 \x01(\t\x12\x13\n\x0btargetAgent\x18\x05 \x01(\t\x12H\n\x15mftAuthorizationToken\x18\x06 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\";\n\x17HttpDownloadApiResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0btargetAgent\x18\x02 \x01(\t\"w\n\x17TransferStateApiRequest\x12\x12\n\ntransferId\x18\x01 \x01(\t\x12H\n\x15mftAuthorizationToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"j\n\x18TransferStateApiResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x16\n\x0eupdateTimeMils\x18\x02 \x01(\x03\x12\x12\n\npercentage\x18\x03 \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"\xff\x01\n\x1bResourceAvailabilityRequest\x12\x12\n\nresourceId\x18\x01 \x01(\t\x12\x19\n\x11\x63hildResourcePath\x18\x02 \x01(\t\x12\x14\n\x0cresourceType\x18\x03 \x01(\t\x12\x15\n\rresourceToken\x18\x04 \x01(\t\x12\x17\n\x0fresourceBackend\x18\x05 \x01(\t\x12!\n\x19resourceCredentialBackend\x18\x06 \x01(\t\x12H\n\x15mftAuthorizationToken\x18\x07 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"1\n\x1cResourceAvailabilityResponse\x12\x11\n\tavailable\x18\x01 \x01(\x08\"\xc7\x01\n\x14\x46ileMetadataResponse\x12\x14\n\x0c\x66riendlyName\x18\x01 \x01(\t\x12\x14\n\x0cresourceSize\x18\x02 \x01(\x03\x12\x13\n\x0b\x63reatedTime\x18\x03 \x01(\x03\x12\x12\n\nupdateTime\x18\x04 \x01(\x03\x12\x0e\n\x06md5sum\x18\x05 \x01(\t\x12\x14\n\x0cresourcePath\x18\x06 \x01(\t\x12\x18\n\x10parentResourceId\x18\x07 \x01(\t\x12\x1a\n\x12parentResourceType\x18\x08 \x01(\t\"\xde\x02\n\x19\x44irectoryMetadataResponse\x12\x14\n\x0c\x66riendlyName\x18\x01 \x01(\t\x12\x13\n\x0b\x63reatedTime\x18\x02 \x01(\x03\x12\x12\n\nupdateTime\x18\x03 \x01(\x03\x12\x14\n\x0cresourcePath\x18\x04 \x01(\t\x12\x18\n\x10parentResourceId\x18\x05 \x01(\t\x12\x1a\n\x12parentResourceType\x18\x06 \x01(\t\x12S\n\x0b\x64irectories\x18\x07 \x03(\x0b\x32>.org.apache.airavata.mft.api.service.DirectoryMetadataResponse\x12H\n\x05\x66iles\x18\x08 \x03(\x0b\x32\x39.org.apache.airavata.mft.api.service.FileMetadataResponse\x12\x17\n\x0flazyInitialized\x18\t \x01(\x08\"\xaa\x02\n\x1c\x46\x65tchResourceMetadataRequest\x12\x12\n\nresourceId\x18\x01 \x01(\t\x12\x19\n\x11\x63hildResourcePath\x18\x02 \x01(\t\x12\x14\n\x0cresourceType\x18\x03 \x01(\t\x12\x15\n\rresourceToken\x18\x04 \x01(\t\x12\x17\n\x0fresourceBackend\x18\x05 \x01(\t\x12!\n\x19resourceCredentialBackend\x18\x06 \x01(\t\x12\x15\n\rtargetAgentId\x18\x07 \x01(\t\x12\x11\n\tchildPath\x18\x08 \x01(\t\x12H\n\x15mftAuthorizationToken\x18\t \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken2\xba\x0b\n\x12MFTTransferService\x12\x9f\x01\n\x0esubmitTransfer\x12\x37.org.apache.airavata.mft.api.service.TransferApiRequest\x1a\x38.org.apache.airavata.mft.api.service.TransferApiResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x12/v1.0/api/transfer\x12\xa8\x01\n\x10submitHttpUpload\x12\x39.org.apache.airavata.mft.api.service.HttpUploadApiRequest\x1a:.org.apache.airavata.mft.api.service.HttpUploadApiResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/v1.0/api/http-upload\x12\xb0\x01\n\x12submitHttpDownload\x12;.org.apache.airavata.mft.api.service.HttpDownloadApiRequest\x1a<.org.apache.airavata.mft.api.service.HttpDownloadApiResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/v1.0/api/http-download\x12\xb5\x01\n\x11getTransferStates\x12<.org.apache.airavata.mft.api.service.TransferStateApiRequest\x1a=.org.apache.airavata.mft.api.service.TransferStateApiResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1.0/api/transfer/states0\x01\x12\xb1\x01\n\x10getTransferState\x12<.org.apache.airavata.mft.api.service.TransferStateApiRequest\x1a=.org.apache.airavata.mft.api.service.TransferStateApiResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1.0/api/transfer/state\x12\xa0\x01\n\x17getResourceAvailability\x12@.org.apache.airavata.mft.api.service.ResourceAvailabilityRequest\x1a\x41.org.apache.airavata.mft.api.service.ResourceAvailabilityResponse\"\x00\x12\xc1\x01\n\x17getFileResourceMetadata\x12\x41.org.apache.airavata.mft.api.service.FetchResourceMetadataRequest\x1a\x39.org.apache.airavata.mft.api.service.FileMetadataResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1.0/api/resource/metadata/file\x12\xd0\x01\n\x1cgetDirectoryResourceMetadata\x12\x41.org.apache.airavata.mft.api.service.FetchResourceMetadataRequest\x1a>.org.apache.airavata.mft.api.service.DirectoryMetadataResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1.0/api/resource/metadata/directoryB\x02P\x01\x62\x06proto3')



_CALLBACKENDPOINT = DESCRIPTOR.message_types_by_name['CallbackEndpoint']
_TRANSFERAPIREQUEST = DESCRIPTOR.message_types_by_name['TransferApiRequest']
_TRANSFERAPIREQUEST_TARGETAGENTSENTRY = _TRANSFERAPIREQUEST.nested_types_by_name['TargetAgentsEntry']
_TRANSFERAPIRESPONSE = DESCRIPTOR.message_types_by_name['TransferApiResponse']
_HTTPUPLOADAPIREQUEST = DESCRIPTOR.message_types_by_name['HttpUploadApiRequest']
_HTTPUPLOADAPIRESPONSE = DESCRIPTOR.message_types_by_name['HttpUploadApiResponse']
_HTTPDOWNLOADAPIREQUEST = DESCRIPTOR.message_types_by_name['HttpDownloadApiRequest']
_HTTPDOWNLOADAPIRESPONSE = DESCRIPTOR.message_types_by_name['HttpDownloadApiResponse']
_TRANSFERSTATEAPIREQUEST = DESCRIPTOR.message_types_by_name['TransferStateApiRequest']
_TRANSFERSTATEAPIRESPONSE = DESCRIPTOR.message_types_by_name['TransferStateApiResponse']
_RESOURCEAVAILABILITYREQUEST = DESCRIPTOR.message_types_by_name['ResourceAvailabilityRequest']
_RESOURCEAVAILABILITYRESPONSE = DESCRIPTOR.message_types_by_name['ResourceAvailabilityResponse']
_FILEMETADATARESPONSE = DESCRIPTOR.message_types_by_name['FileMetadataResponse']
_DIRECTORYMETADATARESPONSE = DESCRIPTOR.message_types_by_name['DirectoryMetadataResponse']
_FETCHRESOURCEMETADATAREQUEST = DESCRIPTOR.message_types_by_name['FetchResourceMetadataRequest']
_CALLBACKENDPOINT_CALLBACKTYPE = _CALLBACKENDPOINT.enum_types_by_name['CallbackType']
CallbackEndpoint = _reflection.GeneratedProtocolMessageType('CallbackEndpoint', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKENDPOINT,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.CallbackEndpoint)
  })
_sym_db.RegisterMessage(CallbackEndpoint)

TransferApiRequest = _reflection.GeneratedProtocolMessageType('TransferApiRequest', (_message.Message,), {

  'TargetAgentsEntry' : _reflection.GeneratedProtocolMessageType('TargetAgentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRANSFERAPIREQUEST_TARGETAGENTSENTRY,
    '__module__' : 'MFTTransferApi_pb2'
    # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.TransferApiRequest.TargetAgentsEntry)
    })
  ,
  'DESCRIPTOR' : _TRANSFERAPIREQUEST,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.TransferApiRequest)
  })
_sym_db.RegisterMessage(TransferApiRequest)
_sym_db.RegisterMessage(TransferApiRequest.TargetAgentsEntry)

TransferApiResponse = _reflection.GeneratedProtocolMessageType('TransferApiResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERAPIRESPONSE,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.TransferApiResponse)
  })
_sym_db.RegisterMessage(TransferApiResponse)

HttpUploadApiRequest = _reflection.GeneratedProtocolMessageType('HttpUploadApiRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPUPLOADAPIREQUEST,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.HttpUploadApiRequest)
  })
_sym_db.RegisterMessage(HttpUploadApiRequest)

HttpUploadApiResponse = _reflection.GeneratedProtocolMessageType('HttpUploadApiResponse', (_message.Message,), {
  'DESCRIPTOR' : _HTTPUPLOADAPIRESPONSE,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.HttpUploadApiResponse)
  })
_sym_db.RegisterMessage(HttpUploadApiResponse)

HttpDownloadApiRequest = _reflection.GeneratedProtocolMessageType('HttpDownloadApiRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPDOWNLOADAPIREQUEST,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.HttpDownloadApiRequest)
  })
_sym_db.RegisterMessage(HttpDownloadApiRequest)

HttpDownloadApiResponse = _reflection.GeneratedProtocolMessageType('HttpDownloadApiResponse', (_message.Message,), {
  'DESCRIPTOR' : _HTTPDOWNLOADAPIRESPONSE,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.HttpDownloadApiResponse)
  })
_sym_db.RegisterMessage(HttpDownloadApiResponse)

TransferStateApiRequest = _reflection.GeneratedProtocolMessageType('TransferStateApiRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERSTATEAPIREQUEST,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.TransferStateApiRequest)
  })
_sym_db.RegisterMessage(TransferStateApiRequest)

TransferStateApiResponse = _reflection.GeneratedProtocolMessageType('TransferStateApiResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERSTATEAPIRESPONSE,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.TransferStateApiResponse)
  })
_sym_db.RegisterMessage(TransferStateApiResponse)

ResourceAvailabilityRequest = _reflection.GeneratedProtocolMessageType('ResourceAvailabilityRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEAVAILABILITYREQUEST,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.ResourceAvailabilityRequest)
  })
_sym_db.RegisterMessage(ResourceAvailabilityRequest)

ResourceAvailabilityResponse = _reflection.GeneratedProtocolMessageType('ResourceAvailabilityResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEAVAILABILITYRESPONSE,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.ResourceAvailabilityResponse)
  })
_sym_db.RegisterMessage(ResourceAvailabilityResponse)

FileMetadataResponse = _reflection.GeneratedProtocolMessageType('FileMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _FILEMETADATARESPONSE,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.FileMetadataResponse)
  })
_sym_db.RegisterMessage(FileMetadataResponse)

DirectoryMetadataResponse = _reflection.GeneratedProtocolMessageType('DirectoryMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTORYMETADATARESPONSE,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.DirectoryMetadataResponse)
  })
_sym_db.RegisterMessage(DirectoryMetadataResponse)

FetchResourceMetadataRequest = _reflection.GeneratedProtocolMessageType('FetchResourceMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHRESOURCEMETADATAREQUEST,
  '__module__' : 'MFTTransferApi_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.api.service.FetchResourceMetadataRequest)
  })
_sym_db.RegisterMessage(FetchResourceMetadataRequest)

_MFTTRANSFERSERVICE = DESCRIPTOR.services_by_name['MFTTransferService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _TRANSFERAPIREQUEST_TARGETAGENTSENTRY._options = None
  _TRANSFERAPIREQUEST_TARGETAGENTSENTRY._serialized_options = b'8\001'
  _MFTTRANSFERSERVICE.methods_by_name['submitTransfer']._options = None
  _MFTTRANSFERSERVICE.methods_by_name['submitTransfer']._serialized_options = b'\202\323\344\223\002\024\"\022/v1.0/api/transfer'
  _MFTTRANSFERSERVICE.methods_by_name['submitHttpUpload']._options = None
  _MFTTRANSFERSERVICE.methods_by_name['submitHttpUpload']._serialized_options = b'\202\323\344\223\002\027\"\025/v1.0/api/http-upload'
  _MFTTRANSFERSERVICE.methods_by_name['submitHttpDownload']._options = None
  _MFTTRANSFERSERVICE.methods_by_name['submitHttpDownload']._serialized_options = b'\202\323\344\223\002\031\"\027/v1.0/api/http-download'
  _MFTTRANSFERSERVICE.methods_by_name['getTransferStates']._options = None
  _MFTTRANSFERSERVICE.methods_by_name['getTransferStates']._serialized_options = b'\202\323\344\223\002\033\022\031/v1.0/api/transfer/states'
  _MFTTRANSFERSERVICE.methods_by_name['getTransferState']._options = None
  _MFTTRANSFERSERVICE.methods_by_name['getTransferState']._serialized_options = b'\202\323\344\223\002\032\022\030/v1.0/api/transfer/state'
  _MFTTRANSFERSERVICE.methods_by_name['getFileResourceMetadata']._options = None
  _MFTTRANSFERSERVICE.methods_by_name['getFileResourceMetadata']._serialized_options = b'\202\323\344\223\002\"\022 /v1.0/api/resource/metadata/file'
  _MFTTRANSFERSERVICE.methods_by_name['getDirectoryResourceMetadata']._options = None
  _MFTTRANSFERSERVICE.methods_by_name['getDirectoryResourceMetadata']._serialized_options = b'\202\323\344\223\002\'\022%/v1.0/api/resource/metadata/directory'
  _CALLBACKENDPOINT._serialized_start=139
  _CALLBACKENDPOINT._serialized_end=294
  _CALLBACKENDPOINT_CALLBACKTYPE._serialized_start=259
  _CALLBACKENDPOINT_CALLBACKTYPE._serialized_end=294
  _TRANSFERAPIREQUEST._serialized_start=297
  _TRANSFERAPIREQUEST._serialized_end=869
  _TRANSFERAPIREQUEST_TARGETAGENTSENTRY._serialized_start=818
  _TRANSFERAPIREQUEST_TARGETAGENTSENTRY._serialized_end=869
  _TRANSFERAPIRESPONSE._serialized_start=871
  _TRANSFERAPIRESPONSE._serialized_end=912
  _HTTPUPLOADAPIREQUEST._serialized_start=915
  _HTTPUPLOADAPIREQUEST._serialized_end=1152
  _HTTPUPLOADAPIRESPONSE._serialized_start=1154
  _HTTPUPLOADAPIRESPONSE._serialized_end=1211
  _HTTPDOWNLOADAPIREQUEST._serialized_start=1214
  _HTTPDOWNLOADAPIREQUEST._serialized_end=1433
  _HTTPDOWNLOADAPIRESPONSE._serialized_start=1435
  _HTTPDOWNLOADAPIRESPONSE._serialized_end=1494
  _TRANSFERSTATEAPIREQUEST._serialized_start=1496
  _TRANSFERSTATEAPIREQUEST._serialized_end=1615
  _TRANSFERSTATEAPIRESPONSE._serialized_start=1617
  _TRANSFERSTATEAPIRESPONSE._serialized_end=1723
  _RESOURCEAVAILABILITYREQUEST._serialized_start=1726
  _RESOURCEAVAILABILITYREQUEST._serialized_end=1981
  _RESOURCEAVAILABILITYRESPONSE._serialized_start=1983
  _RESOURCEAVAILABILITYRESPONSE._serialized_end=2032
  _FILEMETADATARESPONSE._serialized_start=2035
  _FILEMETADATARESPONSE._serialized_end=2234
  _DIRECTORYMETADATARESPONSE._serialized_start=2237
  _DIRECTORYMETADATARESPONSE._serialized_end=2587
  _FETCHRESOURCEMETADATAREQUEST._serialized_start=2590
  _FETCHRESOURCEMETADATAREQUEST._serialized_end=2888
  _MFTTRANSFERSERVICE._serialized_start=2891
  _MFTTRANSFERSERVICE._serialized_end=4357
# @@protoc_insertion_point(module_scope)
