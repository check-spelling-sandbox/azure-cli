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

from .usql_type import USqlType


class USqlTableType(USqlType):
    """A Data Lake Analytics catalog U-SQL table type item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param schema_name: the name of the schema associated with this table and
     database.
    :type schema_name: str
    :param name: the name of type for this type.
    :type name: str
    :param type_family: the type family for this type.
    :type type_family: str
    :param c_sharp_name: the C# name for this type.
    :type c_sharp_name: str
    :param full_csharp_name: the fully qualified C# name for this type.
    :type full_csharp_name: str
    :param system_type_id: the system type ID for this type.
    :type system_type_id: int
    :param user_type_id: the user type ID for this type.
    :type user_type_id: int
    :param schema_id: the schema ID for this type.
    :type schema_id: int
    :param principal_id: the principal ID for this type.
    :type principal_id: int
    :param is_nullable: the switch indicating if this type is nullable.
    :type is_nullable: bool
    :param is_user_defined: the switch indicating if this type is user
     defined.
    :type is_user_defined: bool
    :param is_assembly_type: the switch indicating if this type is an
     assembly type.
    :type is_assembly_type: bool
    :param is_table_type: the switch indicating if this type is a table
     type.
    :type is_table_type: bool
    :param is_complex_type: the switch indicating if this type is a
     complex type.
    :type is_complex_type: bool
    :ivar columns: the type field information associated with this table type.
    :vartype columns: list of :class:`TypeFieldInfo
     <azure.mgmt.datalake.analytics.catalog.models.TypeFieldInfo>`
    """

    _validation = {
        'columns': {'readonly': True},
    }

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'schema_name': {'key': 'schemaName', 'type': 'str'},
        'name': {'key': 'typeName', 'type': 'str'},
        'type_family': {'key': 'typeFamily', 'type': 'str'},
        'c_sharp_name': {'key': 'cSharpName', 'type': 'str'},
        'full_csharp_name': {'key': 'fullCSharpName', 'type': 'str'},
        'system_type_id': {'key': 'systemTypeId', 'type': 'int'},
        'user_type_id': {'key': 'userTypeId', 'type': 'int'},
        'schema_id': {'key': 'schemaId', 'type': 'int'},
        'principal_id': {'key': 'principalId', 'type': 'int'},
        'is_nullable': {'key': 'isNullable', 'type': 'bool'},
        'is_user_defined': {'key': 'isUserDefined', 'type': 'bool'},
        'is_assembly_type': {'key': 'isAssemblyType', 'type': 'bool'},
        'is_table_type': {'key': 'isTableType', 'type': 'bool'},
        'is_complex_type': {'key': 'isComplexType', 'type': 'bool'},
        'columns': {'key': 'columns', 'type': '[TypeFieldInfo]'},
    }

    def __init__(self, compute_account_name=None, version=None, database_name=None, schema_name=None, name=None, type_family=None, c_sharp_name=None, full_csharp_name=None, system_type_id=None, user_type_id=None, schema_id=None, principal_id=None, is_nullable=None, is_user_defined=None, is_assembly_type=None, is_table_type=None, is_complex_type=None):
        super(USqlTableType, self).__init__(compute_account_name=compute_account_name, version=version, database_name=database_name, schema_name=schema_name, name=name, type_family=type_family, c_sharp_name=c_sharp_name, full_csharp_name=full_csharp_name, system_type_id=system_type_id, user_type_id=user_type_id, schema_id=schema_id, principal_id=principal_id, is_nullable=is_nullable, is_user_defined=is_user_defined, is_assembly_type=is_assembly_type, is_table_type=is_table_type, is_complex_type=is_complex_type)
        self.columns = None
