import json
import requests

class RestClient:

    def __init__(self, ip, username, password, domain):
        """
        """
        self.cluster_ip = ip
        self.username = username
        self.password = password
        self.domain = domain
        self.api_prefix = "https://{}/irisservices/api/v1/".format(
            self.cluster_ip)
        
        # Generate access token and use during rest api calls.
        self.token = None
        self.generate_access_token()


    def get(self, api, headers={}):
        """
        GET request.
        :returns exitcode, response
        """
        api = self.api_prefix + api
        headers["Authorization"] = "Bearer {}".format(self.token)
        response = requests.get(url=api, headers=headers, verify=False)
        return response.status_code, response.content


    def put(self, api, headers={}, **kwargs):
        """
        PUT request.
        :returns exitcode, response
        """
        api = self.api_prefix + api
        headers["Authorization"] = "Bearer {}".format(self.token)
        response = requests.put(url=api, headers=headers, verify=False, **kwargs)
        return response.status_code, response.content


    def post(self, api, headers={}, **kwargs):
        """
        POST request.
        :returns exitcode, response
        """
        api = self.api_prefix + api
        if self.token and not headers:
            headers["Authorization"] = "Bearer {}".format(self.token)
        response = requests.post(
            url=api, headers=headers, verify=False, **kwargs)
        return response.status_code, response.content

    def generate_access_token(self):
        """
        Generates token to access the cluster resources. Uses the cluster
        config details from config file and generates token.
        """
        access_token_api = "public/accessTokens"
        args = {"domain": self.domain,
                "username": self.username,
                "password": self.password}
        status_code, resp = self.post(access_token_api, data=json.dumps(args))
        if status_code != 201:
            err_msg = json.loads(resp.decode("utf-8"))["message"]
            print("Failed to fetch access token, {}".format(err_msg))
            exit()
        self.token = json.loads(resp.decode('utf-8'))["accessToken"]
