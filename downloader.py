import yt_dlp as youtube_dl

url = input("Insert a YouTube video URL: ")
output_format = input("Insert the desired output format: ")

valid_formats = ['mp4', 'mp3', 'mkv', 'webm', 'flv']

if output_format not in valid_formats:
    print("Invalid format")
else:
    def download_video(url, output_format):
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.' + output_format,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    download_video(url, output_format)
