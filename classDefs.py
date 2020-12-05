# data loader

class Endpoint:
    def __init__(self, endpoint, url_params, description):
        self.endpoint, self.description, self.url_params = endpoint, description, url_params
    def get_endpoint(self):
        return self.endpoint
    def processor(self):
        # whatever is gevnt to csv, then save to local
        pass
    def __repr__(self):
        return f"{self.endpoint}, requires {self.url_params} , {self.description}"
class DataSource:
    def __init__(self, base_api_url, endpoints, forntend_url):
        self.base_api_url, self.forntend_url =  base_api_url, forntend_url
        self.endpoints = endpoints
    def get_endpoints(self):
        return [self.base_api_url + i.get_endpoint() for i in self.endpoints]

test_data_source = DataSource(
    "spotrs.io/api", 
    [
        Endpoint(endpoint="/players", url_params=["player_id"], description="gets the lifetime stats of a player, indexed by season"),
        Endpoint(endpoint="/coaches", url_params=["coach_id"], description="gets the lifetime stats of a coach, indexed by season")   
    ],
    "spotrs.io"
)

print(test_data_source.get_endpoints())