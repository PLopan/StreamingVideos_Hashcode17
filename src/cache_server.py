class CacheServer:

    def __init__(self, size):
        self.total_size = size
        self.remaining_size = size
        self.videos = set()

    def __repr__(self):
        return "Cache server with {} videos, {}MB left.".format(len(self.videos), self.remaining_size)

    def does_video_fit(self, video_size):
        return video_size <= self.remaining_size

    def add_video(self, video_id, video_size):
        self.videos.add(video_id)
        self.remaining_size -= video_size

    def is_full(self):
        return self.remaining_size == 0
