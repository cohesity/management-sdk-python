#!/usr/bin/env python

# Copyright (c) 2018 by Cohesity, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

'''
This tool relies on VMWare python sdk samples.
Fetch the code from:
https://github.com/vmware/vsphere-automation-sdk-python

Add this path to your environment's PYTHONPATH:
<path to vsphere-automation-sdk-python>
'''

import argparse
import cohesity
from cohesity.rest import ApiException
from pprint import pprint
import time

from base_task import BaseTask
from vmware_tagger import VMTagger

class ConvertProtectionJob(BaseTask):

    def __init__(self):
        BaseTask.__init__(self, "Convert protection job to tag based job.")
        self.jobid = None

        self.argparser.add_argument('-j', '--jobid', type=int,
                                    help="Protection job id to convert.")

        self.argparser.add_argument('--vuser',
                                    default="administrator@vsphere.local",
                                    help="vCenter username.")
        self.argparser.add_argument('--vpassword',
                                    help="vCenter password.")
        self.argparser.add_argument('--vhost',
                                    help="vCenter host.")
        self.argparser.add_argument('--tag-id',
                                    help="Tag id")

    def parse_args(self):
        BaseTask.parse_args(self)

        self.jobid = self.args.jobid
        self.vuser = self.args.vuser
        self.vpassword = self.args.vpassword
        self.vhost = self.args.vhost
        self.tag_id = self.args.tag_id

        self.tagger = VMTagger(self.vuser, self.vpassword, self.vhost)

    def run(self):
        print 'Going to convert job id: %s' % self.jobid
        vm_ids = self.get_job_objects()
        vmware_ids = vm_ids.values()
        print vmware_ids

        tagged_vms = self.tagger.tag_vms(vmware_ids, self.tag_id)
        if set(tagged_vms) != set(vmware_ids):
            print 'Unable to tag all vms in job, aborting.'
            sys.exit(1)       

        key = None
        for item in vm_ids.iterkeys():
            key = item
            break

        self.refresh_protection_source()
        cohesity_tag_id = self.get_local_tag_id(key)
        print 'Local tag id: %s' % cohesity_tag_id
        self.update_job_with_tag(cohesity_tag_id)

    def update_job_with_tag(self, tag_id):
        api_instance = cohesity.ProtectionJobsApi()
        job = api_instance.get_protection_job_by_id(self.jobid)
        job.source_ids = None
        job.vm_tag_ids = [[tag_id]]

        body = cohesity.models.ProtectionJobRequestBody()
        for attr in body.attribute_map:
            value = getattr(job, attr, None)
            if value is None: continue
            setattr(body, attr, value)

        response = api_instance.update_protection_job(body, self.jobid)
        pprint(response)
        print 'Success!!'

    def refresh_protection_source(self):
        print 'Going to refresh object tree: %s' % self.protection_source
        protection_sources_api = cohesity.ProtectionSourcesApi()
        protection_sources_api.refresh_protection_source_by_id(self.protection_source)
        time.sleep(60)
        print 'Refreshed object tree'

    def get_local_tag_id(self, key):
        objects_api = cohesity.ProtectionSourcesApi()
        objects =\
                objects_api.get_protection_sources_objects(object_ids=[str(key)])
        assert len(objects) == 1

        vmware_info = objects[0].vm_ware_protection_source
        if not vmware_info:
            print 'Found non-vmware object!'
            sys.exit(1)
        tags = vmware_info.tag_attributes
        for tag in tags:
            if tag.uuid == self.tag_id:
                return tag.id
        print 'Couldnt find tag id'
        sys.exit(1)

    def get_job_objects(self):
        api_instance = cohesity.ProtectionJobsApi()
        job = api_instance.get_protection_job_by_id(self.jobid)
        object_ids = job.source_ids
        if not object_ids:
            print 'No sources found in job.'
            sys.exit(1)
        print 'Found objects: %s' % object_ids

        objects_api = cohesity.ProtectionSourcesApi()
        object_ids = map(str, object_ids)
        objects = objects_api.get_protection_sources_objects(object_ids=object_ids)
        vm_ids = {} 
        for vm in objects:
            self.protection_source = vm.parent_id
            vmware_info = vm.vm_ware_protection_source
            if not vmware_info:
                print 'Found non-vmware object!'
                sys.exit(1)
            obj_id = vmware_info.id
            assert obj_id.mor_type == 'VirtualMachine'
            vm_id = obj_id.mor_item
            vm_ids[vm.id] = vm_id
        return vm_ids

if __name__ == "__main__":
    task = ConvertProtectionJob()
    task.main()
