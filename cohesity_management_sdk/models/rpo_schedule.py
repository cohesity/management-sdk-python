# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RpoSchedule(object):

    """Implementation of the 'RpoSchedule' model.

    Specifies an RPO Schedule.

    Attributes:
        interval_unit (IntervalUnitEnum): Specifies an RPO policy interval
            unit which will be used along with the multiplier to calculate the
            interval for the RPO policy execution. this can be kHours, kDays,
            KWeeks, kMonths RPOIntervalUnit.  Specifies an RPO Schedule
            interval unit. kMinutes specifies that the rpo interval unit is
            hours. kHours specifies that the rpo interval unit is hours. kDays
            specifies that the rpo interval unit is days. kWeeks specifies
            that the rpo interval unit is weeks. kMonths specifies that the
            rpo interval unit is months.
        multiplier (long|int): Specifies the multiplier value to be used with
            the  RPO interval unit value.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interval_unit":'intervalUnit',
        "multiplier":'multiplier'
    }

    def __init__(self,
                 interval_unit=None,
                 multiplier=None):
        """Constructor for the RpoSchedule class"""

        # Initialize members of the class
        self.interval_unit = interval_unit
        self.multiplier = multiplier


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
        interval_unit = dictionary.get('intervalUnit')
        multiplier = dictionary.get('multiplier')

        # Return an object of this model
        return cls(interval_unit,
                   multiplier)


