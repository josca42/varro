"""CLI for creating and deleting users."""

import argparse
import secrets
import string
from pathlib import Path

from varro.db.crud.user import user as crud_user

CREDENTIALS_DIR = Path(__file__).resolve().parent.parent / "user_credentials"


def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def create_user(email: str, name: str | None = None):
    existing = crud_user.get_by_email(email)
    if existing:
        print(f"User {email} already exists (id={existing.id})")
        return

    password = generate_password()
    new_user = crud_user.create_with_password(email, password, name=name)

    CREDENTIALS_DIR.mkdir(exist_ok=True)
    cred_file = CREDENTIALS_DIR / f"{email}.txt"
    cred_file.write_text(f"email: {email}\npassword: {password}\n")
    cred_file.chmod(0o600)

    print(f"Created user {email} (id={new_user.id})")
    print(f"Credentials written to {cred_file}")

def add_balance(email: str, balance: int):
    existing = crud_user.get_by_email(email)
    if not existing:
        print(f"User {email} not found")
        return

    crud_user.update(existing, balance=balance)
    print(f"Added {balance} to user {email} (id={existing.id})")
    print(f"User balance: {existing.balance}")

def delete_user(email: str):
    existing = crud_user.get_by_email(email)
    if not existing:
        print(f"User {email} not found")
        return

    crud_user.delete(existing)

    cred_file = CREDENTIALS_DIR / f"{email}.txt"
    if cred_file.exists():
        cred_file.unlink()

    print(f"Deleted user {email} (id={existing.id})")


def list_users():
    df = crud_user.get_table()
    if df.empty:
        print("No users found")
        return
    print(df[["id", "email", "name", "is_active", "created_at"]].to_string(index=False))


parser = argparse.ArgumentParser(description="Manage Varro users")
sub = parser.add_subparsers(dest="command", required=True)

p_create = sub.add_parser("create", help="Create a new user")
p_create.add_argument("email")
p_create.add_argument("--name", default=None)

p_delete = sub.add_parser("delete", help="Delete a user")
p_delete.add_argument("email")

sub.add_parser("list", help="List all users")

args = parser.parse_args()

if args.command == "create":
    create_user(args.email, args.name)
elif args.command == "delete":
    delete_user(args.email)
elif args.command == "list":
    list_users()
