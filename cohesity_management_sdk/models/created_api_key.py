# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CreatedApiKey(object):

    """Implementation of the 'CreatedApiKey' model.

    Specifies a created API key.

    Attributes:
        created_time_msecs (int|long): Specifies the API key created time in
            milli seconds.
        created_user_sid (string): Specifies the user sid who created this API
            key.
        created_username (string): Specifies the username who created this API
            key.
        expiring_time_msecs (long|int): Specifies a time stamp when the API
            key will expire in milli seconds.
        id (string): Specifies the API key id.
        is_active (bool): Specifies if the API key is active. Only an active
            and not expired API key can be used for authentication.
        is_expired (bool): Specifies if the API key is expired. Expired API
            keys cannot be used for authentication.
        key (string): Specifies the created key.
        name (string): Specifies the API key name.
        owner_user_sid (string): Specifies the user sid who owns this API key.
        owner_username (string): Specifies the username who owns this API key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time_msecs":'createdTimeMsecs',
        "created_user_sid":'createdUserSid',
        "created_username":'createdUsername',
        "expiring_time_msecs":'expiringTimeMsecs',
        "id":'id',
        "is_active":'isActive',
        "is_expired":'isExpired',
        "key":'key',
        "name":'name',
        "owner_user_sid":'ownerUserSid',
        "owner_username":'ownerUsername'
    }

    def __init__(self,
                 created_time_msecs=None,
                 created_user_sid=None,
                 created_username=None,
                 expiring_time_msecs=None,
                 id=None,
                 is_active=None,
                 is_expired=None,
                 key=None,
                 name=None,
                 owner_user_sid=None,
                 owner_username=None):
        """Constructor for the CreatedApiKey class"""

        # Initialize members of the class
        self.created_time_msecs = created_time_msecs
        self.created_user_sid = created_user_sid
        self.created_username = created_username
        self.expiring_time_msecs = expiring_time_msecs
        self.id = id
        self.is_active = is_active
        self.is_expired = is_expired
        self.key =  key
        self.name = name
        self.owner_user_sid = owner_user_sid
        self.owner_username = owner_username


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
        created_time_msecs = dictionary.get('createdTimeMsecs')
        created_user_sid = dictionary.get('createdUserSid')
        created_username = dictionary.get('createdUsername')
        expiring_time_msecs = dictionary.get('expiringTimeMsecs')
        id = dictionary.get('id')
        is_active = dictionary.get('isActive')
        is_expired = dictionary.get('isExpired')
        key = dictionary.get('key')
        name = dictionary.get('name')
        owner_user_sid = dictionary.get('ownerUserSid')
        owner_username = dictionary.get('ownerUsername')

        # Return an object of this model
        return cls(created_time_msecs,
                   created_user_sid,
                   created_username,
                   expiring_time_msecs,
                   id,
                   is_active,
                   is_expired,
                   key,
                   name,
                   owner_user_sid,
                   owner_username)


