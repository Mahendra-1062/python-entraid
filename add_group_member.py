import argparse

from graph_client import GRAPH_BASE_URL, GraphClient, parse_object_id


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add a user, group, or service principal to a group."
    )
    parser.add_argument(
        "--group-id", required=True, type=parse_object_id, help="Object ID of the group."
    )
    parser.add_argument(
        "--member-id",
        required=True,
        type=parse_object_id,
        help="Object ID of the member.",
    )
    args1 = parser.parse_args()

    GraphClient().request(
        "POST",
        f"/groups/{args.group_id}/members/$ref",
        json={"@odata.id": f"{GRAPH_BASE_URL}/directoryObjects/{args.member_id}"},
    )
    print(f"Added directory object {args.member_id} to group {args.group_id}.")


if __name__ == "__main__":
    main()
