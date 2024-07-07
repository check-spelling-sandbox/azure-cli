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
    "sql mi link create",
)
class Create(AAZCommand):
    """Creates a new instance link.

    This command creates an Azure SQL Managed Instance link by joining distributed availability group on SQL Server based on the parameters passed.

    :example: Creates an instance link.
        az sql mi link create -g 'rg1' --instance-name 'mi1' --name 'link1' --primary-availability-group-name 'primaryag1' --secondary-availability-group-name 'secondaryag1' --source-endpoint '"tcp://server1:5022" --target-database 'db1' --no-wait')
    """

    _aaz_info = {
        "version": "2022-08-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.sql/managedinstances/{}/distributedavailabilitygroups/{}", "2022-08-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.distributed_availability_group_name = AAZStrArg(
            options=["-n", "--link", "--name", "--distributed-availability-group-name"],
            help="Name of the instance link.",
            required=True,
        )
        _args_schema.managed_instance_name = AAZStrArg(
            options=["--mi", "--instance-name", "--managed-instance", "--managed-instance-name"],
            help="Name of Azure SQL Managed Instance.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.primary_availability_group_name = AAZStrArg(
            options=["--primary-ag", "--primary-availability-group-name"],
            arg_group="Properties",
            help="Name of the primary availability group.",
        )
        _args_schema.secondary_availability_group_name = AAZStrArg(
            options=["--secondary-ag", "--secondary-availability-group-name"],
            arg_group="Properties",
            help="Name of the secondary availability group.",
        )
        _args_schema.source_endpoint = AAZStrArg(
            options=["--source-endpoint"],
            arg_group="Properties",
            help="IP address of the source endpoint.",
        )
        _args_schema.target_database = AAZStrArg(
            options=["--target-db", "--target-database"],
            arg_group="Properties",
            help="Name of the target database",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.DistributedAvailabilityGroupsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DistributedAvailabilityGroupsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/distributedAvailabilityGroups/{distributedAvailabilityGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "distributedAvailabilityGroupName", self.ctx.args.distributed_availability_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance_name,
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
                    "api-version", "2022-08-01-preview",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("primaryAvailabilityGroupName", AAZStrType, ".primary_availability_group_name")
                properties.set_prop("secondaryAvailabilityGroupName", AAZStrType, ".secondary_availability_group_name")
                properties.set_prop("sourceEndpoint", AAZStrType, ".source_endpoint")
                properties.set_prop("targetDatabase", AAZStrType, ".target_database")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.distributed_availability_group_id = AAZStrType(
                serialized_name="distributedAvailabilityGroupId",
                flags={"read_only": True},
            )
            properties.instance_role = AAZStrType(
                serialized_name="instanceRole",
                flags={"read_only": True},
            )
            properties.last_hardened_lsn = AAZStrType(
                serialized_name="lastHardenedLsn",
                flags={"read_only": True},
            )
            properties.link_state = AAZStrType(
                serialized_name="linkState",
                flags={"read_only": True},
            )
            properties.primary_availability_group_name = AAZStrType(
                serialized_name="primaryAvailabilityGroupName",
            )
            properties.replication_mode = AAZStrType(
                serialized_name="replicationMode",
            )
            properties.secondary_availability_group_name = AAZStrType(
                serialized_name="secondaryAvailabilityGroupName",
            )
            properties.source_endpoint = AAZStrType(
                serialized_name="sourceEndpoint",
            )
            properties.source_replica_id = AAZStrType(
                serialized_name="sourceReplicaId",
                flags={"read_only": True},
            )
            properties.target_database = AAZStrType(
                serialized_name="targetDatabase",
            )
            properties.target_replica_id = AAZStrType(
                serialized_name="targetReplicaId",
                flags={"read_only": True},
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
