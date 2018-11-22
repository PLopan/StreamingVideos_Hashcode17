class Endpoint:

    def __init__(self, datacenter_latency):
        self.datacenter_latency = datacenter_latency
        self.connected_caches = []
        self.video_requests = []
        self.video_values = {}  # (cache_id, video_id) -> value

    def __repr__(self):
        return "Endpoint with latency {}, {} caches connected, {} video requests." \
            .format(self.datacenter_latency, len(self.connected_caches), len(self.video_requests))
