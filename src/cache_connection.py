class CacheConnection:

    def __init__(self, cache_id, latency):
        self.cache_id = cache_id
        self.latency = latency

    def __repr__(self):
        return "Cache {} connected with latency {}".format(self.cache_id, self.latency)
