class VideoRequest:

    def __init__(self, video_id, endpoint_id, n_requests):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.n_requests = n_requests

    def __repr__(self):
        return "{} requests of video {} from endpoint {}.".format(self.n_requests, self.video_id, self.endpoint_id)
