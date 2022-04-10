# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import airavata_mft_sdk.MFTTransferApi_pb2 as MFTTransferApi__pb2


class MFTTransferServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.submitTransfer = channel.unary_unary(
                '/org.apache.airavata.mft.api.service.MFTTransferService/submitTransfer',
                request_serializer=MFTTransferApi__pb2.TransferApiRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.TransferApiResponse.FromString,
                )
        self.submitHttpUpload = channel.unary_unary(
                '/org.apache.airavata.mft.api.service.MFTTransferService/submitHttpUpload',
                request_serializer=MFTTransferApi__pb2.HttpUploadApiRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.HttpUploadApiResponse.FromString,
                )
        self.submitHttpDownload = channel.unary_unary(
                '/org.apache.airavata.mft.api.service.MFTTransferService/submitHttpDownload',
                request_serializer=MFTTransferApi__pb2.HttpDownloadApiRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.HttpDownloadApiResponse.FromString,
                )
        self.getTransferStates = channel.unary_stream(
                '/org.apache.airavata.mft.api.service.MFTTransferService/getTransferStates',
                request_serializer=MFTTransferApi__pb2.TransferStateApiRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.TransferStateApiResponse.FromString,
                )
        self.getTransferState = channel.unary_unary(
                '/org.apache.airavata.mft.api.service.MFTTransferService/getTransferState',
                request_serializer=MFTTransferApi__pb2.TransferStateApiRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.TransferStateApiResponse.FromString,
                )
        self.getResourceAvailability = channel.unary_unary(
                '/org.apache.airavata.mft.api.service.MFTTransferService/getResourceAvailability',
                request_serializer=MFTTransferApi__pb2.ResourceAvailabilityRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.ResourceAvailabilityResponse.FromString,
                )
        self.getFileResourceMetadata = channel.unary_unary(
                '/org.apache.airavata.mft.api.service.MFTTransferService/getFileResourceMetadata',
                request_serializer=MFTTransferApi__pb2.FetchResourceMetadataRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.FileMetadataResponse.FromString,
                )
        self.getDirectoryResourceMetadata = channel.unary_unary(
                '/org.apache.airavata.mft.api.service.MFTTransferService/getDirectoryResourceMetadata',
                request_serializer=MFTTransferApi__pb2.FetchResourceMetadataRequest.SerializeToString,
                response_deserializer=MFTTransferApi__pb2.DirectoryMetadataResponse.FromString,
                )


class MFTTransferServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def submitTransfer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def submitHttpUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def submitHttpDownload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTransferStates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTransferState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getResourceAvailability(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getFileResourceMetadata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDirectoryResourceMetadata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MFTTransferServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'submitTransfer': grpc.unary_unary_rpc_method_handler(
                    servicer.submitTransfer,
                    request_deserializer=MFTTransferApi__pb2.TransferApiRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.TransferApiResponse.SerializeToString,
            ),
            'submitHttpUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.submitHttpUpload,
                    request_deserializer=MFTTransferApi__pb2.HttpUploadApiRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.HttpUploadApiResponse.SerializeToString,
            ),
            'submitHttpDownload': grpc.unary_unary_rpc_method_handler(
                    servicer.submitHttpDownload,
                    request_deserializer=MFTTransferApi__pb2.HttpDownloadApiRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.HttpDownloadApiResponse.SerializeToString,
            ),
            'getTransferStates': grpc.unary_stream_rpc_method_handler(
                    servicer.getTransferStates,
                    request_deserializer=MFTTransferApi__pb2.TransferStateApiRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.TransferStateApiResponse.SerializeToString,
            ),
            'getTransferState': grpc.unary_unary_rpc_method_handler(
                    servicer.getTransferState,
                    request_deserializer=MFTTransferApi__pb2.TransferStateApiRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.TransferStateApiResponse.SerializeToString,
            ),
            'getResourceAvailability': grpc.unary_unary_rpc_method_handler(
                    servicer.getResourceAvailability,
                    request_deserializer=MFTTransferApi__pb2.ResourceAvailabilityRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.ResourceAvailabilityResponse.SerializeToString,
            ),
            'getFileResourceMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.getFileResourceMetadata,
                    request_deserializer=MFTTransferApi__pb2.FetchResourceMetadataRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.FileMetadataResponse.SerializeToString,
            ),
            'getDirectoryResourceMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.getDirectoryResourceMetadata,
                    request_deserializer=MFTTransferApi__pb2.FetchResourceMetadataRequest.FromString,
                    response_serializer=MFTTransferApi__pb2.DirectoryMetadataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.airavata.mft.api.service.MFTTransferService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MFTTransferService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def submitTransfer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/submitTransfer',
            MFTTransferApi__pb2.TransferApiRequest.SerializeToString,
            MFTTransferApi__pb2.TransferApiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def submitHttpUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/submitHttpUpload',
            MFTTransferApi__pb2.HttpUploadApiRequest.SerializeToString,
            MFTTransferApi__pb2.HttpUploadApiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def submitHttpDownload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/submitHttpDownload',
            MFTTransferApi__pb2.HttpDownloadApiRequest.SerializeToString,
            MFTTransferApi__pb2.HttpDownloadApiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTransferStates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/getTransferStates',
            MFTTransferApi__pb2.TransferStateApiRequest.SerializeToString,
            MFTTransferApi__pb2.TransferStateApiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTransferState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/getTransferState',
            MFTTransferApi__pb2.TransferStateApiRequest.SerializeToString,
            MFTTransferApi__pb2.TransferStateApiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getResourceAvailability(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/getResourceAvailability',
            MFTTransferApi__pb2.ResourceAvailabilityRequest.SerializeToString,
            MFTTransferApi__pb2.ResourceAvailabilityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getFileResourceMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/getFileResourceMetadata',
            MFTTransferApi__pb2.FetchResourceMetadataRequest.SerializeToString,
            MFTTransferApi__pb2.FileMetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDirectoryResourceMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.api.service.MFTTransferService/getDirectoryResourceMetadata',
            MFTTransferApi__pb2.FetchResourceMetadataRequest.SerializeToString,
            MFTTransferApi__pb2.DirectoryMetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
