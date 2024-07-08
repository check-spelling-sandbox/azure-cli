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
    "network virtual-appliance update",
    is_preview=True,
)
class Update(AAZCommand):
    """Update an Azure network virtual appliance.

    :example: Update an Azure network virtual appliance.
        az network virtual-appliance update -n MyName -g MyRG --asn 20000 --init-config "echo $hello"
    """

    _aaz_info = {
        "version": "2023-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkvirtualappliances/{}", "2023-11-01"],
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
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of Network Virtual Appliance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
            nullable=True,
        )
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            help="The identity of the Network Virtual Appliance, if configured.",
            nullable=True,
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the Network Virtual Appliance.",
            nullable=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.",
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
        _args_schema.additional_nics = AAZListArg(
            options=["--additional-nics"],
            arg_group="Properties",
            help="Details required for Additional Network Interface.",
            nullable=True,
        )
        _args_schema.boot_strap_config_blobs = AAZListArg(
            options=["--boot-blobs", "--boot-strap-config-blobs"],
            arg_group="Properties",
            help="Space-separated list of BootStrapConfigurationBlobs storage URLs.",
            nullable=True,
        )
        _args_schema.cloud_init_config = AAZStrArg(
            options=["--init-config", "--cloud-init-config"],
            arg_group="Properties",
            help="CloudInitConfiguration scripts that will be run during cloud initialization.",
            nullable=True,
        )
        _args_schema.cloud_init_config_blobs = AAZListArg(
            options=["--cloud-blobs", "--cloud-init-config-blobs"],
            arg_group="Properties",
            help="Space-separated list of CloudInitConfigurationBlob storage URLs.",
            nullable=True,
        )
        _args_schema.delegation = AAZObjectArg(
            options=["--delegation"],
            arg_group="Properties",
            help="The delegation for the Virtual Appliance",
            nullable=True,
        )

        #Manually changed --internet-ingress-public-ips to --internet-ingress-ips to make it lint compliant.
        #Will fix in Swagger in next release.
        _args_schema.internet_ingress_public_ips = AAZListArg(
            options=["--internet-ingress-ips"],
            arg_group="Properties",
            help="List of Resource URI of Public IPs for Internet Ingress Scenario.",
            nullable=True,
        )
        _args_schema.network_profile = AAZObjectArg(
            options=["--network-profile"],
            arg_group="Properties",
            help="Network Profile containing configurations for Public and Private NIC.",
            nullable=True,
        )
        _args_schema.asn = AAZIntArg(
            options=["--asn"],
            arg_group="Properties",
            help="VirtualAppliance ASN. The valid value ranges from 1 to 4294967295.",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=0,
            ),
        )

        additional_nics = cls._args_schema.additional_nics
        additional_nics.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.additional_nics.Element
        _element.has_public_ip = AAZBoolArg(
            options=["has-public-ip"],
            help="Flag (true or false) for Intent for Public Ip on additional nic",
            nullable=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="Name of additional nic",
            nullable=True,
        )

        boot_strap_config_blobs = cls._args_schema.boot_strap_config_blobs
        boot_strap_config_blobs.Element = AAZStrArg(
            nullable=True,
        )

        cloud_init_config_blobs = cls._args_schema.cloud_init_config_blobs
        cloud_init_config_blobs.Element = AAZStrArg(
            nullable=True,
        )

        delegation = cls._args_schema.delegation
        delegation.service_name = AAZStrArg(
            options=["service-name"],
            help="The service name to which the NVA is delegated.",
            nullable=True,
        )

        internet_ingress_public_ips = cls._args_schema.internet_ingress_public_ips
        internet_ingress_public_ips.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.internet_ingress_public_ips.Element
        _element.id = AAZResourceIdArg(
            options=["id"],
            help="Resource URI of Public Ip",
            nullable=True,
        )

        network_profile = cls._args_schema.network_profile
        network_profile.network_interface_configurations = AAZListArg(
            options=["network-interface-configurations"],
            nullable=True,
        )

        network_interface_configurations = cls._args_schema.network_profile.network_interface_configurations
        network_interface_configurations.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.network_profile.network_interface_configurations.Element
        _element.ip_configurations = AAZListArg(
            options=["ip-configurations"],
            nullable=True,
        )
        _element.type = AAZStrArg(
            options=["type"],
            help="NIC type. This should be either PublicNic or PrivateNic.",
            nullable=True,
            enum={"PrivateNic": "PrivateNic", "PublicNic": "PublicNic"},
        )

        ip_configurations = cls._args_schema.network_profile.network_interface_configurations.Element.ip_configurations
        ip_configurations.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.network_profile.network_interface_configurations.Element.ip_configurations.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="Name of the IP configuration.",
            nullable=True,
        )
        _element.primary = AAZBoolArg(
            options=["primary"],
            help="Whether or not this is primary IP configuration of the NIC.",
            nullable=True,
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.scale_unit = AAZStrArg(
            options=["--scale-unit"],
            arg_group="Sku",
            help="Virtual Appliance Scale Unit.",
            nullable=True,
        )
        _args_schema.version = AAZStrArg(
            options=["-v", "--version"],
            arg_group="Sku",
            help="Virtual Appliance Version.",
            nullable=True,
        )
        _args_schema.vendor = AAZStrArg(
            options=["--vendor"],
            arg_group="Sku",
            help="Virtual Appliance Vendor.",
            nullable=True,
        )

        # define Arg Group "VirtualHub"

        _args_schema = cls._args_schema
        _args_schema.vhub = AAZStrArg(
            options=["--vhub"],
            arg_group="VirtualHub",
            help="Name or ID of the virtual hub to which the Security Partner Provider belongs.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NetworkVirtualAppliancesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.NetworkVirtualAppliancesCreateOrUpdate(ctx=self.ctx)()
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

    class NetworkVirtualAppliancesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkVirtualApplianceName", self.ctx.args.name,
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
                    "api-version", "2023-11-01",
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
            _UpdateHelper._build_schema_network_virtual_appliance_read(cls._schema_on_200)

            return cls._schema_on_200

    class NetworkVirtualAppliancesCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}",
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
                    "networkVirtualApplianceName", self.ctx.args.name,
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
                    "api-version", "2023-11-01",
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
            _UpdateHelper._build_schema_network_virtual_appliance_read(cls._schema_on_200_201)

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
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
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
                properties.set_prop("additionalNics", AAZListType, ".additional_nics")
                properties.set_prop("bootStrapConfigurationBlobs", AAZListType, ".boot_strap_config_blobs")
                properties.set_prop("cloudInitConfiguration", AAZStrType, ".cloud_init_config")
                properties.set_prop("cloudInitConfigurationBlobs", AAZListType, ".cloud_init_config_blobs")
                properties.set_prop("delegation", AAZObjectType, ".delegation")
                properties.set_prop("internetIngressPublicIps", AAZListType, ".internet_ingress_public_ips")
                properties.set_prop("networkProfile", AAZObjectType, ".network_profile")
                properties.set_prop("nvaSku", AAZObjectType)
                properties.set_prop("virtualApplianceAsn", AAZIntType, ".asn")
                properties.set_prop("virtualHub", AAZObjectType)

            additional_nics = _builder.get(".properties.additionalNics")
            if additional_nics is not None:
                additional_nics.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.additionalNics[]")
            if _elements is not None:
                _elements.set_prop("hasPublicIp", AAZBoolType, ".has_public_ip")
                _elements.set_prop("name", AAZStrType, ".name")

            boot_strap_configuration_blobs = _builder.get(".properties.bootStrapConfigurationBlobs")
            if boot_strap_configuration_blobs is not None:
                boot_strap_configuration_blobs.set_elements(AAZStrType, ".")

            cloud_init_configuration_blobs = _builder.get(".properties.cloudInitConfigurationBlobs")
            if cloud_init_configuration_blobs is not None:
                cloud_init_configuration_blobs.set_elements(AAZStrType, ".")

            delegation = _builder.get(".properties.delegation")
            if delegation is not None:
                delegation.set_prop("serviceName", AAZStrType, ".service_name")

            internet_ingress_public_ips = _builder.get(".properties.internetIngressPublicIps")
            if internet_ingress_public_ips is not None:
                internet_ingress_public_ips.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.internetIngressPublicIps[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")

            network_profile = _builder.get(".properties.networkProfile")
            if network_profile is not None:
                network_profile.set_prop("networkInterfaceConfigurations", AAZListType, ".network_interface_configurations")

            network_interface_configurations = _builder.get(".properties.networkProfile.networkInterfaceConfigurations")
            if network_interface_configurations is not None:
                network_interface_configurations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.networkProfile.networkInterfaceConfigurations[]")
            if _elements is not None:
                _elements.set_prop("properties", AAZObjectType)
                _elements.set_prop("type", AAZStrType, ".type")

            properties = _builder.get(".properties.networkProfile.networkInterfaceConfigurations[].properties")
            if properties is not None:
                properties.set_prop("ipConfigurations", AAZListType, ".ip_configurations")

            ip_configurations = _builder.get(".properties.networkProfile.networkInterfaceConfigurations[].properties.ipConfigurations")
            if ip_configurations is not None:
                ip_configurations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.networkProfile.networkInterfaceConfigurations[].properties.ipConfigurations[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties.networkProfile.networkInterfaceConfigurations[].properties.ipConfigurations[].properties")
            if properties is not None:
                properties.set_prop("primary", AAZBoolType, ".primary")

            nva_sku = _builder.get(".properties.nvaSku")
            if nva_sku is not None:
                nva_sku.set_prop("bundledScaleUnit", AAZStrType, ".scale_unit")
                nva_sku.set_prop("marketPlaceVersion", AAZStrType, ".version")
                nva_sku.set_prop("vendor", AAZStrType, ".vendor")

            virtual_hub = _builder.get(".properties.virtualHub")
            if virtual_hub is not None:
                virtual_hub.set_prop("id", AAZStrType, ".vhub")

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

    _schema_network_virtual_appliance_read = None

    @classmethod
    def _build_schema_network_virtual_appliance_read(cls, _schema):
        if cls._schema_network_virtual_appliance_read is not None:
            _schema.etag = cls._schema_network_virtual_appliance_read.etag
            _schema.id = cls._schema_network_virtual_appliance_read.id
            _schema.identity = cls._schema_network_virtual_appliance_read.identity
            _schema.location = cls._schema_network_virtual_appliance_read.location
            _schema.name = cls._schema_network_virtual_appliance_read.name
            _schema.properties = cls._schema_network_virtual_appliance_read.properties
            _schema.tags = cls._schema_network_virtual_appliance_read.tags
            _schema.type = cls._schema_network_virtual_appliance_read.type
            return

        cls._schema_network_virtual_appliance_read = _schema_network_virtual_appliance_read = AAZObjectType()

        network_virtual_appliance_read = _schema_network_virtual_appliance_read
        network_virtual_appliance_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        network_virtual_appliance_read.id = AAZStrType()
        network_virtual_appliance_read.identity = AAZObjectType()
        network_virtual_appliance_read.location = AAZStrType()
        network_virtual_appliance_read.name = AAZStrType(
            flags={"read_only": True},
        )
        network_virtual_appliance_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        network_virtual_appliance_read.tags = AAZDictType()
        network_virtual_appliance_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_network_virtual_appliance_read.identity
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

        user_assigned_identities = _schema_network_virtual_appliance_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_network_virtual_appliance_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_network_virtual_appliance_read.properties
        properties.additional_nics = AAZListType(
            serialized_name="additionalNics",
        )
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
            flags={"read_only": True},
        )
        properties.boot_strap_configuration_blobs = AAZListType(
            serialized_name="bootStrapConfigurationBlobs",
        )
        properties.cloud_init_configuration = AAZStrType(
            serialized_name="cloudInitConfiguration",
        )
        properties.cloud_init_configuration_blobs = AAZListType(
            serialized_name="cloudInitConfigurationBlobs",
        )
        properties.delegation = AAZObjectType()
        properties.deployment_type = AAZStrType(
            serialized_name="deploymentType",
            flags={"read_only": True},
        )
        properties.inbound_security_rules = AAZListType(
            serialized_name="inboundSecurityRules",
            flags={"read_only": True},
        )
        properties.internet_ingress_public_ips = AAZListType(
            serialized_name="internetIngressPublicIps",
        )
        properties.network_profile = AAZObjectType(
            serialized_name="networkProfile",
        )
        properties.nva_sku = AAZObjectType(
            serialized_name="nvaSku",
        )
        properties.partner_managed_resource = AAZObjectType(
            serialized_name="partnerManagedResource",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.ssh_public_key = AAZStrType(
            serialized_name="sshPublicKey",
        )
        properties.virtual_appliance_asn = AAZIntType(
            serialized_name="virtualApplianceAsn",
        )
        properties.virtual_appliance_connections = AAZListType(
            serialized_name="virtualApplianceConnections",
            flags={"read_only": True},
        )
        properties.virtual_appliance_nics = AAZListType(
            serialized_name="virtualApplianceNics",
            flags={"read_only": True},
        )
        properties.virtual_appliance_sites = AAZListType(
            serialized_name="virtualApplianceSites",
            flags={"read_only": True},
        )
        properties.virtual_hub = AAZObjectType(
            serialized_name="virtualHub",
        )
        cls._build_schema_sub_resource_read(properties.virtual_hub)

        additional_nics = _schema_network_virtual_appliance_read.properties.additional_nics
        additional_nics.Element = AAZObjectType()

        _element = _schema_network_virtual_appliance_read.properties.additional_nics.Element
        _element.has_public_ip = AAZBoolType(
            serialized_name="hasPublicIp",
        )
        _element.name = AAZStrType()

        boot_strap_configuration_blobs = _schema_network_virtual_appliance_read.properties.boot_strap_configuration_blobs
        boot_strap_configuration_blobs.Element = AAZStrType()

        cloud_init_configuration_blobs = _schema_network_virtual_appliance_read.properties.cloud_init_configuration_blobs
        cloud_init_configuration_blobs.Element = AAZStrType()

        delegation = _schema_network_virtual_appliance_read.properties.delegation
        delegation.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        delegation.service_name = AAZStrType(
            serialized_name="serviceName",
        )

        inbound_security_rules = _schema_network_virtual_appliance_read.properties.inbound_security_rules
        inbound_security_rules.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(inbound_security_rules.Element)

        internet_ingress_public_ips = _schema_network_virtual_appliance_read.properties.internet_ingress_public_ips
        internet_ingress_public_ips.Element = AAZObjectType()

        _element = _schema_network_virtual_appliance_read.properties.internet_ingress_public_ips.Element
        _element.id = AAZStrType()

        network_profile = _schema_network_virtual_appliance_read.properties.network_profile
        network_profile.network_interface_configurations = AAZListType(
            serialized_name="networkInterfaceConfigurations",
        )

        network_interface_configurations = _schema_network_virtual_appliance_read.properties.network_profile.network_interface_configurations
        network_interface_configurations.Element = AAZObjectType()

        _element = _schema_network_virtual_appliance_read.properties.network_profile.network_interface_configurations.Element
        _element.properties = AAZObjectType()
        _element.type = AAZStrType()

        properties = _schema_network_virtual_appliance_read.properties.network_profile.network_interface_configurations.Element.properties
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
        )

        ip_configurations = _schema_network_virtual_appliance_read.properties.network_profile.network_interface_configurations.Element.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()

        _element = _schema_network_virtual_appliance_read.properties.network_profile.network_interface_configurations.Element.properties.ip_configurations.Element
        _element.name = AAZStrType()
        _element.properties = AAZObjectType()

        properties = _schema_network_virtual_appliance_read.properties.network_profile.network_interface_configurations.Element.properties.ip_configurations.Element.properties
        properties.primary = AAZBoolType()

        nva_sku = _schema_network_virtual_appliance_read.properties.nva_sku
        nva_sku.bundled_scale_unit = AAZStrType(
            serialized_name="bundledScaleUnit",
        )
        nva_sku.market_place_version = AAZStrType(
            serialized_name="marketPlaceVersion",
        )
        nva_sku.vendor = AAZStrType()

        partner_managed_resource = _schema_network_virtual_appliance_read.properties.partner_managed_resource
        partner_managed_resource.id = AAZStrType(
            flags={"read_only": True},
        )
        partner_managed_resource.internal_load_balancer_id = AAZStrType(
            serialized_name="internalLoadBalancerId",
            flags={"read_only": True},
        )
        partner_managed_resource.standard_load_balancer_id = AAZStrType(
            serialized_name="standardLoadBalancerId",
            flags={"read_only": True},
        )

        virtual_appliance_connections = _schema_network_virtual_appliance_read.properties.virtual_appliance_connections
        virtual_appliance_connections.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(virtual_appliance_connections.Element)

        virtual_appliance_nics = _schema_network_virtual_appliance_read.properties.virtual_appliance_nics
        virtual_appliance_nics.Element = AAZObjectType()

        _element = _schema_network_virtual_appliance_read.properties.virtual_appliance_nics.Element
        _element.instance_name = AAZStrType(
            serialized_name="instanceName",
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.nic_type = AAZStrType(
            serialized_name="nicType",
            flags={"read_only": True},
        )
        _element.private_ip_address = AAZStrType(
            serialized_name="privateIpAddress",
            flags={"read_only": True},
        )
        _element.public_ip_address = AAZStrType(
            serialized_name="publicIpAddress",
            flags={"read_only": True},
        )

        virtual_appliance_sites = _schema_network_virtual_appliance_read.properties.virtual_appliance_sites
        virtual_appliance_sites.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(virtual_appliance_sites.Element)

        tags = _schema_network_virtual_appliance_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_network_virtual_appliance_read.etag
        _schema.id = cls._schema_network_virtual_appliance_read.id
        _schema.identity = cls._schema_network_virtual_appliance_read.identity
        _schema.location = cls._schema_network_virtual_appliance_read.location
        _schema.name = cls._schema_network_virtual_appliance_read.name
        _schema.properties = cls._schema_network_virtual_appliance_read.properties
        _schema.tags = cls._schema_network_virtual_appliance_read.tags
        _schema.type = cls._schema_network_virtual_appliance_read.type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]
