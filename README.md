# Hadith Discord Bot

This is a simple Discord bot that sends a random Hadith every 12 hours to a specific channel, and pings a specified role. The Hadiths are stored in a `hadiths.txt` file, from which a random Hadith is selected for each message.

## Features
- Sends a random Hadith to a specified Discord channel every 12 hours.
- Pings a specific role when sending the Hadith.
- Reads Hadiths from a text file (`hadiths.txt`), with each Hadith on a new line.

## Requirements

- Python 3.8 or above
- `discord.py` library (version 1.x or 2.x depending on your implementation)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/T-P-S-G-A/Discord-Hadith-Bot.git
   cd Discord-Hadith-Bot


## How to use:
- Replace all **"Placeholder" Variables Values** with Your Personal DiscordAPI Token and Channel ID & Role ID
- Execute the Python Program after setting up your Discord Bot (with Necessary Intents)

   ### Intents that are Required
   - (Guilds) Server Members Intent
   - Message Content Intent
