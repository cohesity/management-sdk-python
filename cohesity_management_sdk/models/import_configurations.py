# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ImportConfigurations(object):

    """Implementation of the 'ImportConfigurations' model.

    ImportConfigurations struct used for ImportConfig endpoint. This is the
    form of the request.


    Attributes:

        active_directories (list of string): Selective import of active
            directories.
        all (list of string): List of which entities to import all.
        clusters (list of long|int): Selective import certain cluster.
        file (string): File is the config file.
        groups (list of string): Selective import certain groups.
        partitions (list of long|int): Selective import of Partition.
        principal_sources (list of string): Selective import of principal
            sources.
        protection_jobs (list of long|int): Selective import of protection
            jobs.
        protection_policies (list of string): Selective import of protection
            policies.
        protection_sources (list of long|int): Selective import of protection
            sources.
        remote_clusters (list of long|int): Selective import certain remote
            clusters.
        roles (list of string): Selective import certain roles (by username).
        sql (list of long|int): Selective import of sql.
        users (list of string): Selective import certain users.
        vaults (list of long|int): Selective import certain vaults.
        view_boxes (list of long|int): Selective import certain Storage Domains
            (View Boxes).
        views (list of long|int): Selective import of views.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "active_directories":'activeDirectories',
        "all":'all',
        "clusters":'clusters',
        "file":'file',
        "groups":'groups',
        "partitions":'partitions',
        "principal_sources":'principalSources',
        "protection_jobs":'protectionJobs',
        "protection_policies":'protectionPolicies',
        "protection_sources":'protectionSources',
        "remote_clusters":'remoteClusters',
        "roles":'roles',
        "sql":'sql',
        "users":'users',
        "vaults":'vaults',
        "view_boxes":'viewBoxes',
        "views":'views',
    }
    def __init__(self,
                 active_directories=None,
                 all=None,
                 clusters=None,
                 file=None,
                 groups=None,
                 partitions=None,
                 principal_sources=None,
                 protection_jobs=None,
                 protection_policies=None,
                 protection_sources=None,
                 remote_clusters=None,
                 roles=None,
                 sql=None,
                 users=None,
                 vaults=None,
                 view_boxes=None,
                 views=None,
            ):

        """Constructor for the ImportConfigurations class"""

        # Initialize members of the class
        self.active_directories = active_directories
        self.all = all
        self.clusters = clusters
        self.file = file
        self.groups = groups
        self.partitions = partitions
        self.principal_sources = principal_sources
        self.protection_jobs = protection_jobs
        self.protection_policies = protection_policies
        self.protection_sources = protection_sources
        self.remote_clusters = remote_clusters
        self.roles = roles
        self.sql = sql
        self.users = users
        self.vaults = vaults
        self.view_boxes = view_boxes
        self.views = views

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
        active_directories = dictionary.get("activeDirectories")
        all = dictionary.get("all")
        clusters = dictionary.get("clusters")
        file = dictionary.get('file')
        groups = dictionary.get("groups")
        partitions = dictionary.get("partitions")
        principal_sources = dictionary.get("principalSources")
        protection_jobs = dictionary.get("protectionJobs")
        protection_policies = dictionary.get("protectionPolicies")
        protection_sources = dictionary.get("protectionSources")
        remote_clusters = dictionary.get("remoteClusters")
        roles = dictionary.get("roles")
        sql = dictionary.get("sql")
        users = dictionary.get("users")
        vaults = dictionary.get("vaults")
        view_boxes = dictionary.get("viewBoxes")
        views = dictionary.get("views")

        # Return an object of this model
        return cls(
            active_directories,
            all,
            clusters,
            file,
            groups,
            partitions,
            principal_sources,
            protection_jobs,
            protection_policies,
            protection_sources,
            remote_clusters,
            roles,
            sql,
            users,
            vaults,
            view_boxes,
            views
)