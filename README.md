# Phone Book MCP Server

An MCP (Model Context Protocol) server that lets Claude look up phone numbers by name.

## Requirements

- Python 3.12+
- A CSV file in the `info/` folder with columns: `FirstName`, `LastName`, `PhoneHome`, `PhoneMobile`, `PhoneWork`

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

> "I need the phone number for Mark Smith."

Claude will return the available home, mobile, and work numbers for that person.

## CSV format

The `info/` folder should contain exactly one `.csv` file with the following columns:

| Column | Description |
|---|---|
| `FirstName` | First name |
| `LastName` | Last name |
| `PhoneHome` | Home phone number |
| `PhoneMobile` | Mobile phone number |
| `PhoneWork` | Work phone number |
