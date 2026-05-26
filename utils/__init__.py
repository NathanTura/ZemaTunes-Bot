from utils.broadcast import BroadcastManager
from utils.database import db
from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp.utils import DownloadError
from dotenv import load_dotenv
from itertools import combinations
from PIL import Image
from io import BytesIO
from yt_dlp import YoutubeDL as OriginalYoutubeDL
from shazamio import Shazam
import requests, asyncio, re, os
import bs4, wget, hashlib, time
import lyricsgenius
import spotipy
from concurrent.futures import ThreadPoolExecutor
import aiohttp
from telethon import sync
from telethon.tl.functions.messages import SendMediaRequest
from telethon.tl.types import (InputMediaUploadedDocument,
                               DocumentAttributeAudio,
                               InputMediaPhotoExternal,
                               DocumentAttributeVideo)
from FastTelethonhelper import fast_upload
from threading import Thread
import concurrent
from functools import lru_cache, partial
from .tweet_capture import TweetCapture
from .helper import sanitize_query
import io
import sys
from dataclasses import dataclass, field
from spotipy.exceptions import SpotifyException
from typing import Tuple, Any
from telethon.errors.rpcerrorlist import WebpageMediaEmptyError

def convert_json_cookies_to_netscape(json_content):
    import json
    try:
        cookies = json.loads(json_content)
        if not isinstance(cookies, list):
            return None
        lines = [
            "# Netscape HTTP Cookie File",
            "# This file was generated automatically by ZemaTunes-Bot.",
            ""
        ]
        for cookie in cookies:
            domain = cookie.get('domain', '')
            path = cookie.get('path', '/')
            secure = 'TRUE' if cookie.get('secure', False) else 'FALSE'
            expires = str(int(cookie.get('expirationDate', 0)))
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            subdomains = 'TRUE' if domain.startswith('.') else 'FALSE'
            lines.append(f"{domain}\t{subdomains}\t{path}\t{secure}\t{expires}\t{name}\t{value}")
        return "\n".join(lines)
    except Exception as e:
        print(f"Error converting JSON cookies: {e}")
        return None

def get_valid_cookie_file():
    cookie_file = os.getenv('COOKIE_FILE_PATH', 'cookies.txt')
    json_cookie_file = 'cookies.json'
    target_file = None
    if os.path.isfile(cookie_file):
        target_file = cookie_file
    elif os.path.isfile(json_cookie_file):
        target_file = json_cookie_file
        
    if not target_file:
        return None
        
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        if content.startswith('['):
            netscape_content = convert_json_cookies_to_netscape(content)
            if netscape_content:
                netscape_path = 'cookies_netscape.txt'
                with open(netscape_path, 'w', encoding='utf-8') as out:
                    out.write(netscape_content)
                return netscape_path
    except Exception as e:
        print(f"Error checking/converting cookie file: {e}")
        
    return cookie_file if os.path.isfile(cookie_file) else None

class YoutubeDL(OriginalYoutubeDL):
    def __init__(self, params=None, *args, **kwargs):
        if params is None:
            params = {}
        else:
            params = params.copy()
        
        cookie_path = get_valid_cookie_file()
        if cookie_path:
            params['cookiefile'] = cookie_path
            
        super().__init__(params, *args, **kwargs)