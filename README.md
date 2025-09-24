# Downloader Program

This program allows you to download songs from Spotify, videos in the highest quality from YouTube, and reels from Instagram, saving them to specified directories.

## Features

- Download songs from Spotify
- Download videos from YouTube in highest quality
- Download reels from Instagram
- Organize downloads into separate directories

## Installation

1. Ensure you have Python installed.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python downloader.py --platform <platform> --url <url>
   ```

## Usage

- For Spotify: `python downloader.py --platform spotify --url <spotify_url>`
- For YouTube: `python downloader.py --platform youtube --url <youtube_url>`
- For Instagram: `python downloader.py --platform instagram --url <instagram_url>`

## Directories

- Songs: F:\Downloader\Downloads\Songs
- Videos: F:\Downloader\Downloads\Videos
- Reels: F:\Downloader\Downloads\Reels

## Notes

- Some platforms may require authentication.
- Ensure the directories exist or the script will create them.

## Dependencies

- spotdl
- yt-dlp
- instaloader
