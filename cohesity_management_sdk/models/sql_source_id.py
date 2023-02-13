# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SqlSourceId(object):

    """Implementation of the 'SqlSourceId' model.

    Specifies a unique id for a SQL Protection Source.

    Attributes:
        created_date_msecs (long|int): Specifies a unique identifier generated
            from the date the database is created or renamed. Cohesity uses
            this identifier in combination with the databaseId to uniquely
            identify a database.
        database_id (long|int): Specifies a unique id of the database but only
            for the life of the database. SQL Server may reuse database ids.
            Cohesity uses the createDateMsecs in combination with this
            databaseId to uniquely identify a database.
        instance_id (list of int): Array of bytes that stores the SQL Server
            Instance id.  Specifies unique id for the SQL Server instance.
            This id does not change during the life of the instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_date_msecs":'createdDateMsecs',
        "database_id":'databaseId',
        "instance_id":'instanceId'
    }

    def __init__(self,
                 created_date_msecs=None,
                 database_id=None,
                 instance_id=None):
        """Constructor for the SqlSourceId class"""

        # Initialize members of the class
        self.created_date_msecs = created_date_msecs
        self.database_id = database_id
        self.instance_id = instance_id


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
        created_date_msecs = dictionary.get('createdDateMsecs')
        database_id = dictionary.get('databaseId')
        instance_id = dictionary.get('instanceId')

        # Return an object of this model
        return cls(created_date_msecs,
                   database_id,
                   instance_id)


