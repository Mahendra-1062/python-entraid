import argparse
import json
import re
from getpass import getpass

from graph_client import GraphClient


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Microsoft Entra ID user.")
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--user-principal-name", required=True)
    parser.add_argument("--mail-nickname")
    args = parser.parse_args()

    password = getpass("Temporary password (input hidden): ")
    confirmation = getpass("Confirm temporary password: ")
    if not password or password != confirmation:
        parser.error("Passwords must be non-empty and match.")

    mail_nickname = args.mail_nickname or re.sub(
        r"[^A-Za-z0-9._'-]", "", args.user_principal_name.split("@", 1)[0]
    )
    if not mail_nickname:
        parser.error("Could not derive a mail nickname; provide --mail-nickname.")

    user = GraphClient().request(
        "POST",
        "/users",
        json={
            "accountEnabled": True,
            "displayName": args.display_name,
            "mailNickname": mail_nickname,
            "userPrincipalName": args.user_principal_name,
            "passwordProfile": {
                "forceChangePasswordNextSignIn": True,
                "password": password,
            },
        },
    )
    print(json.dumps(user, indent=2))


if __name__ == "__main__":
    main()
