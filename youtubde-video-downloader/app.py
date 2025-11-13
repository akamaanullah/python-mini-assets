import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',  # Best quality available
        'outtmpl': '%(title)s.%(ext)s'  # Save file with video title
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_video("https://www.youtube.com/watch?v=fxqE27gIZcc")
