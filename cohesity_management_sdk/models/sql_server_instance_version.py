# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SQLServerInstanceVersion(object):

    """Implementation of the 'SQLServerInstanceVersion' model.

    Specifies the Server Instance Version.

    Attributes:
        build (int): Specfies the build.
        major_version (int): Specfies the major version.
        minor_version (int): Specfies the minor version.
        revision (int): Specfies the revision.
        version_string (string): Specfies the version string.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "build":'build',
        "major_version":'majorVersion',
        "minor_version":'minorVersion',
        "revision":'revision',
        "version_string":'versionString'
    }

    def __init__(self,
                 build=None,
                 major_version=None,
                 minor_version=None,
                 revision=None,
                 version_string=None):
        """Constructor for the SQLServerInstanceVersion class"""

        # Initialize members of the class
        self.build = build
        self.major_version = major_version
        self.minor_version = minor_version
        self.revision = revision
        self.version_string = version_string


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
        build = dictionary.get('build')
        major_version = dictionary.get('majorVersion')
        minor_version = dictionary.get('minorVersion')
        revision = dictionary.get('revision')
        version_string = dictionary.get('versionString')

        # Return an object of this model
        return cls(build,
                   major_version,
                   minor_version,
                   revision,
                   version_string)


