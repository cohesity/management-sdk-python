#!/usr/bin/env python
'''
Base class from which tools using Cohesity Rest APIs should inherit.

Derived class should implement parse_args and run. Tool should be executed by
calling the main method of the class.
'''

import argparse
import sys
import urllib3

sys.path.append('../sdk')
from prettytable import PrettyTable

urllib3.disable_warnings()

import cohesity
from cohesity.api_client import ApiClient
from cohesity.rest import ApiException
from cohesity.configuration import Configuration

class BaseTask:

    def __init__(self, description):
        self.user = None
        self.password = None
        self.host = None
        self.args = None
        self.config = None #Populated after creating session.

        self.argparser = argparse.ArgumentParser(description=description)
        self.argparser.add_argument('-u', '--user', default='admin',
                                    help="Username for rest api.")
        self.argparser.add_argument('-p', '--password', 
                                    help="Password for rest api.")
        self.argparser.add_argument('--host', 
                                    help="Hostname or ip of the cohesity cluster")

    def parse_args(self):
        self.args = self.argparser.parse_args()
        if (not self.args.host):
          self.argparser.print_help(sys.stderr)
          sys.exit(1)
        
        if (not self.args.password):
          self.argparser.print_help(sys.stderr)
          sys.exit(1)

        self.user = self.args.user
        self.password = self.args.password
        self.host = self.args.host

    def create_session(self):
        config = Configuration()
        config.host = 'https://%s/irisservices/api/v1' % self.host
        config.verify_ssl = False

        body = cohesity.AccessTokenCredential(username=self.user, \
                                              password=self.password)

        try: 
            # Generate an Access Token.
            api_instance = cohesity.AccessTokensApi()
            api_response = api_instance.generate_access_token(body)
            config.api_key['Authorization'] = api_response.access_token
            config.api_key_prefix['Authorization'] = api_response.token_type
        except ApiException as e:
            print "Exception when calling generate_access_token: %s\n" % e
            sys.exit(1)
        config.api_client = ApiClient(header_name="Authorization", header_value= \
                               api_response.token_type + ' '+ \
                               api_response.access_token)
        self.config = config
        print "Successfully established session to <%s> using username <%s>\n" % (self.host,self.user)

    def run(self):
        # Derived class to implement.
        print ""
    def print_table(self, table_header, table_data):
        table = PrettyTable(table_header)
        for row in table_data:
            table.add_row(row)
        print(table)

    def main(self):
        self.parse_args()
        self.create_session()
        self.run()

if __name__ == '__main__':
    task = BaseTask('Base task.')
    task.main()

