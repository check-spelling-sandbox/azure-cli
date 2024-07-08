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
    "vmss list-instances",
)
class ListInstances(AAZCommand):
    """List all virtual machines in a VM scale sets.

    Return a list of virtual machines managed by VMSS. For VMSS in Flexible Orchestration mode, please use "az vm list" to get full details.
    """

    _aaz_info = {
        "version": "2017-03-30",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/virtualmachinescalesets/{}/virtualmachines", "2017-03-30"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.virtual_machine_scale_set_name = AAZStrArg(
            options=["-n", "--name", "--virtual-machine-scale-set-name"],
            help="The name of the VM scale set.",
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="The expand expression to apply to the operation. Allowed values are 'instanceView'.",
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter to apply to the operation. Allowed values are 'startswith(instanceView/statuses/code, 'PowerState') eq true', 'properties/latestModelApplied eq true', 'properties/latestModelApplied eq false'.",
        )
        _args_schema.select = AAZStrArg(
            options=["--select"],
            help="The list parameters. Allowed values are 'instanceView', 'instanceView/statuses'.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualMachineScaleSetVMsList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class VirtualMachineScaleSetVMsList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines",
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
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualMachineScaleSetName", self.ctx.args.virtual_machine_scale_set_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$select", self.ctx.args.select,
                ),
                **self.serialize_query_param(
                    "api-version", "2017-03-30",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.instance_id = AAZStrType(
                serialized_name="instanceId",
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.plan = AAZObjectType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.resources = AAZListType(
                flags={"read_only": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            plan = cls._schema_on_200.value.Element.plan
            plan.name = AAZStrType()
            plan.product = AAZStrType()
            plan.promotion_code = AAZStrType(
                serialized_name="promotionCode",
            )
            plan.publisher = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.availability_set = AAZObjectType(
                serialized_name="availabilitySet",
            )
            _ListInstancesHelper._build_schema_sub_resource_read(properties.availability_set)
            properties.diagnostics_profile = AAZObjectType(
                serialized_name="diagnosticsProfile",
            )
            properties.hardware_profile = AAZObjectType(
                serialized_name="hardwareProfile",
            )
            properties.instance_view = AAZObjectType(
                serialized_name="instanceView",
            )
            properties.latest_model_applied = AAZBoolType(
                serialized_name="latestModelApplied",
                flags={"read_only": True},
            )
            properties.license_type = AAZStrType(
                serialized_name="licenseType",
            )
            properties.network_profile = AAZObjectType(
                serialized_name="networkProfile",
            )
            properties.os_profile = AAZObjectType(
                serialized_name="osProfile",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
            )
            properties.vm_id = AAZStrType(
                serialized_name="vmId",
                flags={"read_only": True},
            )

            diagnostics_profile = cls._schema_on_200.value.Element.properties.diagnostics_profile
            diagnostics_profile.boot_diagnostics = AAZObjectType(
                serialized_name="bootDiagnostics",
            )

            boot_diagnostics = cls._schema_on_200.value.Element.properties.diagnostics_profile.boot_diagnostics
            boot_diagnostics.enabled = AAZBoolType()
            boot_diagnostics.storage_uri = AAZStrType(
                serialized_name="storageUri",
            )

            hardware_profile = cls._schema_on_200.value.Element.properties.hardware_profile
            hardware_profile.vm_size = AAZStrType(
                serialized_name="vmSize",
            )

            instance_view = cls._schema_on_200.value.Element.properties.instance_view
            instance_view.boot_diagnostics = AAZObjectType(
                serialized_name="bootDiagnostics",
            )
            instance_view.disks = AAZListType()
            instance_view.extensions = AAZListType()
            instance_view.placement_group_id = AAZStrType(
                serialized_name="placementGroupId",
            )
            instance_view.platform_fault_domain = AAZIntType(
                serialized_name="platformFaultDomain",
            )
            instance_view.platform_update_domain = AAZIntType(
                serialized_name="platformUpdateDomain",
            )
            instance_view.rdp_thumb_print = AAZStrType(
                serialized_name="rdpThumbPrint",
            )
            instance_view.statuses = AAZListType()
            instance_view.vm_agent = AAZObjectType(
                serialized_name="vmAgent",
            )
            instance_view.vm_health = AAZObjectType(
                serialized_name="vmHealth",
            )

            boot_diagnostics = cls._schema_on_200.value.Element.properties.instance_view.boot_diagnostics
            boot_diagnostics.console_screenshot_blob_uri = AAZStrType(
                serialized_name="consoleScreenshotBlobUri",
                flags={"read_only": True},
            )
            boot_diagnostics.serial_console_log_blob_uri = AAZStrType(
                serialized_name="serialConsoleLogBlobUri",
                flags={"read_only": True},
            )

            disks = cls._schema_on_200.value.Element.properties.instance_view.disks
            disks.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.instance_view.disks.Element
            _element.encryption_settings = AAZListType(
                serialized_name="encryptionSettings",
            )
            _element.name = AAZStrType()
            _element.statuses = AAZListType()

            encryption_settings = cls._schema_on_200.value.Element.properties.instance_view.disks.Element.encryption_settings
            encryption_settings.Element = AAZObjectType()
            _ListInstancesHelper._build_schema_disk_encryption_settings_read(encryption_settings.Element)

            statuses = cls._schema_on_200.value.Element.properties.instance_view.disks.Element.statuses
            statuses.Element = AAZObjectType()
            _ListInstancesHelper._build_schema_instance_view_status_read(statuses.Element)

            extensions = cls._schema_on_200.value.Element.properties.instance_view.extensions
            extensions.Element = AAZObjectType()
            _ListInstancesHelper._build_schema_virtual_machine_extension_instance_view_read(extensions.Element)

            statuses = cls._schema_on_200.value.Element.properties.instance_view.statuses
            statuses.Element = AAZObjectType()
            _ListInstancesHelper._build_schema_instance_view_status_read(statuses.Element)

            vm_agent = cls._schema_on_200.value.Element.properties.instance_view.vm_agent
            vm_agent.extension_handlers = AAZListType(
                serialized_name="extensionHandlers",
            )
            vm_agent.statuses = AAZListType()
            vm_agent.vm_agent_version = AAZStrType(
                serialized_name="vmAgentVersion",
            )

            extension_handlers = cls._schema_on_200.value.Element.properties.instance_view.vm_agent.extension_handlers
            extension_handlers.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.instance_view.vm_agent.extension_handlers.Element
            _element.status = AAZObjectType()
            _ListInstancesHelper._build_schema_instance_view_status_read(_element.status)
            _element.type = AAZStrType()
            _element.type_handler_version = AAZStrType(
                serialized_name="typeHandlerVersion",
            )

            statuses = cls._schema_on_200.value.Element.properties.instance_view.vm_agent.statuses
            statuses.Element = AAZObjectType()
            _ListInstancesHelper._build_schema_instance_view_status_read(statuses.Element)

            vm_health = cls._schema_on_200.value.Element.properties.instance_view.vm_health
            vm_health.status = AAZObjectType()
            _ListInstancesHelper._build_schema_instance_view_status_read(vm_health.status)

            network_profile = cls._schema_on_200.value.Element.properties.network_profile
            network_profile.network_interfaces = AAZListType(
                serialized_name="networkInterfaces",
            )

            network_interfaces = cls._schema_on_200.value.Element.properties.network_profile.network_interfaces
            network_interfaces.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.network_profile.network_interfaces.Element
            _element.id = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.network_profile.network_interfaces.Element.properties
            properties.primary = AAZBoolType()

            os_profile = cls._schema_on_200.value.Element.properties.os_profile
            os_profile.admin_password = AAZStrType(
                serialized_name="adminPassword",
            )
            os_profile.admin_username = AAZStrType(
                serialized_name="adminUsername",
            )
            os_profile.computer_name = AAZStrType(
                serialized_name="computerName",
            )
            os_profile.custom_data = AAZStrType(
                serialized_name="customData",
            )
            os_profile.linux_configuration = AAZObjectType(
                serialized_name="linuxConfiguration",
            )
            os_profile.secrets = AAZListType()
            os_profile.windows_configuration = AAZObjectType(
                serialized_name="windowsConfiguration",
            )

            linux_configuration = cls._schema_on_200.value.Element.properties.os_profile.linux_configuration
            linux_configuration.disable_password_authentication = AAZBoolType(
                serialized_name="disablePasswordAuthentication",
            )
            linux_configuration.ssh = AAZObjectType()

            ssh = cls._schema_on_200.value.Element.properties.os_profile.linux_configuration.ssh
            ssh.public_keys = AAZListType(
                serialized_name="publicKeys",
            )

            public_keys = cls._schema_on_200.value.Element.properties.os_profile.linux_configuration.ssh.public_keys
            public_keys.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.os_profile.linux_configuration.ssh.public_keys.Element
            _element.key_data = AAZStrType(
                serialized_name="keyData",
            )
            _element.path = AAZStrType()

            secrets = cls._schema_on_200.value.Element.properties.os_profile.secrets
            secrets.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.os_profile.secrets.Element
            _element.source_vault = AAZObjectType(
                serialized_name="sourceVault",
            )
            _ListInstancesHelper._build_schema_sub_resource_read(_element.source_vault)
            _element.vault_certificates = AAZListType(
                serialized_name="vaultCertificates",
            )

            vault_certificates = cls._schema_on_200.value.Element.properties.os_profile.secrets.Element.vault_certificates
            vault_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.os_profile.secrets.Element.vault_certificates.Element
            _element.certificate_store = AAZStrType(
                serialized_name="certificateStore",
            )
            _element.certificate_url = AAZStrType(
                serialized_name="certificateUrl",
            )

            windows_configuration = cls._schema_on_200.value.Element.properties.os_profile.windows_configuration
            windows_configuration.additional_unattended_content = AAZListType(
                serialized_name="additionalUnattendContent",
            )
            windows_configuration.enable_automatic_updates = AAZBoolType(
                serialized_name="enableAutomaticUpdates",
            )
            windows_configuration.provision_vm_agent = AAZBoolType(
                serialized_name="provisionVMAgent",
            )
            windows_configuration.time_zone = AAZStrType(
                serialized_name="timeZone",
            )
            windows_configuration.win_rm = AAZObjectType(
                serialized_name="winRM",
            )

            additional_unattended_content = cls._schema_on_200.value.Element.properties.os_profile.windows_configuration.additional_unattended_content
            additional_unattended_content.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.os_profile.windows_configuration.additional_unattended_content.Element
            _element.component_name = AAZStrType(
                serialized_name="componentName",
            )
            _element.content = AAZStrType()
            _element.pass_name = AAZStrType(
                serialized_name="passName",
            )
            _element.setting_name = AAZStrType(
                serialized_name="settingName",
            )

            win_rm = cls._schema_on_200.value.Element.properties.os_profile.windows_configuration.win_rm
            win_rm.listeners = AAZListType()

            listeners = cls._schema_on_200.value.Element.properties.os_profile.windows_configuration.win_rm.listeners
            listeners.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.os_profile.windows_configuration.win_rm.listeners.Element
            _element.certificate_url = AAZStrType(
                serialized_name="certificateUrl",
            )
            _element.protocol = AAZStrType()

            storage_profile = cls._schema_on_200.value.Element.properties.storage_profile
            storage_profile.data_disks = AAZListType(
                serialized_name="dataDisks",
            )
            storage_profile.image_reference = AAZObjectType(
                serialized_name="imageReference",
            )
            storage_profile.os_disk = AAZObjectType(
                serialized_name="osDisk",
            )

            data_disks = cls._schema_on_200.value.Element.properties.storage_profile.data_disks
            data_disks.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.storage_profile.data_disks.Element
            _element.caching = AAZStrType()
            _element.create_option = AAZStrType(
                serialized_name="createOption",
                flags={"required": True},
            )
            _element.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            _element.image = AAZObjectType()
            _ListInstancesHelper._build_schema_virtual_hard_disk_read(_element.image)
            _element.lun = AAZIntType(
                flags={"required": True},
            )
            _element.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListInstancesHelper._build_schema_managed_disk_parameters_read(_element.managed_disk)
            _element.name = AAZStrType()
            _element.vhd = AAZObjectType()
            _ListInstancesHelper._build_schema_virtual_hard_disk_read(_element.vhd)

            image_reference = cls._schema_on_200.value.Element.properties.storage_profile.image_reference
            image_reference.id = AAZStrType()
            image_reference.offer = AAZStrType()
            image_reference.publisher = AAZStrType()
            image_reference.sku = AAZStrType()
            image_reference.version = AAZStrType()

            os_disk = cls._schema_on_200.value.Element.properties.storage_profile.os_disk
            os_disk.caching = AAZStrType()
            os_disk.create_option = AAZStrType(
                serialized_name="createOption",
                flags={"required": True},
            )
            os_disk.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            os_disk.encryption_settings = AAZObjectType(
                serialized_name="encryptionSettings",
            )
            _ListInstancesHelper._build_schema_disk_encryption_settings_read(os_disk.encryption_settings)
            os_disk.image = AAZObjectType()
            _ListInstancesHelper._build_schema_virtual_hard_disk_read(os_disk.image)
            os_disk.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListInstancesHelper._build_schema_managed_disk_parameters_read(os_disk.managed_disk)
            os_disk.name = AAZStrType()
            os_disk.os_type = AAZStrType(
                serialized_name="osType",
            )
            os_disk.vhd = AAZObjectType()
            _ListInstancesHelper._build_schema_virtual_hard_disk_read(os_disk.vhd)

            resources = cls._schema_on_200.value.Element.resources
            resources.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.resources.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.resources.Element.properties
            properties.auto_upgrade_minor_version = AAZBoolType(
                serialized_name="autoUpgradeMinorVersion",
            )
            properties.force_update_tag = AAZStrType(
                serialized_name="forceUpdateTag",
            )
            properties.instance_view = AAZObjectType(
                serialized_name="instanceView",
            )
            _ListInstancesHelper._build_schema_virtual_machine_extension_instance_view_read(properties.instance_view)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.publisher = AAZStrType()
            properties.type = AAZStrType()
            properties.type_handler_version = AAZStrType(
                serialized_name="typeHandlerVersion",
            )

            tags = cls._schema_on_200.value.Element.resources.Element.tags
            tags.Element = AAZStrType()

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListInstancesHelper:
    """Helper class for ListInstances"""

    _schema_disk_encryption_settings_read = None

    @classmethod
    def _build_schema_disk_encryption_settings_read(cls, _schema):
        if cls._schema_disk_encryption_settings_read is not None:
            _schema.disk_encryption_key = cls._schema_disk_encryption_settings_read.disk_encryption_key
            _schema.enabled = cls._schema_disk_encryption_settings_read.enabled
            _schema.key_encryption_key = cls._schema_disk_encryption_settings_read.key_encryption_key
            return

        cls._schema_disk_encryption_settings_read = _schema_disk_encryption_settings_read = AAZObjectType()

        disk_encryption_settings_read = _schema_disk_encryption_settings_read
        disk_encryption_settings_read.disk_encryption_key = AAZObjectType(
            serialized_name="diskEncryptionKey",
        )
        disk_encryption_settings_read.enabled = AAZBoolType()
        disk_encryption_settings_read.key_encryption_key = AAZObjectType(
            serialized_name="keyEncryptionKey",
        )

        disk_encryption_key = _schema_disk_encryption_settings_read.disk_encryption_key
        disk_encryption_key.secret_url = AAZStrType(
            serialized_name="secretUrl",
            flags={"required": True},
        )
        disk_encryption_key.source_vault = AAZObjectType(
            serialized_name="sourceVault",
            flags={"required": True},
        )
        cls._build_schema_sub_resource_read(disk_encryption_key.source_vault)

        key_encryption_key = _schema_disk_encryption_settings_read.key_encryption_key
        key_encryption_key.key_url = AAZStrType(
            serialized_name="keyUrl",
            flags={"required": True},
        )
        key_encryption_key.source_vault = AAZObjectType(
            serialized_name="sourceVault",
            flags={"required": True},
        )
        cls._build_schema_sub_resource_read(key_encryption_key.source_vault)

        _schema.disk_encryption_key = cls._schema_disk_encryption_settings_read.disk_encryption_key
        _schema.enabled = cls._schema_disk_encryption_settings_read.enabled
        _schema.key_encryption_key = cls._schema_disk_encryption_settings_read.key_encryption_key

    _schema_instance_view_status_read = None

    @classmethod
    def _build_schema_instance_view_status_read(cls, _schema):
        if cls._schema_instance_view_status_read is not None:
            _schema.code = cls._schema_instance_view_status_read.code
            _schema.display_status = cls._schema_instance_view_status_read.display_status
            _schema.level = cls._schema_instance_view_status_read.level
            _schema.message = cls._schema_instance_view_status_read.message
            _schema.time = cls._schema_instance_view_status_read.time
            return

        cls._schema_instance_view_status_read = _schema_instance_view_status_read = AAZObjectType()

        instance_view_status_read = _schema_instance_view_status_read
        instance_view_status_read.code = AAZStrType()
        instance_view_status_read.display_status = AAZStrType(
            serialized_name="displayStatus",
        )
        instance_view_status_read.level = AAZStrType()
        instance_view_status_read.message = AAZStrType()
        instance_view_status_read.time = AAZStrType()

        _schema.code = cls._schema_instance_view_status_read.code
        _schema.display_status = cls._schema_instance_view_status_read.display_status
        _schema.level = cls._schema_instance_view_status_read.level
        _schema.message = cls._schema_instance_view_status_read.message
        _schema.time = cls._schema_instance_view_status_read.time

    _schema_managed_disk_parameters_read = None

    @classmethod
    def _build_schema_managed_disk_parameters_read(cls, _schema):
        if cls._schema_managed_disk_parameters_read is not None:
            _schema.id = cls._schema_managed_disk_parameters_read.id
            _schema.storage_account_type = cls._schema_managed_disk_parameters_read.storage_account_type
            return

        cls._schema_managed_disk_parameters_read = _schema_managed_disk_parameters_read = AAZObjectType()

        managed_disk_parameters_read = _schema_managed_disk_parameters_read
        managed_disk_parameters_read.id = AAZStrType()
        managed_disk_parameters_read.storage_account_type = AAZStrType(
            serialized_name="storageAccountType",
        )

        _schema.id = cls._schema_managed_disk_parameters_read.id
        _schema.storage_account_type = cls._schema_managed_disk_parameters_read.storage_account_type

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

    _schema_virtual_hard_disk_read = None

    @classmethod
    def _build_schema_virtual_hard_disk_read(cls, _schema):
        if cls._schema_virtual_hard_disk_read is not None:
            _schema.uri = cls._schema_virtual_hard_disk_read.uri
            return

        cls._schema_virtual_hard_disk_read = _schema_virtual_hard_disk_read = AAZObjectType()

        virtual_hard_disk_read = _schema_virtual_hard_disk_read
        virtual_hard_disk_read.uri = AAZStrType()

        _schema.uri = cls._schema_virtual_hard_disk_read.uri

    _schema_virtual_machine_extension_instance_view_read = None

    @classmethod
    def _build_schema_virtual_machine_extension_instance_view_read(cls, _schema):
        if cls._schema_virtual_machine_extension_instance_view_read is not None:
            _schema.name = cls._schema_virtual_machine_extension_instance_view_read.name
            _schema.statuses = cls._schema_virtual_machine_extension_instance_view_read.statuses
            _schema.substatuses = cls._schema_virtual_machine_extension_instance_view_read.substatuses
            _schema.type = cls._schema_virtual_machine_extension_instance_view_read.type
            _schema.type_handler_version = cls._schema_virtual_machine_extension_instance_view_read.type_handler_version
            return

        cls._schema_virtual_machine_extension_instance_view_read = _schema_virtual_machine_extension_instance_view_read = AAZObjectType()

        virtual_machine_extension_instance_view_read = _schema_virtual_machine_extension_instance_view_read
        virtual_machine_extension_instance_view_read.name = AAZStrType()
        virtual_machine_extension_instance_view_read.statuses = AAZListType()
        virtual_machine_extension_instance_view_read.substatuses = AAZListType()
        virtual_machine_extension_instance_view_read.type = AAZStrType()
        virtual_machine_extension_instance_view_read.type_handler_version = AAZStrType(
            serialized_name="typeHandlerVersion",
        )

        statuses = _schema_virtual_machine_extension_instance_view_read.statuses
        statuses.Element = AAZObjectType()
        cls._build_schema_instance_view_status_read(statuses.Element)

        substatuses = _schema_virtual_machine_extension_instance_view_read.substatuses
        substatuses.Element = AAZObjectType()
        cls._build_schema_instance_view_status_read(substatuses.Element)

        _schema.name = cls._schema_virtual_machine_extension_instance_view_read.name
        _schema.statuses = cls._schema_virtual_machine_extension_instance_view_read.statuses
        _schema.substatuses = cls._schema_virtual_machine_extension_instance_view_read.substatuses
        _schema.type = cls._schema_virtual_machine_extension_instance_view_read.type
        _schema.type_handler_version = cls._schema_virtual_machine_extension_instance_view_read.type_handler_version


__all__ = ["ListInstances"]
