"""Dump REST API v0 OpenAPI schema to a JSON file."""

import json
from pathlib import Path

from django.core.management.base import BaseCommand

from apps.api.rest.v0 import api


class Command(BaseCommand):
    help = "Write OpenAPI schema for REST API v0 to a JSON file."

    def add_arguments(self, parser):
        """Add arguments to the command."""
        parser.add_argument(
            "--output",
            "-o",
            default="-",
            help="Output path (default: stdout)",
        )

    def handle(self, *args, **options):
        """Handle the command."""
        schema = api.get_openapi_schema()
        payload = dict(schema) if hasattr(schema, "keys") else schema
        out = options["output"]
        if out == "-":
            self.stdout.write(json.dumps(payload, indent=2))
        else:
            path = Path(out).resolve()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, indent=2))
