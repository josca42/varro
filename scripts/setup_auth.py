#!/usr/bin/env python3
"""Setup script for user authentication.

Creates users for the Chainlit app.
Run: python scripts/setup_auth.py --email user@example.com --password secret
"""
from varro.db import crud


def create_user(email: str, password: str, name: str | None = None):
    """Create a user if it doesn't exist."""
    existing = crud.user.get_by_email(email)
    if existing:
        print(f"User '{email}' already exists (id={existing.id})")
        return existing

    user = crud.user.create_with_password(email=email, password=password, name=name)
    print(f"Created user '{email}' (id={user.id})")
    return user


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a user for the Chainlit app")
    parser.add_argument("--email", required=True, help="User email")
    parser.add_argument("--password", required=True, help="User password")
    parser.add_argument("--name", help="User name")

    args = parser.parse_args()
    create_user(args.email, args.password, args.name)
