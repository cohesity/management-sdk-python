import json
import requests
import urllib3
import configparser

# Disable warnings raised for unverified https requests.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RestClient:

    __instance = None

    @staticmethod
    def get_instance(conf_type):
        """
        """
        if not RestClient.__instance:
            RestClient(conf_type=conf_type)

        if RestClient.__instance == None:
            exit()
        return RestClient.__instance

    def __init__(self, conf_type="export"):
        """
        """
        if not RestClient.__instance:
            RestClient.__instance = self

        # Fetch the Cluster credentials from config file.
        import configparser
        configparser = configparser.ConfigParser()
        configparser.read('config.ini')
        cluster_config_type = conf_type + "_cluster_config"
        self.cluster_ip = configparser.get(cluster_config_type, "cluster_ip")
        self.username = configparser.get(cluster_config_type, "username")
        self.password = configparser.get(cluster_config_type, "password")
        self.domain = configparser.get(cluster_config_type, "domain")

        self.api_prefix = "https://{}/irisservices/api/v1/public/".format(
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
        if not headers:
            headers["Authorization"] = "Bearer {}".format(self.token)
        response = requests.get(url=api, headers=headers, verify=False)
        return response.status_code, response.content


    def post(self, api, headers={}, **kwargs):
        """
        POST request.
        :returns exitcode, response
        """
        api = self.api_prefix + api
        if not headers and self.token:
            headers["Authorization"] = "Bearer {}".format(self.token)
        response = requests.post(
            url=api, headers=headers, verify=False, **kwargs)
        return response.status_code, response.content

    def generate_access_token(self):
        """
        Generates token to access the cluster resources. Uses the cluster
        config details from config file and generates token.
        """
        access_token_api = "accessTokens"
        args = {"domain": self.domain,
                "username": self.username,
                "password": self.password}
        status_code, resp = self.post(access_token_api, data=json.dumps(args))
        if status_code != 201:
            err_msg = json.loads(resp.decode("utf-8"))["message"]
            print("Failed to fetch access token, {}".format(err_msg))
            exit()
        self.token = json.loads(resp.decode('utf-8'))["accessToken"]