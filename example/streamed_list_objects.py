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
    channel = grpc.insecure_channel("172.19.0.8:9081")
    stub = inventory_service_pb2_grpc.KesselInventoryServiceStub(channel)

    object_type = representation_type_pb2.RepresentationType(
        resource_type="host",
        reporter_type="hbi",
    )

    resource_ref = resource_reference_pb2.ResourceReference(
        resource_type="host",
        resource_id="dd1b73b9-3e33-4264-968c-e3ce55b9afec",
        reporter=reporter_reference_pb2.ReporterReference(
            type="hbi",
            instance_id="3088be62-1c60-4884-b133-9200542d0b3f",
        ),
    )

    subject = subject_reference_pb2.SubjectReference(
        resource=resource_ref,
    )

    request = streamed_list_objects_request_pb2.StreamedListObjectsRequest(
        object_type=object_type,
        relation="view",
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
