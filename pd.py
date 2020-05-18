#!/usr/bin/env python3

import argparse
import os
from pipedrive import Pipedrive


ENV_PIPEDRIVE_TOKEN = os.environ.get("PIPEDRIVE_TOKEN")


root_parser = argparse.ArgumentParser()
root_parser.add_argument(
    "-t", "--token", default=ENV_PIPEDRIVE_TOKEN, required=not bool(ENV_PIPEDRIVE_TOKEN)
)
root_subparsers = root_parser.add_subparsers(required=True, dest="command")

deals_parser = root_subparsers.add_parser("deals")
deals_subparsers = deals_parser.add_subparsers(required=True, dest="command2")

deals_create_parser = deals_subparsers.add_parser("create")
deals_create_parser.add_argument("--title", required=True)
deals_create_parser.add_argument("--value", required=True, type=int)
deals_create_parser.add_argument("--currency", required=True)

products_parser = root_subparsers.add_parser("products")
products_subparsers = products_parser.add_subparsers(required=True, dest="command2")

products_create_parser = products_subparsers.add_parser("create")
products_create_parser.add_argument("--name", required=True)
products_create_parser.add_argument("--price", required=True, type=int)
products_create_parser.add_argument("--currency", required=True)

persons_parser = root_subparsers.add_parser("persons")
persons_subparsers = persons_parser.add_subparsers(required=True, dest="command2")

persons_create_parser = persons_subparsers.add_parser("create")
persons_create_parser.add_argument("--name", required=True)
persons_create_parser.add_argument("--email")
persons_create_parser.add_argument("--phone")
persons_create_parser.add_argument("--org-id", type=int)

organization_parser = root_subparsers.add_parser("organizations")
organization_subparsers = organization_parser.add_subparsers(
    required=True, dest="command2"
)

organization_create_parser = organization_subparsers.add_parser("create")
organization_create_parser.add_argument("--name", required=True)

args = root_parser.parse_args()


pipedrive = Pipedrive(args.token)


def deals_create():
    pipedrive.create_deals(
        {
            "title": args.title,
            "value": args.value,
            "currency": args.currency,
            "status": "open",
        },
    )


def products_create():
    pipedrive.create_products(
        {
            "name": args.name,
            "prices": [{"price": args.price, "currency": args.currency,}],
        },
    )


def persons_create():
    pipedrive.create_persons(
        {
            "name": args.name,
            "email": args.email,
            "phone": args.phone,
            "org_id": args.org_id,
        },
    )


def organizations_create():
    pipedrive.create_organizations({"name": args.name})


{
    ("deals", "create"): deals_create,
    ("products", "create"): products_create,
    ("persons", "create"): persons_create,
    ("organizations", "create"): organizations_create,
}[(args.command, args.command2)]()
