import argparse
import json

from graph_client import GraphClient


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Microsoft Entra ID group.")
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--mail-nickname", required=True)
    parser.add_argument("--description", default="")
    parser.add_argument(
        "--type",
        choices=("security", "microsoft-365"),
        default="security",
        help="Group type (default: security).",
    )
    args = parser.parse_args()

    is_microsoft_365 = args.type == "microsoft-365"
    group = GraphClient().request(
        "POST",
        "/groups",
        json={
            "displayName": args.display_name,
            "description": args.description,
            "mailEnabled": is_microsoft_365,
            "mailNickname": args.mail_nickname,
            "securityEnabled": not is_microsoft_365,
            "groupTypes": ["Unified"] if is_microsoft_365 else [],
        },
    )
    print(json.dumps(group, indent=2))


if __name__ == "__main__":
    main()
