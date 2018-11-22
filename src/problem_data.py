from endpoint import Endpoint
from cache_connection import CacheConnection
from video_request import VideoRequest
from cache_server import CacheServer


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
        self.total_video_values = []
        self.cache_servers = []

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

    def compute_total_values(self):
        """
            Take into consideration the values of videos considering every endpoint, not only one.
            The list total_video_values is ordered by total value.
        """
        total_video_values_dict = {}
        for endp in self.endpoints:
            for key, value in endp.video_values.items():
                total_value = total_video_values_dict.get(key, 0)
                total_value += value
                total_video_values_dict[key] = total_value

        for (cache_id, video_id), value in total_video_values_dict.items():
            self.total_video_values.append((cache_id, video_id, value))

        self.total_video_values = sorted(self.total_video_values, key=lambda x: -x[2])

    def are_all_caches_full(self):
        for cache in self.cache_servers:
            if not cache.is_full():
                return False
        return True

    def fill_caches(self):
        self.cache_servers = [CacheServer(self.s_caches) for _ in range(self.n_caches)]
        for (cache_id, video_id, value) in self.total_video_values:
            if self.are_all_caches_full():
                break
            elif self.cache_servers[cache_id].does_video_fit(self.video_sizes[video_id]):
                self.cache_servers[cache_id].add_video(video_id, self.video_sizes[video_id])

