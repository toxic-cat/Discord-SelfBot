# Discord Self-Bot

This is a feature-rich Discord self-bot with over 50 commands.

**Disclaimer:** Using a self-bot is against Discord's Terms of Service and can result in your account being banned. Please be aware of this risk before proceeding.

## Table of Contents

- [Features](#features)
- [How To Setup/Install](#how-to-setupinstall)
- [Commands](#commands)
  - [Fun](#fun)
  - [Utility](#utility)
  - [Discord Utils](#discord-utils)
  - [Management](#management)
  - [Cloning](#cloning)
  - [Automation](#automation)
  - [Moderation](#moderation)
  - [NSFW](#nsfw)
  - [Account](#account)
  - [Raiding](#raiding)
  - [Text](#text)
  - [Misc](#misc)

## Features

- **Paginated Help Command:** The help command is designed to be under 2000 characters per page, making it accessible to non-Nitro users.
- **Extensive Command List:** Over 50 commands, including:
    - Server Cloner
    - Autobeefer
    - Spammer
    - Moderation
    - Fun
    - Utility
    - NSFW
    - Account
    - Raiding/Nuking
- **Linux and Termux Compatibility:** The bot is designed to be fully executable on Linux and Termux.

## How To Setup/Install

### Windows

1. **Update `config.json`**: Enter your bot token and preferred prefix.
2. **Installation**:
   ```bash
   $ git clone https://github.com/your-repo/your-repo.git
   $ python -m pip install -r requirements.txt
   $ python main.py
   ```

### Linux

1. **Update `config.json`**: Enter your bot token and preferred prefix.
2. **Installation**:
   ```bash
   $ sudo apt-get install git python3-pip
   $ git clone https://github.com/your-repo/your-repo.git
   $ cd your-repo
   $ python3 -m pip install -r requirements.txt
   $ python3 main.py
   ```

### Termux

1. **Update `config.json`**: Enter your bot token and preferred prefix.
2. **Installation**:
   ```bash
   $ pkg install git python
   $ git clone https://github.com/your-repo/your-repo.git
   $ cd your-repo
   $ pip install -r requirements.txt
   $ python main.py
   ```

## Commands

### Fun

- `airplane`: Sends a 9/11 attack (warning: use responsibly).
- `minesweeper`: Play a game of Minesweeper with custom grid size.
- `leetspeak`: Speak like a hacker, replacing letters.
- `dick`: Show the "size" of a user's dick.
- `reverse`: Reverse the letters of a message.
- `ascii`: Convert a message to ASCII art.
- `8ball`: Ask the magic 8ball a question.
- `gayrate`: See how gay a user is.
- `simprate`: See how much of a simp a user is.
- `slots`: Play a game of slots.

### Utility

- `uptime`: Returns how long the selfbot has been running.
- `ping`: Returns the bot's latency.
- `geoip`: Looks up the IP's location.
- `tts`: Converts text to speech and sends an audio file (.wav).
- `qr`: Generate a QR code from the provided text and send it as an image.
- `pingweb`: Ping a website and return the HTTP status code (e.g., 200 if online).
- `gentoken`: Generate an invalid but correctly patterned token.
- `quickdelete`: Send a message and delete it after 2 seconds.
- `firstmessage`: Get the link to the first message in the current channel.
- `google`: Get a google search link for a query.
- `urban`: Get the urban dictionary definition of a term.

### Discord Utils

- `usericon`: Get the profile picture of a user.
- `guildinfo`: Get information about the current server.
- `guildicon`: Get the icon of the current server.
- `guildbanner`: Get the banner of the current server.
- `nitro`: Generate a fake Nitro code.

### Management

- `changeprefix`: Change the bot's prefix.
- `shutdown`: Stop the selfbot.
- `afk`: Enable or disable AFK mode.
- `autoreply`: Enable or disable automatic replies.
- `copycat`: Automatically reply with the same message whenever the mentioned user speaks.

### Cloning

- `clone`: Clones the current server.

### Automation

- `autobeefer`: Automatically beef with a user.
- `spam`: Spams a message a specified number of times.

### Moderation

- `kick`: Kicks a member from the server.
- `ban`: Bans a member from the server.
- `unban`: Unbans a member from the server.
- `purge`: Purges a specified number of messages from a channel.

### NSFW

**Disclaimer:** These commands are for use in NSFW channels only. By using these commands, you acknowledge that you are of legal age to view NSFW content.

- `lesbian`: Sends a random lesbian image.
- `boobs`: Sends a random boobs image.
- `pussy`: Sends a random pussy image.

### Account

- `avatar`: Get a user's avatar.
- `banner`: Get a user's banner.
- `userinfo`: Get information about a user.

### Raiding

**Disclaimer:** These commands are destructive and can cause irreversible damage to a server. Use them at your own risk.

- `nuke`: Deletes all channels and creates 50 new ones.
- `banall`: Bans all members in the server.
- `kickall`: Kicks all members in the server.
- `roleall`: Gives a specified role to all members in the server.

### Text

- `tiny`: Makes your text tiny.
- `zalgo`: Makes your text zalgo.

### Misc

- `whois`: Get information about a user.
- `poll`: Create a poll.
