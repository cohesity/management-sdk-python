# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HostSettingsCheckResult(object):

    """Implementation of the 'HostSettingsCheckResult' model.

    Specifies the result of various checks performed internally on host.

    Attributes:
        check_type (CheckTypeEnum): Specifies the type of the check internally
            performed. Specifies the type of the host check performed
            internally. 'kIsAgentPortAccessible' indicates the check for agent
            port access. 'kIsAgentRunning' indicates the status for the
            Cohesity agent service. 'kIsSQLWriterRunningCheck' indicates the
            status for SQLWriter service. 'kAreSQLInstancesRunning' indicates
            the run status for for all the SQL instances in the host.
            'kCheckServiceLoginsConfig' checks the privileges and sysadmin
            status of the logins used by the SQL instance services, Cohesity
            agent service and the SQLWriter service. 'kCheckSQLFCIVIP' checks
            whether the SQL FCI is registered with a valid VIP or FQDN.
        result_type (ResultTypeEnum): Specifies the type of the result
            returned after performing the internal host check. Specifies the
            type of the host check result performed internally. 'kPass'
            indicates that the respective check was successful. 'kFail'
            indicates that the respective check failed as some mandatory
            setting is not met 'kWarning' indicates that the respective check
            has warning as certain non-mandatory setting is not met.
        user_message (string): Specifies a descriptive message for
            failed/warning types.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "check_type":'checkType',
        "result_type":'resultType',
        "user_message":'userMessage'
    }

    def __init__(self,
                 check_type=None,
                 result_type=None,
                 user_message=None):
        """Constructor for the HostSettingsCheckResult class"""

        # Initialize members of the class
        self.check_type = check_type
        self.result_type = result_type
        self.user_message = user_message


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
        check_type = dictionary.get('checkType')
        result_type = dictionary.get('resultType')
        user_message = dictionary.get('userMessage')

        # Return an object of this model
        return cls(check_type,
                   result_type,
                   user_message)


