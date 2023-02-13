# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PaginationParameters(object):

    """Implementation of the 'PaginationParameters' model.

    Specifies the cursor based pagination parameters for Protection Source
    and
    its children. Pagination is supported at a given level within the
    Protection
    Source Hierarchy with the help of before or after cursors.
    A Cursor will always refer to a specific source within the source dataset
    but will be invalidated if the item is removed.

    Attributes:
        after_cursor_entity_id (long|int): Specifies the entity id starting
            from which the items are to be returned.
        before_cursor_entity_id (long|int): Specifies the entity id upto which
            the items are to be returned.
        node_id (long|int): Specifies the entity id for the Node at any level
            within the Source entity hierarchy whose children are to be
            paginated.
        page_size (long|int): Specifies the maximum number of entities to be
            returned within the page.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "after_cursor_entity_id":'afterCursorEntityId',
        "before_cursor_entity_id":'beforeCursorEntityId',
        "node_id":'nodeId',
        "page_size":'pageSize'
    }

    def __init__(self,
                 after_cursor_entity_id=None,
                 before_cursor_entity_id=None,
                 node_id=None,
                 page_size=None):
        """Constructor for the PaginationParameters class"""

        # Initialize members of the class
        self.after_cursor_entity_id = after_cursor_entity_id
        self.before_cursor_entity_id = before_cursor_entity_id
        self.node_id = node_id
        self.page_size = page_size


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
        after_cursor_entity_id = dictionary.get('afterCursorEntityId')
        before_cursor_entity_id = dictionary.get('beforeCursorEntityId')
        node_id = dictionary.get('nodeId')
        page_size = dictionary.get('pageSize')

        # Return an object of this model
        return cls(after_cursor_entity_id,
                   before_cursor_entity_id,
                   node_id,
                   page_size)


