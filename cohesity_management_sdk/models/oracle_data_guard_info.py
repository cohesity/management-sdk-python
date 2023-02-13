# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OracleDataGuardInfo(object):

    """Implementation of the 'OracleDataGuardInfo' model.

    Specifies information about the Database in Oracle DataGuard
    configuration.
    Data GUard provides a comprehensive set of services that create, maintain,
    and monitor one or more standby databases to enable production Oracle
    databases to survive disasters and data corruptions. Data Guard maintains
    these standby databases as transactionally consistent copies of the
    production databases.

    Attributes:
        role (RoleOracleDataGuardInfoEnum): Specifies the role of the
            DataGuard database.
            Specifies the role of the DataGuard database.

            A Data Guard configuration contains one production database, also
            referred to as the primary database, that functions in the primary
            role.
            The primary database can be either a single-instance Oracle
            database or an Oracle Real Application Clusters database.

            A standby database is a transactionally consistent copy of the
            primary database. Similar to a primary database, a standby
            database can be either a single-instance Oracle database or an
            Oracle Real Application Clusters database.
            'kPrimary' indicates that the current database is primary
            database.
            'kStandby' indicates that the current database is standby
            database.
        mtype (TypeOracleDataGuardInfoEnum): Specifies the type of standby
            database. Specifies the type of standby database. 'kPhysical'
            indicates that the current database provides a physically
            identical copy of the primary database, with on disk structures
            identical to the primary database on a block-for-block basis. It
            is kept synchronized with the primary database, though Redo Apply,
            which recovers the redo data received from the primary database
            and applies the redo to the physical standby database. 'kLogical'
            indicates that the current database provides the same logical
            information as the production database, although the physical
            structure can be different. It is kept synchronized with the
            primary database thorugh SQL Apply, which transforms the data in
            the redo received from the primary database into SQL statements
            and then executing the SQL statements on the standby database.
            'kSnapshot' indicates that the current database is a fully
            updateable standby created by converting a physical standby
            database into a snasphot standby database. It receives and
            archives but does not apply redo data from a primary database.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "role":'role',
        "mtype":'type'
    }

    def __init__(self,
                 role=None,
                 mtype=None):
        """Constructor for the OracleDataGuardInfo class"""

        # Initialize members of the class
        self.role = role
        self.mtype = mtype


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
        role = dictionary.get('role')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(role, mtype)


