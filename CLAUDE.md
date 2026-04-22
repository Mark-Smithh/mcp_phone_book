# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install mcp
```

## Running the server

```bash
.venv/bin/python3 server.py
```

## Connecting to Claude Code (CLI)

```bash
claude mcp add phone-book /path/to/.venv/bin/python3 -- /path/to/server.py
```

## Architecture

This is a single-file MCP server (`server.py`) built with `fastmcp`. It exposes tools to Claude via the Model Context Protocol.

- The CSV data file lives in `info/` and is auto-detected by extension — there should be exactly one `.csv` file there.
- `load_contacts()` re-reads the CSV on every tool call (no caching), so changes to the CSV take effect immediately without restarting the server.
- Tools return markdown-formatted strings that Claude renders in its response.

## CSV format

| Column | Description |
|---|---|
| `FirstName` | First name |
| `LastName` | Last name |
| `DisplayName` | Full display name (not used by tools) |
| `PhoneHome` | Home phone |
| `PhoneMobile` | Mobile phone |
| `PhoneWork` | Work phone |

## Available tools

- **`lookup_contact(first_name, last_name)`** — forward lookup: name → phone numbers
- **`reverse_lookup(phone_number)`** — reverse lookup: phone number or partial digits → contact name. Strips non-digits before comparing, so any format works. Matches on exact or suffix (e.g. last 4 digits).
