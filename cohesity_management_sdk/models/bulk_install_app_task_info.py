# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BulkInstallAppTaskInfo(object):

    """Implementation of the 'BulkInstallAppTaskInfo' model.

    Parameters for a bulk install app task.

    Attributes:
        job_id (string): Job id of the task.
        num_machines_failed (int): Number of machines on which task is
            started.
        num_machines_passed (int): Number of machines on which task is
            started.
        num_machines_total (int): Number of machines on which task is started.
        registering_app (RegisteringAppEnum): Application being registered.
            This param is used to indicate the app for which the job is
            created. 'oracle' indicates that the job was created for oracle
            app. 'msSql' indicates that the job was created for msSql app.
            'physical' indicates that the job was created for physical
            machine.
        state (StateBulkInstallAppTaskInfoEnum): Current state of the task.
            This param is used to indicate the state of the job created by the
            bulk install app. 'started' indicates that the job has been
            started by the user. 'completed' indicates that the job has
            completed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_id": 'jobId',
        "num_machines_failed": 'numMachinesFailed',
        "num_machines_passed": 'numMachinesPassed',
        "num_machines_total": 'numMachinesTotal',
        "registering_app":'registeringApp',
        "state":'state'
    }

    def __init__(self,
                 job_id=None,
                 num_machines_failed=None,
                 num_machines_passed=None,
                 num_machines_total=None,
                 registering_app=None,
                 state=None):
        """Constructor for the BulkInstallAppTaskInfo class"""

        # Initialize members of the class
        self.job_id = job_id
        self.num_machines_failed = num_machines_failed
        self.num_machines_passed = num_machines_passed
        self.num_machines_total = num_machines_total
        self.registering_app = registering_app
        self.state = state

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        job_id = dictionary.get('jobId')
        num_machines_failed = dictionary.get('numMachinesFailed')
        num_machines_passed = dictionary.get('numMachinesPassed')
        num_machines_total = dictionary.get('numMachinesTotal')
        registering_app = dictionary.get('registeringApp')
        state = dictionary.get('state')

        # Return an object of this model
        return cls(job_id,
                   num_machines_failed,
                   num_machines_passed,
                   num_machines_total,
                   registering_app,
                   state)


