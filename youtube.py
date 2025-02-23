import yt_dlp
import os

base_path = "data"

def download_audio_from_youtube(youtube_url, output_path):
    save_path = os.path.join(base_path, output_path)
    os.makedirs(save_path, exist_ok=True)
    # Options to extract audio in the best format available
    ydl_opts = {
        'format': 'bestaudio/best',  # Extract best available audio
        'outtmpl': f'{os.path.join(save_path, output_path)}.%(ext)s',  # Output file template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # You can change this to 'wav', 'm4a', etc.
            'preferredquality': '192',  # Adjust audio quality if needed
        }],
        'quiet': False,  # Set to True to suppress output
        'keepvideo': True  # Keep the original file
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Example usage
if __name__ == '__main__':
    youtube_url = input("Enter YouTube URL: ")
    output_path = input("Enter output file path (without extension): ")
    download_audio_from_youtube(youtube_url, output_path)