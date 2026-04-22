import csv
import os
from mcp.server.fastmcp import FastMCP

_info_dir = os.path.join(os.path.dirname(__file__), "info")
CSV_PATH = next(
    os.path.join(_info_dir, f) for f in os.listdir(_info_dir) if f.endswith(".csv")
)

mcp = FastMCP("Phone Book")


def load_contacts() -> list[dict]:
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@mcp.tool()
def lookup_contact(first_name: str, last_name: str) -> str:
    """Look up a phone numbers by first and last name.

    Args:
        first_name: The person's first name.
        last_name: The person's last name.
    """
    contacts = load_contacts()
    first_lower = first_name.strip().lower()
    last_lower = last_name.strip().lower()

    matches = [
        c for c in contacts
        if c["FirstName"].strip().lower() == first_lower
        and c["LastName"].strip().lower() == last_lower
    ]

    if not matches:
        return f"No contact found for {first_name} {last_name}."

    lines = []
    for c in matches:
        parts = [f"**{c['FirstName']} {c['LastName']}**"]
        home = c.get("PhoneHome", "").strip()
        mobile = c.get("PhoneMobile", "").strip()
        work = c.get("PhoneWork", "").strip()

        if home:
            parts.append(f"Home:   {home}")
        if mobile:
            parts.append(f"Mobile: {mobile}")
        if work:
            parts.append(f"Work:   {work}")

        if len(parts) == 1:
            parts.append("No phone numbers on file.")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


@mcp.tool()
def reverse_lookup(phone_number: str) -> str:
    """Look up who owns a phone number, or find contacts whose number ends with the given digits.

    Args:
        phone_number: The phone number or partial number (e.g. last 4 digits) to search for.
    """
    contacts = load_contacts()
    digits = "".join(ch for ch in phone_number if ch.isdigit())

    phone_fields = ["PhoneHome", "PhoneMobile", "PhoneWork"]
    matches = []
    for c in contacts:
        for field in phone_fields:
            raw = c.get(field, "").strip()
            if not raw:
                continue
            contact_digits = "".join(ch for ch in raw if ch.isdigit())
            if contact_digits == digits or contact_digits.endswith(digits):
                matches.append((c, field, raw))
                break

    if not matches:
        return f"No contact found with a phone number matching '{phone_number}'."

    lines = []
    for c, field, number in matches:
        label = {"PhoneHome": "Home", "PhoneMobile": "Mobile", "PhoneWork": "Work"}[field]
        lines.append(f"**{c['FirstName']} {c['LastName']}** — {label}: {number}")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
