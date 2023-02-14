"""This program downloads a YouTube video or audio"""
from pytube import YouTube


def download_video(link):
    """This function downloads a YouTube video"""
    youtube_video = YouTube(link)
    version = input("Do you want to download the video or audio? (v/a): ")
    if version == "v":
        quality = input(
            "What quality do you want? (144p, 240p, 360p, 480p, 720p, 1080p): "
        )
        youtube_video = youtube_video.streams.filter(
            progressive=True
        ).get_by_resolution(resolution=quality)
    elif version == "a":
        youtube_video = youtube_video.streams.get_audio_only()
    try:
        youtube_video.download()
        print("\nDownload complete!!!!")
    except:
        print("An error has occurred")


link = input("Enter the link of the YouTube video: ")
download_video(link)
