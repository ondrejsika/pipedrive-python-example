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


{("deals", "create"): deals_create,}[(args.command, args.command2)]()
