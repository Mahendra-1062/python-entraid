import argparse
import json

from graph_client import GraphClient


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a Microsoft Entra ID app registration."
    )
    parser.add_argument("--display-name", required=True)
    parser.add_argument(
        "--sign-in-audience",
        choices=(
            "AzureADMyOrg",
            "AzureADMultipleOrgs",
            "AzureADandPersonalMicrosoftAccount",
            "PersonalMicrosoftAccount",
        ),
        default="AzureADMyOrg",
    )
    args = parser.parse_args()

    application = GraphClient().request(
        "POST",
        "/applications",
        json={
            "displayName": args.display_name,
            "signInAudience": args.sign_in_audience,
        },
    )
    print(json.dumps(application, indent=2))


if __name__ == "__main__":
    main()
