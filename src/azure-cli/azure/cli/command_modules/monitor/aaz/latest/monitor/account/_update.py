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
    "monitor account update",
)
class Update(AAZCommand):
    """Update a workspace

    :example: Update monitor account tags
        az monitor account update -n account-name -g rg --tags "{tag:test}"
    """

    _aaz_info = {
        "version": "2023-04-03",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.monitor/accounts/{}", "2023-04-03"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.azure_monitor_workspace_name = AAZStrArg(
            options=["-n", "--name", "--azure-monitor-workspace-name"],
            help="The name of the Azure Monitor workspace.  The name is case-insensitive",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^(?!-)[a-zA-Z0-9-]+[^-]$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "AzureMonitorWorkspaceProperties"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="AzureMonitorWorkspaceProperties",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AzureMonitorWorkspacesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.AzureMonitorWorkspacesCreate(ctx=self.ctx)()
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

    class AzureMonitorWorkspacesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/accounts/{azureMonitorWorkspaceName}",
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
                    "azureMonitorWorkspaceName", self.ctx.args.azure_monitor_workspace_name,
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
                    "api-version", "2023-04-03",
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
            _UpdateHelper._build_schema_azure_monitor_workspace_resource_read(cls._schema_on_200)

            return cls._schema_on_200

    class AzureMonitorWorkspacesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/accounts/{azureMonitorWorkspaceName}",
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
                    "azureMonitorWorkspaceName", self.ctx.args.azure_monitor_workspace_name,
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
                    "api-version", "2023-04-03",
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
            _UpdateHelper._build_schema_azure_monitor_workspace_resource_read(cls._schema_on_200_201)

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
            _builder.set_prop("tags", AAZDictType, ".tags")

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

    _schema_azure_monitor_workspace_resource_read = None

    @classmethod
    def _build_schema_azure_monitor_workspace_resource_read(cls, _schema):
        if cls._schema_azure_monitor_workspace_resource_read is not None:
            _schema.etag = cls._schema_azure_monitor_workspace_resource_read.etag
            _schema.id = cls._schema_azure_monitor_workspace_resource_read.id
            _schema.location = cls._schema_azure_monitor_workspace_resource_read.location
            _schema.name = cls._schema_azure_monitor_workspace_resource_read.name
            _schema.properties = cls._schema_azure_monitor_workspace_resource_read.properties
            _schema.system_data = cls._schema_azure_monitor_workspace_resource_read.system_data
            _schema.tags = cls._schema_azure_monitor_workspace_resource_read.tags
            _schema.type = cls._schema_azure_monitor_workspace_resource_read.type
            return

        cls._schema_azure_monitor_workspace_resource_read = _schema_azure_monitor_workspace_resource_read = AAZObjectType()

        azure_monitor_workspace_resource_read = _schema_azure_monitor_workspace_resource_read
        azure_monitor_workspace_resource_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        azure_monitor_workspace_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )
        azure_monitor_workspace_resource_read.location = AAZStrType(
            flags={"required": True},
        )
        azure_monitor_workspace_resource_read.name = AAZStrType(
            flags={"read_only": True},
        )
        azure_monitor_workspace_resource_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        azure_monitor_workspace_resource_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cls._build_schema_system_data_read(azure_monitor_workspace_resource_read.system_data)
        azure_monitor_workspace_resource_read.tags = AAZDictType()
        azure_monitor_workspace_resource_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_azure_monitor_workspace_resource_read.properties
        properties.account_id = AAZStrType(
            serialized_name="accountId",
            flags={"read_only": True},
        )
        properties.default_ingestion_settings = AAZObjectType(
            serialized_name="defaultIngestionSettings",
            flags={"read_only": True},
        )
        properties.metrics = AAZObjectType(
            flags={"read_only": True},
        )
        properties.private_endpoint_connections = AAZListType(
            serialized_name="privateEndpointConnections",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_network_access = AAZStrType(
            serialized_name="publicNetworkAccess",
            flags={"read_only": True},
        )

        default_ingestion_settings = _schema_azure_monitor_workspace_resource_read.properties.default_ingestion_settings
        default_ingestion_settings.data_collection_endpoint_resource_id = AAZStrType(
            serialized_name="dataCollectionEndpointResourceId",
            flags={"read_only": True},
        )
        default_ingestion_settings.data_collection_rule_resource_id = AAZStrType(
            serialized_name="dataCollectionRuleResourceId",
            flags={"read_only": True},
        )

        metrics = _schema_azure_monitor_workspace_resource_read.properties.metrics
        metrics.internal_id = AAZStrType(
            serialized_name="internalId",
            flags={"read_only": True},
        )
        metrics.prometheus_query_endpoint = AAZStrType(
            serialized_name="prometheusQueryEndpoint",
            flags={"read_only": True},
        )

        private_endpoint_connections = _schema_azure_monitor_workspace_resource_read.properties.private_endpoint_connections
        private_endpoint_connections.Element = AAZObjectType()

        _element = _schema_azure_monitor_workspace_resource_read.properties.private_endpoint_connections.Element
        _element.id = AAZStrType(
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

        properties = _schema_azure_monitor_workspace_resource_read.properties.private_endpoint_connections.Element.properties
        properties.group_ids = AAZListType(
            serialized_name="groupIds",
            flags={"read_only": True},
        )
        properties.private_endpoint = AAZObjectType(
            serialized_name="privateEndpoint",
        )
        properties.private_link_service_connection_state = AAZObjectType(
            serialized_name="privateLinkServiceConnectionState",
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        group_ids = _schema_azure_monitor_workspace_resource_read.properties.private_endpoint_connections.Element.properties.group_ids
        group_ids.Element = AAZStrType()

        private_endpoint = _schema_azure_monitor_workspace_resource_read.properties.private_endpoint_connections.Element.properties.private_endpoint
        private_endpoint.id = AAZStrType(
            flags={"read_only": True},
        )

        private_link_service_connection_state = _schema_azure_monitor_workspace_resource_read.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
        private_link_service_connection_state.actions_required = AAZStrType(
            serialized_name="actionsRequired",
        )
        private_link_service_connection_state.description = AAZStrType()
        private_link_service_connection_state.status = AAZStrType()

        tags = _schema_azure_monitor_workspace_resource_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_azure_monitor_workspace_resource_read.etag
        _schema.id = cls._schema_azure_monitor_workspace_resource_read.id
        _schema.location = cls._schema_azure_monitor_workspace_resource_read.location
        _schema.name = cls._schema_azure_monitor_workspace_resource_read.name
        _schema.properties = cls._schema_azure_monitor_workspace_resource_read.properties
        _schema.system_data = cls._schema_azure_monitor_workspace_resource_read.system_data
        _schema.tags = cls._schema_azure_monitor_workspace_resource_read.tags
        _schema.type = cls._schema_azure_monitor_workspace_resource_read.type

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
