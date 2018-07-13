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
Given a tag id and vm-ids, it will attach the tag to the vms.
'''
from samples.vsphere.common.service_manager_factory import ServiceManagerFactory
from com.vmware.cis.tagging_client import (
    Category, CategoryModel, Tag, TagAssociation)
from com.vmware.vapi.std_client import DynamicID

class VMTagger:

    def __init__(self, user, password, host, skip_verification=True):
        self.user = user
        self.password = password
        self.host = host
        self.service_manager = ServiceManagerFactory.get_service_manager(self.host,
                                                         self.user,
                                                         self.password, skip_verification)
        self.tag_svc = Tag(self.service_manager.stub_config)
        self.tag_association = TagAssociation(self.service_manager.stub_config)


    '''Return value is vm_ids that were tagged.'''
    def tag_vms(self, vm_ids, tag_id):
        # Check whether tag with the id exists
        tags = self.tag_svc.list()
        found = tag_id in tags

        if not found:
            print 'Tag %s not found!' % tag_id
            return []
        tag = self.tag_svc.get(tag_id)
        
        output = []

        for vm in vm_ids:
            dynamic_id = DynamicID(type='VirtualMachine', id=vm)
            try:
                self.tag_association.attach(tag_id=tag.id, object_id=dynamic_id)
                print 'Tagged %s' % vm
            except Exception, e:
                print 'Unable to tag: %s, error: %s' % (vm, e)
            output.append(vm)
        return output
