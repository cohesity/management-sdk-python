# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SmbActiveOpen(object):

    """Implementation of the 'SmbActiveOpen' model.

    Specifies an active open of an SMB file, its access and sharing
    information.

    Attributes:
        access_info_list (list of AccessInfoListEnum): Specifies the access
            information. 'kFileReadData' indicates the right to read data from
            the file or named pipe. 'kFileWriteData' indicates the right to
            write data into the file or named pipe beyond the end of the file.
            'kFileAppendData' indicates the right to append data into the file
            or named pipe. 'kFileReadEa' indicates the right to read the
            extended attributes of the file or named pipe. 'kFileWriteEa'
            indicates the right to write or change the extended attributes to
            the file or named pipe. 'kFileExecute' indicates the right to
            delete entries within a directory. 'kFileDeleteChild' indicates
            the right to execute the file. 'kFileReadAttributes' indicates the
            right to read the attributes of the file. 'kFileWriteAttributes'
            indicates the right to change the attributes of the file.
            'kDelete' indicates the right to delete the file. 'kReadControl'
            indicates the right to read the security descriptor for the file
            or named pipe. 'kWriteDac' indicates the right to change the
            discretionary access control list (DACL) in the security
            descriptor for the file or named pipe. For the DACL data
            structure, see ACL in [MS-DTYP]. 'kWriteOwner' indicates the right
            to change the owner in the security descriptor for the file or
            named pipe. 'kSynchronize' is used only by SMB2 clients.
            'kAccessSystemSecurity' indicates the right to read or change the
            system access control list (SACL) in the security descriptor for
            the file or named pipe. For the SACL data structure, see ACL in
            [MS-DTYP].<42> 'kMaximumAllowed' indicates that the client is
            requesting an open to the file with the highest level of access
            the client has on this file. If no access is granted for the
            client on this file, the server MUST fail the open with
            STATUS_ACCESS_DENIED. 'kGenericAll' indicates a request for all
            the access flags that are previously listed except kMaximumAllowed
            and kAccessSystemSecurity. 'kGenericExecute' indicates a request
            for the following combination of access flags listed above:
            kFileReadAttributes| kFileExecute| kSynchronize| kReadControl.
            'kGenericWrite' indicates a request for the following combination
            of access flags listed above: kFileWriteData| kFileAppendData|
            kFileWriteAttributes| kFileWriteEa| kSynchronize| kReadControl.
            'kGenericRead' indicates a request for the following combination
            of access flags listed above: kFileReadData| kFileReadAttributes|
            kFileReadEa| kSynchronize| kReadControl.
        open_id (long|int): Specifies the id of the active open.
        others_can_delete (bool): Specifies whether others are allowed to
            delete.
        others_can_read (bool): Specifies whether others are allowed to read.
        others_can_write (bool): Specifies whether others are allowed to
            write.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_info_list":'accessInfoList',
        "open_id":'openId',
        "others_can_delete":'othersCanDelete',
        "others_can_read":'othersCanRead',
        "others_can_write":'othersCanWrite'
    }

    def __init__(self,
                 access_info_list=None,
                 open_id=None,
                 others_can_delete=None,
                 others_can_read=None,
                 others_can_write=None):
        """Constructor for the SmbActiveOpen class"""

        # Initialize members of the class
        self.access_info_list = access_info_list
        self.open_id = open_id
        self.others_can_delete = others_can_delete
        self.others_can_read = others_can_read
        self.others_can_write = others_can_write


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
        access_info_list = dictionary.get('accessInfoList')
        open_id = dictionary.get('openId')
        others_can_delete = dictionary.get('othersCanDelete')
        others_can_read = dictionary.get('othersCanRead')
        others_can_write = dictionary.get('othersCanWrite')

        # Return an object of this model
        return cls(access_info_list,
                   open_id,
                   others_can_delete,
                   others_can_read,
                   others_can_write)


