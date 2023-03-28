# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_transfer_info_private_network_info


class DataTransferInfo(object):

    """Implementation of the 'DataTransferInfo' model.

    This proto contains information of the network which will be used at the
    source side for data transfer from the source to the Cohesity cluster.
    Currently, this is populated only in case of Native Backup/Restore of Azure
    Managed VMs.


    Attributes:

        is_private_network (bool): Whether to use private network or public
            network.
        private_network_info_vec (list of DataTransferInfo_PrivateNetworkInfo):
            Information required to create endpoints in private networks for
            all the regions whose VMs are getting protected.
        use_protection_job_info (bool): Whether to use private network info
            which was used in backup of VMs. This should be populated only for
            restore job. is_private_network should be true if this is set and
            its corresponding backup job should also have is_private_network to
            be true.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_private_network":'isPrivateNetwork',
        "private_network_info_vec":'privateNetworkInfoVec',
        "use_protection_job_info":'useProtectionJobInfo',
    }
    def __init__(self,
                 is_private_network=None,
                 private_network_info_vec=None,
                 use_protection_job_info=None,
            ):

        """Constructor for the DataTransferInfo class"""

        # Initialize members of the class
        self.is_private_network = is_private_network
        self.private_network_info_vec = private_network_info_vec
        self.use_protection_job_info = use_protection_job_info

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
        is_private_network = dictionary.get('isPrivateNetwork')
        private_network_info_vec = None
        if dictionary.get('privateNetworkInfoVec') != None:
            private_network_info_vec = list()
            for structure in dictionary.get('privateNetworkInfoVec'):
                private_network_info_vec.append(cohesity_management_sdk.models.data_transfer_info_private_network_info.DataTransferInfo_PrivateNetworkInfo.from_dictionary(structure))
        use_protection_job_info = dictionary.get('useProtectionJobInfo')

        # Return an object of this model
        return cls(
            is_private_network,
            private_network_info_vec,
            use_protection_job_info
)