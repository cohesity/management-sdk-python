# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_object_restore_status_ad_attribute_restore_status
import cohesity_management_sdk.models.error_proto

class ADObjectRestoreStatus(object):

    """Implementation of the 'ADObjectRestoreStatus' model.

    TODO: type model description here.

    Attributes:
        dest_guid (string): Destination guid string of the AD object that is
            newly created on production AD corresponding to 'source_guid'. If
            the object was restored from production AD recycle Bin, this value
            can be empty or set to same value as 'source_guid'. If this value
            is non-empty and is different from source_guid, implying
            production AD object is a new object created in production AD as
            part of restore.
        object_flags (int): Object result flags of type ADObjectFlags.
        property_status_vec (list of
            ADObjectRestoreStatusADAttributeRestoreStatus): AD object
            attribute(property) restore status vector.
        source_guid (string): Source guid of AD object that was restored. This
            will not be empty. This is populated from the source of request
            argument.
        status (ErrorProto): TODO: type description here.
        timetaken_ms (int): Time taken in milliseconds to restore the
            individual object or attribute update. If this object restore was
            part of a batch, it shows the time taken once the operation was
            dispatched to AD for the object. This time can be useful in
            answering why some objects took long time to restore. Note that
            this time is not the elapsed time when the request was made from
            Magneto.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dest_guid":'destGuid',
        "object_flags":'objectFlags',
        "property_status_vec":'propertyStatusVec',
        "source_guid":'sourceGuid',
        "status":'status',
        "timetaken_ms":'timetakenMs'
    }

    def __init__(self,
                 dest_guid=None,
                 object_flags=None,
                 property_status_vec=None,
                 source_guid=None,
                 status=None,
                 timetaken_ms=None):
        """Constructor for the ADObjectRestoreStatus class"""

        # Initialize members of the class
        self.dest_guid = dest_guid
        self.object_flags = object_flags
        self.property_status_vec = property_status_vec
        self.source_guid = source_guid
        self.status = status
        self.timetaken_ms = timetaken_ms


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
        dest_guid = dictionary.get('destGuid')
        object_flags = dictionary.get('objectFlags')
        property_status_vec = None
        if dictionary.get('propertyStatusVec') != None:
            property_status_vec = list()
            for structure in dictionary.get('propertyStatusVec'):
                property_status_vec.append(cohesity_management_sdk.models.ad_object_restore_status_ad_attribute_restore_status.ADObjectRestoreStatusADAttributeRestoreStatus.from_dictionary(structure))
        source_guid = dictionary.get('sourceGuid')
        status = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('status')) if dictionary.get('status') else None
        timetaken_ms = dictionary.get('timetakenMs')

        # Return an object of this model
        return cls(dest_guid,
                   object_flags,
                   property_status_vec,
                   source_guid,
                   status,
                   timetaken_ms)


