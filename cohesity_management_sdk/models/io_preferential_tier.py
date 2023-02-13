# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IoPreferentialTier(object):

    """Implementation of the 'IoPreferentialTier' model.

    Specifies the preferred storage tier for IO operations.

    Attributes:
        apollo_io_preferential_tier (list of ApolloIOPreferentialTierEnum):
            Specifies the preferred storage tier used by Apollo as its working
            directory.
        apollo_wal_io_preferential_tier (list of
            ApolloWalIOPreferentialTierEnum): Specifies the preferred storage
            tier used by Apollo as its actions WAL.
        athena_io_preferential_tier (list of AthenaIOPreferentialTierEnum):
            Specifies the list of perferred storage tiers used by Athena.
        athena_slower_io_preferential_tier (list of
            AthenaSlowerIOPreferentialTierEnum): Specifies the list of
            perferred storage tiers used by Athena for slower storage.
        down_tier_usage_percent_thresholds (list of int): Specifies the usage
            percentage thresholds for the correponding storage tier.
        groot_io_preferential_tier (list of GrootIOPreferentialTierEnum):
            Specifies the preferred storage tier used by Groot as its working
            directory.
        hydra_downtier_io_preferential_tier (list of
            HydraDowntierIOPreferentialTierEnum): Specifies the list of
            perferred storage tiers used by Hydra for offloading.
        hydra_io_preferential_tier (list of HydraIOPreferentialTierEnum):
            Specifies the list of perferred storage tiers used by Hydra.
        librarian_io_preferential_tier (list of
            LibrarianIOPreferentialTierEnum): Specifies the list of perferred
            storage tiers used by librarian.
        random_io_preferential_tier (list of RandomIOPreferentialTierEnum):
            Specifies the order of perferred storage tiers for random IO
            operations.
        scribe_io_preferential_tier (list of ScribeIOPreferentialTierEnum):
            Specifies the list of perferred storage tiers used by Scribe.
        sequential_io_preferential_tier (list of
            SequentialIOPreferentialTierEnum): Specifies the preferred storage
            tier for sequential IO operations.
        yoda_io_preferential_tier (list of YodaIOPreferentialTierEnum):
            Specifies the list of perferred storage tiers used by Yoda.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "apollo_io_preferential_tier":'apolloIOPreferentialTier',
        "apollo_wal_io_preferential_tier":'apolloWalIOPreferentialTier',
        "athena_io_preferential_tier":'athenaIOPreferentialTier',
        "athena_slower_io_preferential_tier":'athenaSlowerIOPreferentialTier',
        "down_tier_usage_percent_thresholds":'downTierUsagePercentThresholds',
        "groot_io_preferential_tier":'grootIOPreferentialTier',
        "hydra_downtier_io_preferential_tier":'hydraDowntierIOPreferentialTier',
        "hydra_io_preferential_tier":'hydraIOPreferentialTier',
        "librarian_io_preferential_tier":'librarianIOPreferentialTier',
        "random_io_preferential_tier":'randomIOPreferentialTier',
        "scribe_io_preferential_tier":'scribeIOPreferentialTier',
        "sequential_io_preferential_tier":'sequentialIOPreferentialTier',
        "yoda_io_preferential_tier":'yodaIOPreferentialTier'
    }

    def __init__(self,
                 apollo_io_preferential_tier=None,
                 apollo_wal_io_preferential_tier=None,
                 athena_io_preferential_tier=None,
                 athena_slower_io_preferential_tier=None,
                 down_tier_usage_percent_thresholds=None,
                 groot_io_preferential_tier=None,
                 hydra_downtier_io_preferential_tier=None,
                 hydra_io_preferential_tier=None,
                 librarian_io_preferential_tier=None,
                 random_io_preferential_tier=None,
                 scribe_io_preferential_tier=None,
                 sequential_io_preferential_tier=None,
                 yoda_io_preferential_tier=None):
        """Constructor for the IoPreferentialTier class"""

        # Initialize members of the class
        self.apollo_io_preferential_tier = apollo_io_preferential_tier
        self.apollo_wal_io_preferential_tier = apollo_wal_io_preferential_tier
        self.athena_io_preferential_tier = athena_io_preferential_tier
        self.athena_slower_io_preferential_tier = athena_slower_io_preferential_tier
        self.down_tier_usage_percent_thresholds = down_tier_usage_percent_thresholds
        self.groot_io_preferential_tier = groot_io_preferential_tier
        self.hydra_downtier_io_preferential_tier = hydra_downtier_io_preferential_tier
        self.hydra_io_preferential_tier = hydra_io_preferential_tier
        self.librarian_io_preferential_tier = librarian_io_preferential_tier
        self.random_io_preferential_tier = random_io_preferential_tier
        self.scribe_io_preferential_tier = scribe_io_preferential_tier
        self.sequential_io_preferential_tier = sequential_io_preferential_tier
        self.yoda_io_preferential_tier = yoda_io_preferential_tier


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
        apollo_io_preferential_tier = dictionary.get('apolloIOPreferentialTier')
        apollo_wal_io_preferential_tier = dictionary.get('apolloWalIOPreferentialTier')
        athena_io_preferential_tier = dictionary.get('athenaIOPreferentialTier')
        athena_slower_io_preferential_tier = dictionary.get('athenaSlowerIOPreferentialTier')
        down_tier_usage_percent_thresholds = dictionary.get('downTierUsagePercentThresholds')
        groot_io_preferential_tier = dictionary.get('grootIOPreferentialTier')
        hydra_downtier_io_preferential_tier = dictionary.get('hydraDowntierIOPreferentialTier')
        hydra_io_preferential_tier = dictionary.get('hydraIOPreferentialTier')
        librarian_io_preferential_tier = dictionary.get('librarianIOPreferentialTier')
        random_io_preferential_tier = dictionary.get('randomIOPreferentialTier')
        scribe_io_preferential_tier = dictionary.get('scribeIOPreferentialTier')
        sequential_io_preferential_tier = dictionary.get('sequentialIOPreferentialTier')
        yoda_io_preferential_tier = dictionary.get('yodaIOPreferentialTier')

        # Return an object of this model
        return cls(apollo_io_preferential_tier,
                   apollo_wal_io_preferential_tier,
                   athena_io_preferential_tier,
                   athena_slower_io_preferential_tier,
                   down_tier_usage_percent_thresholds,
                   groot_io_preferential_tier,
                   hydra_downtier_io_preferential_tier,
                   hydra_io_preferential_tier,
                   librarian_io_preferential_tier,
                   random_io_preferential_tier,
                   scribe_io_preferential_tier,
                   sequential_io_preferential_tier,
                   yoda_io_preferential_tier)


