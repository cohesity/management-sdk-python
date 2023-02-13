# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class KubernetesTypeEnum(object):

    """Implementation of the 'KubernetesType' enum.

    Specifies the entity type if the environment is kKubernetes.
    overrideDescription: true
    Specifies the type of a Kubernetes Protection Source.
    'kCluster' indicates a Kubernetes Cluster.
    'kNamespace' indicates a namespace in a Kubernetes Cluster.
    'kService' indicates a service running on a Kubernetes Cluster.

    Attributes:
        KCLUSTER: TODO: type description here.
        KNAMESPACE: TODO: type description here.
        KSERVICE: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KNAMESPACE = 'kNamespace'

    KSERVICE = 'kService'

