# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource_py3 import ProxyResource


class Pool(ProxyResource):
    """Contains information about a pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar etag: The ETag of the resource, used for concurrency statements.
    :vartype etag: str
    :param display_name: The display name for the pool. The display name need
     not be unique and can contain any Unicode characters up to a maximum
     length of 1024.
    :type display_name: str
    :ivar last_modified: The last modified time of the pool. This is the last
     time at which the pool level data, such as the targetDedicatedNodes or
     autoScaleSettings, changed. It does not factor in node-level changes such
     as a compute node changing state.
    :vartype last_modified: datetime
    :ivar creation_time: The creation time of the pool.
    :vartype creation_time: datetime
    :ivar provisioning_state: The current state of the pool. Possible values
     include: 'Succeeded', 'Deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.batch.models.PoolProvisioningState
    :ivar provisioning_state_transition_time: The time at which the pool
     entered its current state.
    :vartype provisioning_state_transition_time: datetime
    :ivar allocation_state: Whether the pool is resizing. Possible values
     include: 'Steady', 'Resizing', 'Stopping'
    :vartype allocation_state: str or ~azure.mgmt.batch.models.AllocationState
    :ivar allocation_state_transition_time: The time at which the pool entered
     its current allocation state.
    :vartype allocation_state_transition_time: datetime
    :param vm_size: The size of virtual machines in the pool. All VMs in a
     pool are the same size. For information about available sizes of virtual
     machines for Cloud Services pools (pools created with
     cloudServiceConfiguration), see Sizes for Cloud Services
     (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/).
     Batch supports all Cloud Services VM sizes except ExtraSmall. For
     information about available VM sizes for pools using images from the
     Virtual Machines Marketplace (pools created with
     virtualMachineConfiguration) see Sizes for Virtual Machines (Linux)
     (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/)
     or Sizes for Virtual Machines (Windows)
     (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/).
     Batch supports all Azure VM sizes except STANDARD_A0 and those with
     premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
    :type vm_size: str
    :param deployment_configuration: This property describes how the pool
     nodes will be deployed - using Cloud Services or Virtual Machines. Using
     CloudServiceConfiguration specifies that the nodes should be creating
     using Azure Cloud Services (PaaS), while VirtualMachineConfiguration uses
     Azure Virtual Machines (IaaS).
    :type deployment_configuration:
     ~azure.mgmt.batch.models.DeploymentConfiguration
    :ivar current_dedicated_nodes: The number of compute nodes currently in
     the pool.
    :vartype current_dedicated_nodes: int
    :ivar current_low_priority_nodes: The number of low priority compute nodes
     currently in the pool.
    :vartype current_low_priority_nodes: int
    :param scale_settings: Settings which configure the number of nodes in the
     pool.
    :type scale_settings: ~azure.mgmt.batch.models.ScaleSettings
    :ivar auto_scale_run: The results and errors from the last execution of
     the autoscale formula. This property is set only if the pool automatically
     scales, i.e. autoScaleSettings are used.
    :vartype auto_scale_run: ~azure.mgmt.batch.models.AutoScaleRun
    :param inter_node_communication: Whether the pool permits direct
     communication between nodes. This imposes restrictions on which nodes can
     be assigned to the pool. Enabling this value can reduce the chance of the
     requested number of nodes to be allocated in the pool. If not specified,
     this value defaults to 'Disabled'. Possible values include: 'Enabled',
     'Disabled'
    :type inter_node_communication: str or
     ~azure.mgmt.batch.models.InterNodeCommunicationState
    :param network_configuration: The network configuration for the pool.
    :type network_configuration: ~azure.mgmt.batch.models.NetworkConfiguration
    :param max_tasks_per_node: The maximum number of tasks that can run
     concurrently on a single compute node in the pool. The default value is 1.
     The maximum value is the smaller of 4 times the number of cores of the
     vmSize of the pool or 256.
    :type max_tasks_per_node: int
    :param task_scheduling_policy: How tasks are distributed across compute
     nodes in a pool. If not specified, the default is spread.
    :type task_scheduling_policy:
     ~azure.mgmt.batch.models.TaskSchedulingPolicy
    :param user_accounts: The list of user accounts to be created on each node
     in the pool.
    :type user_accounts: list[~azure.mgmt.batch.models.UserAccount]
    :param metadata: A list of name-value pairs associated with the pool as
     metadata. The Batch service does not assign any meaning to metadata; it is
     solely for the use of user code.
    :type metadata: list[~azure.mgmt.batch.models.MetadataItem]
    :param start_task: A task specified to run on each compute node as it
     joins the pool. In an PATCH (update) operation, this property can be set
     to an empty object to remove the start task from the pool.
    :type start_task: ~azure.mgmt.batch.models.StartTask
    :param certificates: The list of certificates to be installed on each
     compute node in the pool. For Windows compute nodes, the Batch service
     installs the certificates to the specified certificate store and location.
     For Linux compute nodes, the certificates are stored in a directory inside
     the task working directory and an environment variable
     AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this
     location. For certificates with visibility of 'remoteUser', a 'certs'
     directory is created in the user's home directory (e.g.,
     /home/{user-name}/certs) and certificates are placed in that directory.
    :type certificates: list[~azure.mgmt.batch.models.CertificateReference]
    :param application_packages: The list of application packages to be
     installed on each compute node in the pool. Changes to application package
     references affect all new compute nodes joining the pool, but do not
     affect compute nodes that are already in the pool until they are rebooted
     or reimaged. There is a maximum of 10 application package references on
     any given pool.
    :type application_packages:
     list[~azure.mgmt.batch.models.ApplicationPackageReference]
    :param application_licenses: The list of application licenses the Batch
     service will make available on each compute node in the pool. The list of
     application licenses must be a subset of available Batch service
     application licenses. If a license is requested which is not supported,
     pool creation will fail.
    :type application_licenses: list[str]
    :ivar resize_operation_status: Contains details about the current or last
     completed resize operation.
    :vartype resize_operation_status:
     ~azure.mgmt.batch.models.ResizeOperationStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
        'last_modified': {'readonly': True},
        'creation_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'provisioning_state_transition_time': {'readonly': True},
        'allocation_state': {'readonly': True},
        'allocation_state_transition_time': {'readonly': True},
        'current_dedicated_nodes': {'readonly': True},
        'current_low_priority_nodes': {'readonly': True},
        'auto_scale_run': {'readonly': True},
        'resize_operation_status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'last_modified': {'key': 'properties.lastModified', 'type': 'iso-8601'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'PoolProvisioningState'},
        'provisioning_state_transition_time': {'key': 'properties.provisioningStateTransitionTime', 'type': 'iso-8601'},
        'allocation_state': {'key': 'properties.allocationState', 'type': 'AllocationState'},
        'allocation_state_transition_time': {'key': 'properties.allocationStateTransitionTime', 'type': 'iso-8601'},
        'vm_size': {'key': 'properties.vmSize', 'type': 'str'},
        'deployment_configuration': {'key': 'properties.deploymentConfiguration', 'type': 'DeploymentConfiguration'},
        'current_dedicated_nodes': {'key': 'properties.currentDedicatedNodes', 'type': 'int'},
        'current_low_priority_nodes': {'key': 'properties.currentLowPriorityNodes', 'type': 'int'},
        'scale_settings': {'key': 'properties.scaleSettings', 'type': 'ScaleSettings'},
        'auto_scale_run': {'key': 'properties.autoScaleRun', 'type': 'AutoScaleRun'},
        'inter_node_communication': {'key': 'properties.interNodeCommunication', 'type': 'InterNodeCommunicationState'},
        'network_configuration': {'key': 'properties.networkConfiguration', 'type': 'NetworkConfiguration'},
        'max_tasks_per_node': {'key': 'properties.maxTasksPerNode', 'type': 'int'},
        'task_scheduling_policy': {'key': 'properties.taskSchedulingPolicy', 'type': 'TaskSchedulingPolicy'},
        'user_accounts': {'key': 'properties.userAccounts', 'type': '[UserAccount]'},
        'metadata': {'key': 'properties.metadata', 'type': '[MetadataItem]'},
        'start_task': {'key': 'properties.startTask', 'type': 'StartTask'},
        'certificates': {'key': 'properties.certificates', 'type': '[CertificateReference]'},
        'application_packages': {'key': 'properties.applicationPackages', 'type': '[ApplicationPackageReference]'},
        'application_licenses': {'key': 'properties.applicationLicenses', 'type': '[str]'},
        'resize_operation_status': {'key': 'properties.resizeOperationStatus', 'type': 'ResizeOperationStatus'},
    }

    def __init__(self, *, display_name: str=None, vm_size: str=None, deployment_configuration=None, scale_settings=None, inter_node_communication=None, network_configuration=None, max_tasks_per_node: int=None, task_scheduling_policy=None, user_accounts=None, metadata=None, start_task=None, certificates=None, application_packages=None, application_licenses=None, **kwargs) -> None:
        super(Pool, self).__init__(**kwargs)
        self.display_name = display_name
        self.last_modified = None
        self.creation_time = None
        self.provisioning_state = None
        self.provisioning_state_transition_time = None
        self.allocation_state = None
        self.allocation_state_transition_time = None
        self.vm_size = vm_size
        self.deployment_configuration = deployment_configuration
        self.current_dedicated_nodes = None
        self.current_low_priority_nodes = None
        self.scale_settings = scale_settings
        self.auto_scale_run = None
        self.inter_node_communication = inter_node_communication
        self.network_configuration = network_configuration
        self.max_tasks_per_node = max_tasks_per_node
        self.task_scheduling_policy = task_scheduling_policy
        self.user_accounts = user_accounts
        self.metadata = metadata
        self.start_task = start_task
        self.certificates = certificates
        self.application_packages = application_packages
        self.application_licenses = application_licenses
        self.resize_operation_status = None
