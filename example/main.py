import grpc
from kessel.inventory.v1beta2 import (
    resource_pb2,
    reporter_data_pb2,
    resource_service_pb2_grpc,
    resource_service_pb2
)
from google.protobuf import struct_pb2


def run():
    channel = grpc.insecure_channel("localhost:9000")
    stub = resource_service_pb2_grpc.KesselResourceServiceStub(channel)

    resource_data_struct = struct_pb2.Struct()

    common_resource_data_struct = struct_pb2.Struct()
    common_resource_data_struct.update({
        "workspace_id": "123"
    })

    resource = resource_pb2.Resource(
        resource_type="host",
        reporter_data=reporter_data_pb2.ReporterData(
            reporter_type="HBI",
            reporter_instance_id="user@example.com",
            reporter_version="0.1",
            local_resource_id="25",
            api_href="www.example.com",
            console_href="www.rhel.example.com",
            resource_data=resource_data_struct
        ),
        common_resource_data=common_resource_data_struct
    )

    # Wrap in ReportResourceRequest
    request = resource_service_pb2.ReportResourceRequest(
        resource=resource
    )

    delReq = resource_service_pb2.DeleteResourceRequest(
        reporter_type="HBI",
        local_resource_id="25",

    )

    # Send gRPC request
    try:
        response = stub.ReportResource(request)
        print("Resource reported successfully")
        print(response)

        response = stub.DeleteResource(delReq)
        print("Resource deleted successfully")
        print(response)
    except grpc.RpcError as e:
        print("gRPC error occurred:")
        print(f"Code: {e.code()}")
        print(f"Details: {e.details()}")


if __name__ == "__main__":
    run()
