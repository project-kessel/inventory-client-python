# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from kessel.inventory.v1beta1 import hosts_service_pb2 as kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in kessel/inventory/v1beta1/hosts_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class HostsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRHELHost = channel.unary_unary(
                '/api.kessel.inventory.v1beta1.HostsService/CreateRHELHost',
                request_serializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.CreateRHELHostRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.CreateRHELHostResponse.FromString,
                _registered_method=True)
        self.UpdateRHELHost = channel.unary_unary(
                '/api.kessel.inventory.v1beta1.HostsService/UpdateRHELHost',
                request_serializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.UpdateRHELHostRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.UpdateRHELHostResponse.FromString,
                _registered_method=True)
        self.DeleteRHELHost = channel.unary_unary(
                '/api.kessel.inventory.v1beta1.HostsService/DeleteRHELHost',
                request_serializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.DeleteRHELHostRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.DeleteRHELHostResponse.FromString,
                _registered_method=True)


class HostsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRHELHost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRHELHost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRHELHost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HostsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRHELHost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRHELHost,
                    request_deserializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.CreateRHELHostRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.CreateRHELHostResponse.SerializeToString,
            ),
            'UpdateRHELHost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRHELHost,
                    request_deserializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.UpdateRHELHostRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.UpdateRHELHostResponse.SerializeToString,
            ),
            'DeleteRHELHost': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRHELHost,
                    request_deserializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.DeleteRHELHostRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.DeleteRHELHostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.kessel.inventory.v1beta1.HostsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('api.kessel.inventory.v1beta1.HostsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HostsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRHELHost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.kessel.inventory.v1beta1.HostsService/CreateRHELHost',
            kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.CreateRHELHostRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.CreateRHELHostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateRHELHost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.kessel.inventory.v1beta1.HostsService/UpdateRHELHost',
            kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.UpdateRHELHostRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.UpdateRHELHostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteRHELHost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.kessel.inventory.v1beta1.HostsService/DeleteRHELHost',
            kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.DeleteRHELHostRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta1_dot_hosts__service__pb2.DeleteRHELHostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)