# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from airavata_mft_sdk.gcs import GCSStorage_pb2 as gcs_dot_GCSStorage__pb2
from airavata_mft_sdk.google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class GCSStorageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.listGCSStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/listGCSStorage',
                request_serializer=gcs_dot_GCSStorage__pb2.GCSStorageListRequest.SerializeToString,
                response_deserializer=gcs_dot_GCSStorage__pb2.GCSStorageListResponse.FromString,
                )
        self.getGCSStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/getGCSStorage',
                request_serializer=gcs_dot_GCSStorage__pb2.GCSStorageGetRequest.SerializeToString,
                response_deserializer=gcs_dot_GCSStorage__pb2.GCSStorage.FromString,
                )
        self.createGCSStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/createGCSStorage',
                request_serializer=gcs_dot_GCSStorage__pb2.GCSStorageCreateRequest.SerializeToString,
                response_deserializer=gcs_dot_GCSStorage__pb2.GCSStorage.FromString,
                )
        self.updateGCSStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/updateGCSStorage',
                request_serializer=gcs_dot_GCSStorage__pb2.GCSStorageUpdateRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.deleteGCSStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/deleteGCSStorage',
                request_serializer=gcs_dot_GCSStorage__pb2.GCSStorageDeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class GCSStorageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def listGCSStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getGCSStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createGCSStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateGCSStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteGCSStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GCSStorageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'listGCSStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.listGCSStorage,
                    request_deserializer=gcs_dot_GCSStorage__pb2.GCSStorageListRequest.FromString,
                    response_serializer=gcs_dot_GCSStorage__pb2.GCSStorageListResponse.SerializeToString,
            ),
            'getGCSStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.getGCSStorage,
                    request_deserializer=gcs_dot_GCSStorage__pb2.GCSStorageGetRequest.FromString,
                    response_serializer=gcs_dot_GCSStorage__pb2.GCSStorage.SerializeToString,
            ),
            'createGCSStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.createGCSStorage,
                    request_deserializer=gcs_dot_GCSStorage__pb2.GCSStorageCreateRequest.FromString,
                    response_serializer=gcs_dot_GCSStorage__pb2.GCSStorage.SerializeToString,
            ),
            'updateGCSStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.updateGCSStorage,
                    request_deserializer=gcs_dot_GCSStorage__pb2.GCSStorageUpdateRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'deleteGCSStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteGCSStorage,
                    request_deserializer=gcs_dot_GCSStorage__pb2.GCSStorageDeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.airavata.mft.resource.service.gcs.GCSStorageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GCSStorageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def listGCSStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/listGCSStorage',
            gcs_dot_GCSStorage__pb2.GCSStorageListRequest.SerializeToString,
            gcs_dot_GCSStorage__pb2.GCSStorageListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getGCSStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/getGCSStorage',
            gcs_dot_GCSStorage__pb2.GCSStorageGetRequest.SerializeToString,
            gcs_dot_GCSStorage__pb2.GCSStorage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createGCSStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/createGCSStorage',
            gcs_dot_GCSStorage__pb2.GCSStorageCreateRequest.SerializeToString,
            gcs_dot_GCSStorage__pb2.GCSStorage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateGCSStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/updateGCSStorage',
            gcs_dot_GCSStorage__pb2.GCSStorageUpdateRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteGCSStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.gcs.GCSStorageService/deleteGCSStorage',
            gcs_dot_GCSStorage__pb2.GCSStorageDeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
