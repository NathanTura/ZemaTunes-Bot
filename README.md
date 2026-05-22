# 🎵 ZemaTunes-Bot

A Telegram bot for downloading music and videos from **YouTube** — fast, clean, and easy to use.

> ⚡ Built for personal use. Search any song or paste a YouTube link and get it straight in Telegram.

---

## ✨ Features

- 🎵 Download audio from YouTube links
- 🔍 Search songs by name and download instantly
- 🎬 Download YouTube videos
- 🎙️ Voice recognition — hum or record audio to find a song
- 🎤 Fetch song lyrics
- ⚙️ Choose your preferred audio format and quality
- 📣 Admin broadcast system

---

## 🚀 Quick Start

### 1. Prerequisites

- Python **3.10.12**
- FFmpeg installed and added to PATH

**Install FFmpeg:**

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows — download from https://ffmpeg.org/download.html
# then add the /bin folder to your system PATH
```

Verify it works:
```bash
ffmpeg -version
```

---

### 2. Clone This Repo

```bash
git clone https://github.com/NathanTura/ZemaTunes-Bot.git
cd ZemaTunes-Bot
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Up Your Config

Copy the example config and fill in your credentials:

```bash
cp config.env.example config.env
```

Then edit `config.env`:

```env
ADMIN_USER_IDS = "your_telegram_user_id"

API_ID = "your_telegram_api_id"
API_HASH = "your_telegram_api_hash"

BOT_TOKEN = "your_telegram_bot_token"

SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"

GENIUS_ACCESS_TOKEN = "your_genius_access_token"
```

**Where to get these:**
| Key | Source |
|---|---|
| `BOT_TOKEN` | [@BotFather](https://t.me/BotFather) on Telegram |
| `API_ID` / `API_HASH` | [my.telegram.org](https://my.telegram.org) |
| `ADMIN_USER_IDS` | Your Telegram user ID (use [@userinfobot](https://t.me/userinfobot)) |
| `SPOTIFY_*` | [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) |
| `GENIUS_ACCESS_TOKEN` | [Genius API](https://genius.com/api-clients) |

---

### 5. Run the Bot

```bash
python main.py
```

---

## 💬 Commands

| Command | Description |
|---|---|
| `/start` | Welcome message |
| `/search <song name>` | Search and download a song |
| `/settings` | Change audio format, quality, etc. |
| `/quality` | Quickly change audio quality |
| `/help` | Get help |
| `/ping` | Check bot response time |
| `/stats` | Usage statistics |

### Admin Only
| Command | Description |
|---|---|
| `/broadcast` | Message all subscribed users |
| `/broadcast_to_all` | Message every user |

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
