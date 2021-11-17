from pytube import YouTube
from colorama import init,Fore 

print(Fore.YELLOW+'\n---------- Welcome to YouTube Downloader ----------\n')

url = input(Fore.BLUE+' [ * ] '+Fore.WHITE+'Enter URL : ')
print(Fore.GREEN+'\n i trying concten to '+url)
video = YouTube(url)
stream = video.streams.get_highest_resolution()

#locate = input(Fore.BLUE+' [ ? ] '+Fore.WHITE+'location for Download video : ')
stream.download()
