# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AppMetadata(object):

    """Implementation of the 'AppMetadata' model.

    AppMetadata provides metadata information about an application.


    Attributes:

        author (string): Specifies author of the app.
        created_date (string): Specifies date when the first version of the app
            was created.
        deployment_parameters (string): Deployment parameters required for the
            app launch.
        description (string): Specifies description about what app does.
        dev_version (string): Specifies version of the app provided by the
            developer.
        icon_image (string): Specifies application icon.
        last_modified_date (string): Specifies date when the app was last
            modified.
        name (string): Specifies name of the app.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "author":'author',
        "created_date":'createdDate',
        "deployment_parameters":'deploymentParameters',
        "description":'description',
        "dev_version":'devVersion',
        "icon_image":'iconImage',
        "last_modified_date":'lastModifiedDate',
        "name":'name',
    }
    def __init__(self,
                 author=None,
                 created_date=None,
                 deployment_parameters=None,
                 description=None,
                 dev_version=None,
                 icon_image=None,
                 last_modified_date=None,
                 name=None,
            ):

        """Constructor for the AppMetadata class"""

        # Initialize members of the class
        self.author = author
        self.created_date = created_date
        self.deployment_parameters = deployment_parameters
        self.description = description
        self.dev_version = dev_version
        self.icon_image = icon_image
        self.last_modified_date = last_modified_date
        self.name = name

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
        author = dictionary.get('author')
        created_date = dictionary.get('createdDate')
        deployment_parameters = dictionary.get('deploymentParameters')
        description = dictionary.get('description')
        dev_version = dictionary.get('devVersion')
        icon_image = dictionary.get('iconImage')
        last_modified_date = dictionary.get('lastModifiedDate')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            author,
            created_date,
            deployment_parameters,
            description,
            dev_version,
            icon_image,
            last_modified_date,
            name
)