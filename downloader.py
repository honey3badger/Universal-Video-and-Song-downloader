import os
import subprocess
import yt_dlp
import instaloader
import argparse

# Define download directories
SONGS_DIR = r"F:\Downloader\Downloads\Songs"
VIDEOS_DIR = r"F:\Downloader\Downloads\Videos"
REELS_DIR = r"F:\Downloader\Downloads\Reels"

# Ensure directories exist
os.makedirs(SONGS_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)
os.makedirs(REELS_DIR, exist_ok=True)

def download_spotify_song(url):
    """Download song from Spotify URL."""
    try:
        subprocess.run(['python', '-m', 'spotdl', url, '--output', SONGS_DIR], check=True)
        print(f"Song downloaded to {SONGS_DIR}")
    except Exception as e:
        print(f"Error downloading Spotify song: {e}")

def download_youtube_video(url):
    """Download video from YouTube in highest quality."""
    try:
        ydl_opts = {
            'outtmpl': os.path.join(VIDEOS_DIR, '%(title)s.%(ext)s'),
            'format': 'best',
            'quiet': False,
            'no_warnings': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Video downloaded to {VIDEOS_DIR}")
    except Exception as e:
        print(f"Error downloading YouTube video: {e}")

def download_instagram_reel(url):
    """Download reel from Instagram URL."""
    try:
        loader = instaloader.Instaloader(download_video_thumbnails=False, download_geotags=False, download_comments=False)
        post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])
        loader.download_post(post, target=REELS_DIR)
        print(f"Reel downloaded to {REELS_DIR}")
    except Exception as e:
        print(f"Error downloading Instagram reel: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download media from various platforms.")
    parser.add_argument('--platform', choices=['spotify', 'youtube', 'instagram'], required=True, help="Platform to download from")
    parser.add_argument('--url', required=True, help="URL to download")
    args = parser.parse_args()

    if args.platform == 'spotify':
        download_spotify_song(args.url)
    elif args.platform == 'youtube':
        download_youtube_video(args.url)
    elif args.platform == 'instagram':
        download_instagram_reel(args.url)

if __name__ == "__main__":
    main()
