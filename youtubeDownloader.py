from pytube import YouTube

url = input(" please define URL : ")
video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path= '/')