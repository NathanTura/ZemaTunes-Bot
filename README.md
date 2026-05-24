# 🎵 ZemaTunes-Bot

A personal Telegram bot for downloading music and videos from **YouTube** — designed to run locally on your machine.

> **What it does:** Search for songs by name, paste YouTube links, use voice recognition, and grab lyrics — all straight to your Telegram. It's your own private music bot!

---

## ⚡ What You Need to Know

### This is a **Local Bot**
This bot runs on **your machine** (laptop, desktop, or home server). It's designed for personal/private use — not for hosting on a public server. You keep it running, you get your music.

### Want to Deploy It?
If you want to run this on a remote server (like Render or Heroku), you'll need to handle YouTube's bot detection. The bot currently uses cookies to bypass this, but for deployment you'll need:
1. Valid YouTube cookies (frequently updated)
2. A mechanism to refresh them automatically
3. User-Agent rotation and proxy support (optional but recommended)

See the **Deployment Notes** section below for more details.

---

## ✨ Features

- 🎵 **Download Audio** — Extract audio from YouTube links, save as MP3
- 🔍 **Song Search** — Search by song name and download instantly
- 🎬 **Video Downloads** — Get the full video if you need it
- 🎙️ **Voice Recognition** — Hum or record audio to identify songs (Shazam integration)
- 🎤 **Lyrics** — Fetch song lyrics on demand
- ⚙️ **Format & Quality** — Choose audio quality and format to your liking
- 📣 **Admin Broadcast** — Send messages to all users (admin only)

---

## 🚀 Installation Guide

### Step 1: Install System Dependencies

You need **Python 3.10.12** and **FFmpeg** installed on your machine.

**Python:** Download from [python.org](https://www.python.org/downloads/) — make sure to add Python to your PATH during installation.

**FFmpeg:** This is the tool that converts videos to audio.

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS (with Homebrew)
brew install ffmpeg

# Windows
# Option A: Use Chocolatey (if you have it)
choco install ffmpeg

# Option B: Manual download
# 1. Go to https://ffmpeg.org/download.html
# 2. Download the Windows build
# 3. Extract it somewhere (e.g., C:\ffmpeg)
# 4. Add the /bin folder to your system PATH
```

**Verify FFmpeg is installed:**
```bash
ffmpeg -version
```

You should see the version info. If not, FFmpeg isn't in your PATH yet.

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/NathanTura/ZemaTunes-Bot.git
cd ZemaTunes-Bot
```

---

### Step 3: Create a Virtual Environment (Recommended)

This keeps your bot's dependencies isolated from your system Python.

```bash
# Create virtual environment
python -m venv my-env

# Activate it
# On Windows:
my-env\Scripts\activate
# On macOS/Linux:
source my-env/bin/activate
```

You'll know it worked if you see `(my-env)` at the start of your terminal.

---

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This might take a few minutes. Grab some coffee! ☕

---

### Step 5: Set Up Your Credentials

The bot needs credentials to work with Telegram and other services.

**Copy the example config:**
```bash
cp config.env.example config.env
```

**Edit `config.env` and fill in your values:**
```env
ADMIN_USER_IDS = "your_telegram_user_id"

API_ID = "your_telegram_api_id"
API_HASH = "your_telegram_api_hash"

BOT_TOKEN = "your_telegram_bot_token"

SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"

GENIUS_ACCESS_TOKEN = "your_genius_access_token"
```

**Where to get each credential:**

| Key | Where to Get It | Instructions |
|---|---|---|
| `BOT_TOKEN` | [@BotFather](https://t.me/BotFather) | Message BotFather on Telegram, use `/newbot`, follow the steps |
| `API_ID` / `API_HASH` | [my.telegram.org](https://my.telegram.org) | Log in, go to "API development tools", create an app |
| `ADMIN_USER_IDS` | Your Telegram ID | Use [@userinfobot](https://t.me/userinfobot) to get your ID |
| `SPOTIFY_CLIENT_ID` / `SECRET` | [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) | Create a new app, grab the credentials (optional if not using Spotify) |
| `GENIUS_ACCESS_TOKEN` | [Genius API](https://genius.com/api-clients) | Create a new API client, get your access token |

---

### Step 6: Run It!

```bash
python main.py
```

Your bot is now running! Open Telegram, find your bot, and hit `/start`.

---

## 💬 Available Commands

| Command | What It Does |
|---|---|
| `/start` | Welcome message, introduction |
| `/search <song name>` | Search for a song and download it |
| `/settings` | Change audio format, quality, etc. |
| `/quality` | Quickly switch audio quality |
| `/help` | Show available commands |
| `/ping` | Check if the bot is responding |
| `/stats` | See your usage stats |

**Admin Only:**
| Command | What It Does |
|---|---|
| `/broadcast` | Send a message to all subscribed users |
| `/broadcast_to_all` | Send a message to every user |

---

## 🌐 Deployment Notes

### Running Locally? ✅
You're all set! Just keep the terminal open and the bot keeps running.

### Want to Deploy to a Server? ⚠️
YouTube frequently blocks bot requests. This bot uses **cookies** to bypass that. If you deploy it to a remote server:

1. **Get YouTube Cookies**
   - Log into YouTube in a browser
   - Use a cookie extractor extension
   - Save your cookies to a file

2. **Update the Bot**
   - Pass the cookies via the `YOUTUBE_COOKIES` environment variable
   - Or modify the YouTube downloader module to load cookies from a file

3. **Keep Cookies Fresh**
   - YouTube cookies expire after a while
   - You'll need to refresh them periodically
   - Consider automating this process

4. **Optional Extras for Reliability**
   - Use proxies or VPNs to distribute requests
   - Implement User-Agent rotation
   - Add retry logic with exponential backoff
   - Monitor download success rates and adapt

**Without these measures, your remote bot will likely fail after a while.** This is why it's designed for local use — your local machine is trusted by YouTube, so no special tricks needed.

---

## 🛠️ Dependencies

- [Telethon](https://github.com/LonamiWebs/Telethon)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Shazamio](https://github.com/dotX12/ShazamIO)
- [lyricsgenius](https://github.com/johnwmillr/LyricsGenius)
- [aiosqlite](https://github.com/omnilib/aiosqlite)
- [Pillow](https://python-pillow.org/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## 🙏 Credits

This project is a fork of [MusicDownloader-Telegram-Bot](https://github.com/AdibNikjou/MusicDownloader-Telegram-Bot) by [Adib Nikjou](https://github.com/AdibNikjou) — huge props for building the original.

I adapted it to focus on YouTube-only downloads and tweaked it to my needs. Original project is licensed under the MIT License.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ by <a href="https://github.com/NathanTura">NathanTura</a></p>
