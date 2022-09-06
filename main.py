from youtube_statistics import YTstats

API_KEY = "AIzaSyA-0KfpLK04NpQN1XghxhSlzG-WkC3DHLs"

channel_id = "UCcgqSM4YEo5vVQpqwN-MaNw"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.dump()