import grpc
from src.kessel.inventory.v1beta2 import (
    inventory_service_pb2_grpc,
    streamed_list_objects_request_pb2,
    representation_type_pb2,
    subject_reference_pb2,
    resource_reference_pb2,
    reporter_reference_pb2
)

def run():
    channel = grpc.insecure_channel("localhost:9000")
    stub = inventory_service_pb2_grpc.KesselInventoryServiceStub(channel)

    object_type = representation_type_pb2.RepresentationType(
        resource_type="host",
        reporter_type="hbi",
    )

    resource_ref = resource_reference_pb2.ResourceReference(
        resource_type="host",
        resource_id="12345",
        reporter=reporter_reference_pb2.ReporterReference(
            type="hbi",
            instance_id="some-reporter-id",
        ),
    )

    subject = subject_reference_pb2.SubjectReference(
        resource=resource_ref,
    )

    request = streamed_list_objects_request_pb2.StreamedListObjectsRequest(
        object_type=object_type,
        relation="member",
        subject=subject,
    )

    try:
        responses = stub.StreamedListObjects(request)
        print("Received streamed responses:")
        for response in responses:
            print(response)

    except grpc.RpcError as e:
        print("gRPC error occurred:")
        print(f"Code: {e.code()}")
        print(f"Details: {e.details()}")

if __name__ == "__main__":
    run()
