# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AdObjectRestoreParameters(object):

    """Implementation of the 'AdObjectRestoreParameters' model.

    AdObjectRestoreParameters are the parameters to restore AD objects from
    recycle bin or from a mounted AD snapshot database.

    Attributes:
        change_password_on_next_logon (bool): Specifies the option for AD
            'user' type of objects to change password when they next logon.
        leave_state_disabled (bool): Specifies the option to leave the
            restored object in disabled state for AD 'account' type of objects
            that support disabled state so that admin can do manual inspection
            before enabling the account. This property has no effect when
            restoring object from recycle bin. 'User' and 'Computer' are AD
            account types having enable/disable option.
        object_guids (list of string): Specifies the array of AD object guids
            to restore either from recycle bin or from AD snapshot. The guid
            should not exist in production AD. If it exits, then kDuplicate
            error is output in status.
        organization_unit_path (string): Specifies the Distinguished name(DN)
            of the target Organization Unit (OU) to restore non-OU object.
            This can be empty, in which case objects are restored to their
            original OU. The 'credential' specified must have privileges to
            add objects to this OU. Example:
            'OU=SJC,OU=EngOU,DC=contoso,DC=com'. This parameter is ignored for
            OU objects.
        password (string): Specifies the password for restoring user type
            objects (user, inetOrgPerson or organizationalPerson LDAP classes)
            that is returned in search result with 'kRestorePasswordRequired'
            flag, an initial password is required. The password is UTF8 string
            encoded in base64 format. Password cannot be empty and must
            satisfy production AD password complexity. If
            'kFromDestRecycleBinIfFound' is true and the user is restored from
            production AD recycle bin, password will not be changed and the
            restored user retains their original password. For non-user type
            objects, this password value is ignored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "change_password_on_next_logon":'changePasswordOnNextLogon',
        "leave_state_disabled":'leaveStateDisabled',
        "object_guids":'objectGuids',
        "organization_unit_path":'organizationUnitPath',
        "password":'password'
    }

    def __init__(self,
                 change_password_on_next_logon=None,
                 leave_state_disabled=None,
                 object_guids=None,
                 organization_unit_path=None,
                 password=None):
        """Constructor for the AdObjectRestoreParameters class"""

        # Initialize members of the class
        self.change_password_on_next_logon = change_password_on_next_logon
        self.leave_state_disabled = leave_state_disabled
        self.object_guids = object_guids
        self.organization_unit_path = organization_unit_path
        self.password = password


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
        change_password_on_next_logon = dictionary.get('changePasswordOnNextLogon')
        leave_state_disabled = dictionary.get('leaveStateDisabled')
        object_guids = dictionary.get('objectGuids')
        organization_unit_path = dictionary.get('organizationUnitPath')
        password = dictionary.get('password')

        # Return an object of this model
        return cls(change_password_on_next_logon,
                   leave_state_disabled,
                   object_guids,
                   organization_unit_path,
                   password)


