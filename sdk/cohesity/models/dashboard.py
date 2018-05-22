# coding: utf-8

"""
    Cohesity REST API

    This API provides operations for interfacing with the Cohesity Cluster. NOTE: To view the documentation on the responses, click 'Model' next to 'Example Value' and keep clicking to expand the hierarchy.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Dashboard(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, audit_logs=None, cluster_id=None, health=None, iops=None, job_runs=None, protected_objects=None, protection=None, recoveries=None, storage_efficiency=None, throughput=None):
        """
        Dashboard - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'audit_logs': 'AuditLogsTile',
            'cluster_id': 'int',
            'health': 'HealthTile',
            'iops': 'IopsTile',
            'job_runs': 'JobRunsTile',
            'protected_objects': 'ProtectedObjectsTile',
            'protection': 'ProtectionTile',
            'recoveries': 'RecoveriesTile',
            'storage_efficiency': 'StorageEfficiencyTile',
            'throughput': 'ThroughputTile'
        }

        self.attribute_map = {
            'audit_logs': 'auditLogs',
            'cluster_id': 'clusterId',
            'health': 'health',
            'iops': 'iops',
            'job_runs': 'jobRuns',
            'protected_objects': 'protectedObjects',
            'protection': 'protection',
            'recoveries': 'recoveries',
            'storage_efficiency': 'storageEfficiency',
            'throughput': 'throughput'
        }

        self._audit_logs = audit_logs
        self._cluster_id = cluster_id
        self._health = health
        self._iops = iops
        self._job_runs = job_runs
        self._protected_objects = protected_objects
        self._protection = protection
        self._recoveries = recoveries
        self._storage_efficiency = storage_efficiency
        self._throughput = throughput

    @property
    def audit_logs(self):
        """
        Gets the audit_logs of this Dashboard.
        Audit Logs.

        :return: The audit_logs of this Dashboard.
        :rtype: AuditLogsTile
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """
        Sets the audit_logs of this Dashboard.
        Audit Logs.

        :param audit_logs: The audit_logs of this Dashboard.
        :type: AuditLogsTile
        """

        self._audit_logs = audit_logs

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this Dashboard.
        Id of the cluster for which dashboard is given.

        :return: The cluster_id of this Dashboard.
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this Dashboard.
        Id of the cluster for which dashboard is given.

        :param cluster_id: The cluster_id of this Dashboard.
        :type: int
        """

        self._cluster_id = cluster_id

    @property
    def health(self):
        """
        Gets the health of this Dashboard.
        Cluster Health and alerts.

        :return: The health of this Dashboard.
        :rtype: HealthTile
        """
        return self._health

    @health.setter
    def health(self, health):
        """
        Sets the health of this Dashboard.
        Cluster Health and alerts.

        :param health: The health of this Dashboard.
        :type: HealthTile
        """

        self._health = health

    @property
    def iops(self):
        """
        Gets the iops of this Dashboard.
        IOPs.

        :return: The iops of this Dashboard.
        :rtype: IopsTile
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """
        Sets the iops of this Dashboard.
        IOPs.

        :param iops: The iops of this Dashboard.
        :type: IopsTile
        """

        self._iops = iops

    @property
    def job_runs(self):
        """
        Gets the job_runs of this Dashboard.
        Protection Job Runs.

        :return: The job_runs of this Dashboard.
        :rtype: JobRunsTile
        """
        return self._job_runs

    @job_runs.setter
    def job_runs(self, job_runs):
        """
        Sets the job_runs of this Dashboard.
        Protection Job Runs.

        :param job_runs: The job_runs of this Dashboard.
        :type: JobRunsTile
        """

        self._job_runs = job_runs

    @property
    def protected_objects(self):
        """
        Gets the protected_objects of this Dashboard.
        ProtectedObjects related stats.

        :return: The protected_objects of this Dashboard.
        :rtype: ProtectedObjectsTile
        """
        return self._protected_objects

    @protected_objects.setter
    def protected_objects(self, protected_objects):
        """
        Sets the protected_objects of this Dashboard.
        ProtectedObjects related stats.

        :param protected_objects: The protected_objects of this Dashboard.
        :type: ProtectedObjectsTile
        """

        self._protected_objects = protected_objects

    @property
    def protection(self):
        """
        Gets the protection of this Dashboard.
        Protection related stats.

        :return: The protection of this Dashboard.
        :rtype: ProtectionTile
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """
        Sets the protection of this Dashboard.
        Protection related stats.

        :param protection: The protection of this Dashboard.
        :type: ProtectionTile
        """

        self._protection = protection

    @property
    def recoveries(self):
        """
        Gets the recoveries of this Dashboard.
        Recoveries related stats.

        :return: The recoveries of this Dashboard.
        :rtype: RecoveriesTile
        """
        return self._recoveries

    @recoveries.setter
    def recoveries(self, recoveries):
        """
        Sets the recoveries of this Dashboard.
        Recoveries related stats.

        :param recoveries: The recoveries of this Dashboard.
        :type: RecoveriesTile
        """

        self._recoveries = recoveries

    @property
    def storage_efficiency(self):
        """
        Gets the storage_efficiency of this Dashboard.
        Storage efficiency stats.

        :return: The storage_efficiency of this Dashboard.
        :rtype: StorageEfficiencyTile
        """
        return self._storage_efficiency

    @storage_efficiency.setter
    def storage_efficiency(self, storage_efficiency):
        """
        Sets the storage_efficiency of this Dashboard.
        Storage efficiency stats.

        :param storage_efficiency: The storage_efficiency of this Dashboard.
        :type: StorageEfficiencyTile
        """

        self._storage_efficiency = storage_efficiency

    @property
    def throughput(self):
        """
        Gets the throughput of this Dashboard.
        Throughput.

        :return: The throughput of this Dashboard.
        :rtype: ThroughputTile
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """
        Sets the throughput of this Dashboard.
        Throughput.

        :param throughput: The throughput of this Dashboard.
        :type: ThroughputTile
        """

        self._throughput = throughput

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
