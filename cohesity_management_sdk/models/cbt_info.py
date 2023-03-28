# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CbtInfo(object):

    """Implementation of the 'CbtInfo' model.

    Specifies information about the Cbt Driver associated with agent.


    Attributes:

        is_installed (bool): Specifies whether the cbt driver is installed or
            not.
        reboot_status (RebootStatusEnum): Specifies the reboot status of the
            host post cbt driver installation. Only applicable for volcbt
            driver. Specifies the reboot status of the source post volcbt
            driver installation. 'kRebooted' indicates the source has been
            rebooted post volcbt driver installation. 'kNeedsReboot' indicates
            the source has not been rebooted post volcbt driver installation.
            'kInternalError' indicates that there was an error while fetching
            reboot status from source.
        service_state (ServiceStateEnum): Specifies the status of the cbt
            driver. Specifies the service state of the cbt driver. 'kRunning'
            indicates the cbt driver is running. 'kStopped' indicates the
            service is stopped. 'kPaused' indicates the service is paused (it
            is a Windows-specific state). 'kUnknown' indicates the service with
            the specified name is not known on the system.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_installed":'isInstalled',
        "reboot_status":'rebootStatus',
        "service_state":'serviceState',
    }
    def __init__(self,
                 is_installed=None,
                 reboot_status=None,
                 service_state=None,
            ):

        """Constructor for the CbtInfo class"""

        # Initialize members of the class
        self.is_installed = is_installed
        self.reboot_status = reboot_status
        self.service_state = service_state

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
        is_installed = dictionary.get('isInstalled')
        reboot_status = dictionary.get('rebootStatus')
        service_state = dictionary.get('serviceState')

        # Return an object of this model
        return cls(
            is_installed,
            reboot_status,
            service_state
)