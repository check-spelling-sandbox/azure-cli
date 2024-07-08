# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "servicebus namespace update",
)
class Update(AAZCommand):
    """Update a service namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.

    :example: Updates a Service Bus Namespace
        az servicebus namespace update --resource-group myresourcegroup --name mynamespace --tags tag=value
        az az servicebus namespace update --name mynamespace --resource-group myresourcegroup --sku Basic
    """

    _aaz_info = {
        "version": "2022-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.servicebus/namespaces/{}", "2022-10-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.namespace_name = AAZStrArg(
            options=["-n", "--name", "--namespace-name"],
            help="The namespace name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="The resourceGroup name",
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Parameters",
            help="Properties of BYOK Identity description",
            nullable=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags",
            nullable=True,
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity.",
            nullable=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="Properties for User Assigned Identities",
            nullable=True,
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.alternate_name = AAZStrArg(
            options=["--alternate-name"],
            arg_group="Properties",
            help="Alternate name for namespace",
            nullable=True,
        )
        _args_schema.disable_local_auth = AAZBoolArg(
            options=["--disable-local-auth"],
            arg_group="Properties",
            help="This property disables SAS authentication for the Service Bus namespace.",
            nullable=True,
        )
        _args_schema.encryption = AAZObjectArg(
            options=["--encryption"],
            arg_group="Properties",
            help="Properties of BYOK Encryption description",
            nullable=True,
        )
        _args_schema.minimum_tls_version = AAZStrArg(
            options=["--minimum-tls-version"],
            arg_group="Properties",
            help="The minimum TLS version for the cluster to support, e.g. '1.2'",
            nullable=True,
            enum={"1.0": "1.0", "1.1": "1.1", "1.2": "1.2"},
        )
        _args_schema.premium_messaging_partitions = AAZIntArg(
            options=["--premium-partitions", "--premium-messaging-partitions"],
            arg_group="Properties",
            help="The number of partitions of a Service Bus namespace. This property is only applicable to Premium SKU namespaces. The default value is 1 and possible values are 1, 2 and 4",
            nullable=True,
        )
        _args_schema.private_endpoint_connections = AAZListArg(
            options=["--connections", "--private-endpoint-connections"],
            arg_group="Properties",
            help="List of private endpoint connections.",
            nullable=True,
        )
        _args_schema.public_network_access = AAZStrArg(
            options=["--public-network-access"],
            arg_group="Properties",
            help="This determines if traffic is allowed over public network. By default it is enabled.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled", "SecuredByPerimeter": "SecuredByPerimeter"},
        )

        encryption = cls._args_schema.encryption
        encryption.key_source = AAZStrArg(
            options=["key-source"],
            help="Enumerates the possible value of keySource for Encryption",
            nullable=True,
            enum={"Microsoft.KeyVault": "Microsoft.KeyVault"},
        )
        encryption.key_vault_properties = AAZListArg(
            options=["key-vault-properties"],
            help="Properties of KeyVault",
            nullable=True,
        )
        encryption.require_infrastructure_encryption = AAZBoolArg(
            options=["require-infrastructure-encryption"],
            help="Enable Infrastructure Encryption (Double Encryption)",
            nullable=True,
        )

        key_vault_properties = cls._args_schema.encryption.key_vault_properties
        key_vault_properties.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.encryption.key_vault_properties.Element
        _element.user_assigned_identity = AAZStrArg(
            options=["user-assigned-identity"],
            help="ARM ID of user Identity selected for encryption",
            nullable=True,
        )
        _element.key_name = AAZStrArg(
            options=["key-name"],
            help="Name of the Key from KeyVault",
            nullable=True,
        )
        _element.key_vault_uri = AAZStrArg(
            options=["key-vault-uri"],
            help="URI of KeyVault",
            nullable=True,
        )
        _element.key_version = AAZStrArg(
            options=["key-version"],
            help="Version of KeyVault",
            nullable=True,
        )

        private_endpoint_connections = cls._args_schema.private_endpoint_connections
        private_endpoint_connections.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.private_endpoint_connections.Element
        _element.private_endpoint = AAZObjectArg(
            options=["private-endpoint"],
            help="The Private Endpoint resource for this Connection.",
            nullable=True,
        )
        _element.private_link_service_connection_state = AAZObjectArg(
            options=["private-link-service-connection-state"],
            help="Details about the state of the connection.",
            nullable=True,
        )
        _element.provisioning_state = AAZStrArg(
            options=["provisioning-state"],
            help="Provisioning state of the Private Endpoint Connection.",
            nullable=True,
            enum={"Canceled": "Canceled", "Creating": "Creating", "Deleting": "Deleting", "Failed": "Failed", "Succeeded": "Succeeded", "Updating": "Updating"},
        )

        private_endpoint = cls._args_schema.private_endpoint_connections.Element.private_endpoint
        private_endpoint.id = AAZStrArg(
            options=["id"],
            help="The ARM identifier for Private Endpoint.",
            nullable=True,
        )

        private_link_service_connection_state = cls._args_schema.private_endpoint_connections.Element.private_link_service_connection_state
        private_link_service_connection_state.description = AAZStrArg(
            options=["description"],
            help="Description of the connection state.",
            nullable=True,
        )
        private_link_service_connection_state.status = AAZStrArg(
            options=["status"],
            help="Status of the connection.",
            nullable=True,
            enum={"Approved": "Approved", "Disconnected": "Disconnected", "Pending": "Pending", "Rejected": "Rejected"},
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.capacity = AAZIntArg(
            options=["--capacity"],
            arg_group="Sku",
            help="Messaging units for your service bus premium namespace. Valid capacities are {1, 2, 4, 8, 16} multiples of your properties.premiumMessagingPartitions setting. For example, If properties.premiumMessagingPartitions is 1 then possible capacity values are 1, 2, 4, 8, and 16. If properties.premiumMessagingPartitions is 4 then possible capacity values are 4, 8, 16, 32 and 64",
            nullable=True,
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            arg_group="Sku",
            help="Name of this SKU.",
            enum={"Basic": "Basic", "Premium": "Premium", "Standard": "Standard"},
        )
        _args_schema.tier = AAZStrArg(
            options=["--tier"],
            arg_group="Sku",
            help="The billing tier of this particular SKU.",
            nullable=True,
            enum={"Basic": "Basic", "Premium": "Premium", "Standard": "Standard"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NamespacesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.NamespacesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NamespacesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_sb_namespace_read(cls._schema_on_200)

            return cls._schema_on_200

    class NamespacesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_sb_namespace_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type")
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("alternateName", AAZStrType, ".alternate_name")
                properties.set_prop("disableLocalAuth", AAZBoolType, ".disable_local_auth")
                properties.set_prop("encryption", AAZObjectType, ".encryption")
                properties.set_prop("minimumTlsVersion", AAZStrType, ".minimum_tls_version")
                properties.set_prop("premiumMessagingPartitions", AAZIntType, ".premium_messaging_partitions")
                properties.set_prop("privateEndpointConnections", AAZListType, ".private_endpoint_connections")
                properties.set_prop("publicNetworkAccess", AAZStrType, ".public_network_access")

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("keySource", AAZStrType, ".key_source")
                encryption.set_prop("keyVaultProperties", AAZListType, ".key_vault_properties")
                encryption.set_prop("requireInfrastructureEncryption", AAZBoolType, ".require_infrastructure_encryption")

            key_vault_properties = _builder.get(".properties.encryption.keyVaultProperties")
            if key_vault_properties is not None:
                key_vault_properties.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.encryption.keyVaultProperties[]")
            if _elements is not None:
                _elements.set_prop("identity", AAZObjectType)
                _elements.set_prop("keyName", AAZStrType, ".key_name")
                _elements.set_prop("keyVaultUri", AAZStrType, ".key_vault_uri")
                _elements.set_prop("keyVersion", AAZStrType, ".key_version")

            identity = _builder.get(".properties.encryption.keyVaultProperties[].identity")
            if identity is not None:
                identity.set_prop("userAssignedIdentity", AAZStrType, ".user_assigned_identity")

            private_endpoint_connections = _builder.get(".properties.privateEndpointConnections")
            if private_endpoint_connections is not None:
                private_endpoint_connections.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.privateEndpointConnections[]")
            if _elements is not None:
                _elements.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties.privateEndpointConnections[].properties")
            if properties is not None:
                properties.set_prop("privateEndpoint", AAZObjectType, ".private_endpoint")
                properties.set_prop("privateLinkServiceConnectionState", AAZObjectType, ".private_link_service_connection_state")
                properties.set_prop("provisioningState", AAZStrType, ".provisioning_state")

            private_endpoint = _builder.get(".properties.privateEndpointConnections[].properties.privateEndpoint")
            if private_endpoint is not None:
                private_endpoint.set_prop("id", AAZStrType, ".id")

            private_link_service_connection_state = _builder.get(".properties.privateEndpointConnections[].properties.privateLinkServiceConnectionState")
            if private_link_service_connection_state is not None:
                private_link_service_connection_state.set_prop("description", AAZStrType, ".description")
                private_link_service_connection_state.set_prop("status", AAZStrType, ".status")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("capacity", AAZIntType, ".capacity")
                sku.set_prop("name", AAZStrType, ".sku", typ_kwargs={"flags": {"required": True}})
                sku.set_prop("tier", AAZStrType, ".tier")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_sb_namespace_read = None

    @classmethod
    def _build_schema_sb_namespace_read(cls, _schema):
        if cls._schema_sb_namespace_read is not None:
            _schema.id = cls._schema_sb_namespace_read.id
            _schema.identity = cls._schema_sb_namespace_read.identity
            _schema.location = cls._schema_sb_namespace_read.location
            _schema.name = cls._schema_sb_namespace_read.name
            _schema.properties = cls._schema_sb_namespace_read.properties
            _schema.sku = cls._schema_sb_namespace_read.sku
            _schema.system_data = cls._schema_sb_namespace_read.system_data
            _schema.tags = cls._schema_sb_namespace_read.tags
            _schema.type = cls._schema_sb_namespace_read.type
            return

        cls._schema_sb_namespace_read = _schema_sb_namespace_read = AAZObjectType()

        sb_namespace_read = _schema_sb_namespace_read
        sb_namespace_read.id = AAZStrType(
            flags={"read_only": True},
        )
        sb_namespace_read.identity = AAZObjectType()
        sb_namespace_read.location = AAZStrType(
            flags={"required": True},
        )
        sb_namespace_read.name = AAZStrType(
            flags={"read_only": True},
        )
        sb_namespace_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        sb_namespace_read.sku = AAZObjectType()
        sb_namespace_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cls._build_schema_system_data_read(sb_namespace_read.system_data)
        sb_namespace_read.tags = AAZDictType()
        sb_namespace_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_sb_namespace_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType()
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_sb_namespace_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_sb_namespace_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_sb_namespace_read.properties
        properties.alternate_name = AAZStrType(
            serialized_name="alternateName",
        )
        properties.created_at = AAZStrType(
            serialized_name="createdAt",
            flags={"read_only": True},
        )
        properties.disable_local_auth = AAZBoolType(
            serialized_name="disableLocalAuth",
        )
        properties.encryption = AAZObjectType()
        properties.metric_id = AAZStrType(
            serialized_name="metricId",
            flags={"read_only": True},
        )
        properties.minimum_tls_version = AAZStrType(
            serialized_name="minimumTlsVersion",
        )
        properties.premium_messaging_partitions = AAZIntType(
            serialized_name="premiumMessagingPartitions",
        )
        properties.private_endpoint_connections = AAZListType(
            serialized_name="privateEndpointConnections",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_network_access = AAZStrType(
            serialized_name="publicNetworkAccess",
        )
        properties.service_bus_endpoint = AAZStrType(
            serialized_name="serviceBusEndpoint",
            flags={"read_only": True},
        )
        properties.status = AAZStrType(
            flags={"read_only": True},
        )
        properties.updated_at = AAZStrType(
            serialized_name="updatedAt",
            flags={"read_only": True},
        )
        properties.zone_redundant = AAZBoolType(
            serialized_name="zoneRedundant",
        )

        encryption = _schema_sb_namespace_read.properties.encryption
        encryption.key_source = AAZStrType(
            serialized_name="keySource",
        )
        encryption.key_vault_properties = AAZListType(
            serialized_name="keyVaultProperties",
        )
        encryption.require_infrastructure_encryption = AAZBoolType(
            serialized_name="requireInfrastructureEncryption",
        )

        key_vault_properties = _schema_sb_namespace_read.properties.encryption.key_vault_properties
        key_vault_properties.Element = AAZObjectType()

        _element = _schema_sb_namespace_read.properties.encryption.key_vault_properties.Element
        _element.identity = AAZObjectType()
        _element.key_name = AAZStrType(
            serialized_name="keyName",
        )
        _element.key_vault_uri = AAZStrType(
            serialized_name="keyVaultUri",
        )
        _element.key_version = AAZStrType(
            serialized_name="keyVersion",
        )

        identity = _schema_sb_namespace_read.properties.encryption.key_vault_properties.Element.identity
        identity.user_assigned_identity = AAZStrType(
            serialized_name="userAssignedIdentity",
        )

        private_endpoint_connections = _schema_sb_namespace_read.properties.private_endpoint_connections
        private_endpoint_connections.Element = AAZObjectType()

        _element = _schema_sb_namespace_read.properties.private_endpoint_connections.Element
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.location = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        _element.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cls._build_schema_system_data_read(_element.system_data)
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_sb_namespace_read.properties.private_endpoint_connections.Element.properties
        properties.private_endpoint = AAZObjectType(
            serialized_name="privateEndpoint",
        )
        properties.private_link_service_connection_state = AAZObjectType(
            serialized_name="privateLinkServiceConnectionState",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )

        private_endpoint = _schema_sb_namespace_read.properties.private_endpoint_connections.Element.properties.private_endpoint
        private_endpoint.id = AAZStrType()

        private_link_service_connection_state = _schema_sb_namespace_read.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
        private_link_service_connection_state.description = AAZStrType()
        private_link_service_connection_state.status = AAZStrType()

        sku = _schema_sb_namespace_read.sku
        sku.capacity = AAZIntType()
        sku.name = AAZStrType(
            flags={"required": True},
        )
        sku.tier = AAZStrType()

        tags = _schema_sb_namespace_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_sb_namespace_read.id
        _schema.identity = cls._schema_sb_namespace_read.identity
        _schema.location = cls._schema_sb_namespace_read.location
        _schema.name = cls._schema_sb_namespace_read.name
        _schema.properties = cls._schema_sb_namespace_read.properties
        _schema.sku = cls._schema_sb_namespace_read.sku
        _schema.system_data = cls._schema_sb_namespace_read.system_data
        _schema.tags = cls._schema_sb_namespace_read.tags
        _schema.type = cls._schema_sb_namespace_read.type

    _schema_system_data_read = None

    @classmethod
    def _build_schema_system_data_read(cls, _schema):
        if cls._schema_system_data_read is not None:
            _schema.created_at = cls._schema_system_data_read.created_at
            _schema.created_by = cls._schema_system_data_read.created_by
            _schema.created_by_type = cls._schema_system_data_read.created_by_type
            _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
            _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
            _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type
            return

        cls._schema_system_data_read = _schema_system_data_read = AAZObjectType(
            flags={"read_only": True}
        )

        system_data_read = _schema_system_data_read
        system_data_read.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data_read.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data_read.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data_read.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data_read.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data_read.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.created_at = cls._schema_system_data_read.created_at
        _schema.created_by = cls._schema_system_data_read.created_by
        _schema.created_by_type = cls._schema_system_data_read.created_by_type
        _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
        _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type


__all__ = ["Update"]
