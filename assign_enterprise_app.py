import argparse
import json

from graph_client import GraphClient, parse_object_id


DEFAULT_ACCESS_ROLE_ID = "00000000-0000-0000-0000-000000000000"


def get_main() -> None:
    parser = argparse.ArgumentParser(
        description="Assign a user or group to an enterprise app."
    )
    parser.add_argument(
        "--service-principal-id",
        required=True,
        type=parse_object_id,
        help="Object ID of the enterprise app (service principal).",
    )
    parser.add_argument(
        "--principal-id",
        required=True,
        type=parse_object_id,
        help="Object ID of the user or group to assign.",
    )
    parser.add_argument(
        "--app-role-id",
        default=DEFAULT_ACCESS_ROLE_ID,
        type=parse_object_id,
        help=(
            "App role ID to assign. The all-zero default grants the app's default "
            "access when no specific role is required."
        ),
    )
    args = parser.parse_args()

    assignment = GraphClient().request(
        "POST",
        f"/servicePrincipals/{args.service_principal_id}/appRoleAssignedTo",
        json={
            "principalId": args.principal_id,
            "resourceId": args.service_principal_id,
            "appRoleId": args.app_role_id,
        },
    )
    print(json.dumps(assignment, indent=2))


if __name__ == "__main__":
    get_main()
