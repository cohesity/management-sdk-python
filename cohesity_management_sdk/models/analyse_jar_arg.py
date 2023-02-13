# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AnalyseJarArg(object):

    """Implementation of the 'AnalyseJarArg' model.

    API to analyse a JAR file. This JAR may contain multiple mappers/reducers.
    Jar will be analysed and list of all mappers/reducers found in the jar
    will be returned.

    Attributes:
        jar_name (string): Name of the JAR to be analysed.
        jar_path (string): Path of the jar file.
        jar_relative_path (string): :TODO add description here.
        save_entities (bool): If this flag is true, then also save mapper and
            reducers in scribe.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "jar_name":'jarName',
        "jar_path":'jarPath',
        "jar_relative_path":'jarRelativePath',
        "save_entities":'saveEntities'
    }

    def __init__(self,
                 jar_name=None,
                 jar_path=None,
                 jar_relative_path=None,
                 save_entities=None):
        """Constructor for the AnalyseJarArg class"""

        # Initialize members of the class
        self.jar_name = jar_name
        self.jar_path = jar_path
        self.jar_relative_path = jar_relative_path
        self.save_entities = save_entities


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
        jar_name = dictionary.get('jarName')
        jar_path = dictionary.get('jarPath')
        jar_relative_path = dictionary.get('jarRelativePath')
        save_entities = dictionary.get('saveEntities')

        # Return an object of this model
        return cls(jar_name,
                   jar_path,
                   jar_relative_path,
                   save_entities)


