from endpoint import Endpoint
from cache_connection import CacheConnection
from video_request import VideoRequest


class ProblemData:
    def __init__(self):
        self.n_videos = 0
        self.n_endpoints = 0
        self.n_requests = 0
        self.n_caches = 0
        self.s_caches = 0
        self.video_sizes = []
        self.endpoints = []
        self.requests = []

    def load_data(self, input_file):
        with open(input_file, 'r') as f:
            self.n_videos, self.n_endpoints, self.n_requests, self.n_caches, self.s_caches = list(map(int, f.readline().split()))
            self.video_sizes = list(map(int, f.readline().split()))

            for i in range(self.n_endpoints):
                datacenter_latency, num_connected_caches = list(map(int, f.readline().split()))
                e = Endpoint(datacenter_latency)
                for j in range(num_connected_caches):
                    id_cache, latency_cache = list(map(int, f.readline().split()))
                    conn = CacheConnection(id_cache, latency_cache)
                    e.connected_caches.append(conn)
                self.endpoints.append(e)

            for i in range(self.n_requests):
                video, endpoint, num_requests = list(map(int, f.readline().split()))
                r = VideoRequest(video, endpoint, num_requests)
                self.endpoints[endpoint].video_requests.append(r)
                self.requests.append(r)

    def compute_video_values(self):
        """
            Value is equal to (number of times requested * time saved) / video size
        """
        for endp in self.endpoints:
            for req in endp.video_requests:
                for cache in endp.connected_caches:
                    value = req.n_requests * (endp.datacenter_latency - cache.latency)
                    value = value / float(self.video_sizes[req.video_id])
                    endp.video_values[(cache.cache_id, req.video_id)] = value
