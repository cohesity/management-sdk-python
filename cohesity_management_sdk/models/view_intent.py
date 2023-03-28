# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ViewIntent(object):

    """Implementation of the 'ViewIntent' model.

    Specifies the Intent of the View.


    Attributes:

        template_id (long|int): Specifies the template Id from which the View
            is created.
        template_name (string): Specifies the template name from which the View
            is created.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "template_id":'TemplateId',
        "template_name":'TemplateName',
    }
    def __init__(self,
                 template_id=None,
                 template_name=None,
            ):

        """Constructor for the ViewIntent class"""

        # Initialize members of the class
        self.template_id = template_id
        self.template_name = template_name

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
        template_id = dictionary.get('TemplateId')
        template_name = dictionary.get('TemplateName')

        # Return an object of this model
        return cls(
            template_id,
            template_name
)