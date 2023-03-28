# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AccessInfoListEnum(object):

    """Implementation of the 'AccessInfoList' enum.
    Specifies the access information. 'kFileReadData' indicates the right to
    read data from the file or named pipe. 'kFileWriteData' indicates the right
    to write data into the file or named pipe beyond the end of the file.
    'kFileAppendData' indicates the right to append data into the file or named
    pipe. 'kFileReadEa' indicates the right to read the extended attributes of
    the file or named pipe. 'kFileWriteEa' indicates the right to write or
    change the extended attributes to the file or named pipe. 'kFileExecute'
    indicates the right to delete entries within a directory.
    'kFileDeleteChild' indicates the right to execute the file.
    'kFileReadAttributes' indicates the right to read the attributes of the
    file. 'kFileWriteAttributes' indicates the right to change the attributes
    of the file. 'kDelete' indicates the right to delete the file.
    'kReadControl' indicates the right to read the security descriptor for the
    file or named pipe. 'kWriteDac' indicates the right to change the
    discretionary access control list (DACL) in the security descriptor for the
    file or named pipe. For the DACL data structure, see ACL in [MS-DTYP].
    'kWriteOwner' indicates the right to change the owner in the security
    descriptor for the file or named pipe. 'kSynchronize' is used only by SMB2
    clients. 'kAccessSystemSecurity' indicates the right to read or change the
    system access control list (SACL) in the security descriptor for the file
    or named pipe. For the SACL data structure, see ACL in [MS-DTYP].<42>
    'kMaximumAllowed' indicates that the client is requesting an open to the
    file with the highest level of access the client has on this file. If no
    access is granted for the client on this file, the server MUST fail the
    open with STATUS_ACCESS_DENIED. 'kGenericAll' indicates a request for all
    the access flags that are previously listed except kMaximumAllowed and
    kAccessSystemSecurity. 'kGenericExecute' indicates a request for the
    following combination of access flags listed above: kFileReadAttributes|
    kFileExecute| kSynchronize| kReadControl. 'kGenericWrite' indicates a
    request for the following combination of access flags listed above:
    kFileWriteData| kFileAppendData| kFileWriteAttributes| kFileWriteEa|
    kSynchronize| kReadControl. 'kGenericRead' indicates a request for the
    following combination of access flags listed above: kFileReadData|
    kFileReadAttributes| kFileReadEa| kSynchronize| kReadControl.


    Attributes:
        KFILEREADDATA: TODO: type description here.
        KFILEWRITEDATA: TODO: type description here.
        KFILEAPPENDDATA: TODO: type description here.
        KFILEREADEA: TODO: type description here.
        KFILEWRITEEA: TODO: type description here.
        KFILEEXECUTE: TODO: type description here.
        KFILEDELETECHILD: TODO: type description here.
        KFILEREADATTRIBUTES: TODO: type description here.
        KFILEWRITEATTRIBUTES: TODO: type description here.
        KDELETE: TODO: type description here.
        KREADCONTROL: TODO: type description here.
        KWRITEDAC: TODO: type description here.
        KWRITEOWNER: TODO: type description here.
        KSYNCHRONIZE: TODO: type description here.
        KACCESSSYSTEMSECURITY: TODO: type description here.
        KMAXIMUMALLOWED: TODO: type description here.
        KGENERICALL: TODO: type description here.
        KGENERICEXECUTE: TODO: type description here.
        KGENERICWRITE: TODO: type description here.
        KGENERICREAD: TODO: type description here.

    """

    KFILEREADDATA = 'kFileReadData'

    KFILEWRITEDATA = 'kFileWriteData'

    KFILEAPPENDDATA = 'kFileAppendData'

    KFILEREADEA = 'kFileReadEa'

    KFILEWRITEEA = 'kFileWriteEa'

    KFILEEXECUTE = 'kFileExecute'

    KFILEDELETECHILD = 'kFileDeleteChild'

    KFILEREADATTRIBUTES = 'kFileReadAttributes'

    KFILEWRITEATTRIBUTES = 'kFileWriteAttributes'

    KDELETE = 'kDelete'

    KREADCONTROL = 'kReadControl'

    KWRITEDAC = 'kWriteDac'

    KWRITEOWNER = 'kWriteOwner'

    KSYNCHRONIZE = 'kSynchronize'

    KACCESSSYSTEMSECURITY = 'kAccessSystemSecurity'

    KMAXIMUMALLOWED = 'kMaximumAllowed'

    KGENERICALL = 'kGenericAll'

    KGENERICEXECUTE = 'kGenericExecute'

    KGENERICWRITE = 'kGenericWrite'

    KGENERICREAD = 'kGenericRead'
