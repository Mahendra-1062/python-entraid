import argparse
import json

from graph_client import GraphClient, parse_object_id


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create an enterprise app (service principal) for an app registration."
    )
    parser.add_argument(
        "--app-id",
        required=True,
        type=parse_object_id,
        help="Application (client) ID of the app registration.",
    )
    args = parser.parse_args()
    graph = GraphClient()

    matches = graph.request(
        "GET",
        "/servicePrincipals",
        params={"$filter": f"appId eq '{args.app_id}'", "$select": "id,appId,displayName"},
    )
    if matches["value"]:
        print("An enterprise app already exists for this application:")
        print(json.dumps(matches["value"][0], indent=2))
        return

    service_principal = graph.request(
        "POST", "/servicePrincipals", json={"appId": args.app_id}
    )
    print(json.dumps(service_principal, indent=2))


if __name__ == "__main__":
    main()
