# Phone Book MCP Server

An MCP (Model Context Protocol) server that lets Claude look up phone numbers by name, or look up who owns a given phone number.

## Requirements

- Python 3.12+
- A CSV file in the `info/` folder with columns: `FirstName`, `MiddleName`, `LastName`, `DisplayName`, `PhoneHome`, `PhoneMobile`, `PhoneWork`

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

## Connecting to Claude Desktop (Mac)

Add the following to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "phone-book": {
      "command": "/path/to/phone_book/.venv/bin/python3",
      "args": ["/path/to/phone_book/server.py"]
    }
  }
}
```

Then quit and relaunch Claude Desktop.

## Usage

Ask Claude naturally:

> "What's the phone number for Mark Smith?"

Claude will return the available home, mobile, and work numbers for that person.

> "What's John's number?"

If there is only one John, Claude returns their number directly. If there are multiple, Claude asks which one you mean.

> "What's the number for Lucan Jr.?"

Suffixes like Jr., Sr., II, III, IV are recognized and matched correctly regardless of how Claude parses the name.

> "Who's phone number is this? 323-574-2262"

> "Who's phone number ends in 2262?"

Claude will search all phone fields and return the matching contact(s). Partial lookups using just the last few digits are supported.

## CSV format

The `info/` folder should contain exactly one `.csv` file with the following columns:

| Column | Description |
|---|---|
| `FirstName` | First name (may include a suffix, e.g. `Lucan Jr.`) |
| `MiddleName` | Middle name (not used by tools) |
| `LastName` | Last name |
| `DisplayName` | Full display name (not used by tools) |
| `PhoneHome` | Home phone number |
| `PhoneMobile` | Mobile phone number |
| `PhoneWork` | Work phone number |
