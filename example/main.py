import grpc
from kessel.inventory.v1beta2 import (
    resource_pb2,
    resource_service_pb2_grpc,
    resource_representations_pb2,
    representation_metadata_pb2,
    report_resource_request_pb2,
    delete_resource_request_pb2,
    check_request_pb2,
    check_service_pb2_grpc,
    allowed_pb2,
    subject_reference_pb2,
    resource_reference_pb2,
    reporter_reference_pb2,
    check_for_update_request_pb2
)
from google.protobuf import struct_pb2


def runResourceLifecycle():
    channel = grpc.insecure_channel("localhost:9000")
    stub = resource_service_pb2_grpc.KesselResourceServiceStub(channel)

    common_struct = struct_pb2.Struct()
    common_struct.update({
        "workspace_id": "6eb10953-4ec9-4feb-838f-ba43a60880bf"
    })

    reporter_struct = struct_pb2.Struct()
    reporter_struct.update({
        "satellite_id": "ca234d8f-9861-4659-a033-e80460b2801c",
        "sub_manager_id": "e9b7d65f-3f81-4c26-b86c-2db663376eed",
        "insights_inventory_id": "c4b9b5e7-a82a-467a-b382-024a2f18c129",
        "ansible_host": "host-1"
    })

    metadata = representation_metadata_pb2.RepresentationMetadata(
        local_resource_id="854589f0-3be7-4cad-8bcd-45e18f33cb81",
        api_href="https://apiHref.com/",
        console_href="https://www.consoleHref.com/",
        reporter_version="0.2.11"
    )

    representations = resource_representations_pb2.ResourceRepresentations(
        metadata=metadata,
        common=common_struct,
        reporter=reporter_struct
    )

    resource = resource_pb2.Resource(
        type="host",
        reporter_type="HBI",
        reporter_instance_id="0a2a430e-1ad9-4304-8e75-cc6fd3b5441a",
        representations=representations
    )

    # Wrap in ReportResourceRequest
    request = report_resource_request_pb2.ReportResourceRequest(
        resource=resource
    )

    delReq = delete_resource_request_pb2.DeleteResourceRequest(
        reporter_type="HBI",
        local_resource_id="854589f0-3be7-4cad-8bcd-45e18f33cb81",

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


def runAuthLifecycle():

    channel = grpc.insecure_channel("localhost:9000")
    stub = check_service_pb2_grpc.KesselCheckServiceStub(channel)

    # Prepare the subject
    subject = subject_reference_pb2.SubjectReference(
        resource=resource_reference_pb2.ResourceReference(
            resource_id="bob",
            resource_type="principal",
            reporter=reporter_reference_pb2.ReporterReference(
                type="rbac"
            )
        )
    )

    # Prepare the parent object
    parent = resource_reference_pb2.ResourceReference(
        resource_id="bob_club",
        resource_type="group",
        reporter=reporter_reference_pb2.ReporterReference(
            type="rbac"
        )
    )

    # 1. Perform /authz/check
    check_request = check_request_pb2.CheckRequest(
        subject=subject,
        relation="member",
        object=parent,
    )

    try:
        check_response = stub.Check(check_request)
        print("Check response received successfully")
        print(check_response)
    except grpc.RpcError as e:
        print("gRPC error occurred during Check:")
        print(f"Code: {e.code()}")
        print(f"Details: {e.details()}")
        raise

    # 2. Perform /authz/checkforupdate
    checkforupdate_request = check_for_update_request_pb2.CheckForUpdateRequest(
        subject=subject,
        relation="member",
        object=parent,
    )

    try:
        checkforupdate_response = stub.CheckForUpdate(checkforupdate_request)
        print("CheckForUpdate response received successfully")
        print(checkforupdate_response)
    except grpc.RpcError as e:
        print("gRPC error occurred during CheckForUpdate:")
        print(f"Code: {e.code()}")
        print(f"Details: {e.details()}")



if __name__ == "__main__":
    #runResourceLifecycle()
    runAuthLifecycle()
