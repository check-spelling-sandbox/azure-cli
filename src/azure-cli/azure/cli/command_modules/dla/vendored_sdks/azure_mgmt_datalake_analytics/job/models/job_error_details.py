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

from msrest.serialization import Model


class JobErrorDetails(Model):
    """The Data Lake Analytics job error details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar description: the error message description
    :vartype description: str
    :ivar details: the details of the error message.
    :vartype details: str
    :ivar end_offset: the end offset in the job where the error was found.
    :vartype end_offset: int
    :ivar error_id: the specific identifier for the type of error encountered
     in the job.
    :vartype error_id: str
    :ivar file_path: the path to any supplemental error files, if any.
    :vartype file_path: str
    :ivar help_link: the link to MSDN or Azure help for this type of error, if
     any.
    :vartype help_link: str
    :ivar internal_diagnostics: the internal diagnostic stack trace if the
     user requesting the job error details has sufficient permissions it will
     be retrieved, otherwise it will be empty.
    :vartype internal_diagnostics: str
    :ivar line_number: the specific line number in the job where the error
     occurred.
    :vartype line_number: int
    :ivar message: the user friendly error message for the failure.
    :vartype message: str
    :ivar resolution: the recommended resolution for the failure, if any.
    :vartype resolution: str
    :ivar inner_error: the inner error of this specific job error message, if
     any.
    :vartype inner_error: :class:`JobInnerError
     <azure.mgmt.datalake.analytics.job.models.JobInnerError>`
    :ivar severity: the severity level of the failure. Possible values
     include: 'Warning', 'Error', 'Info', 'SevereWarning', 'Deprecated',
     'UserWarning'
    :vartype severity: str or :class:`SeverityTypes
     <azure.mgmt.datalake.analytics.job.models.SeverityTypes>`
    :ivar source: the ultimate source of the failure (usually either SYSTEM or
     USER).
    :vartype source: str
    :ivar start_offset: the start offset in the job where the error was found
    :vartype start_offset: int
    """

    _validation = {
        'description': {'readonly': True},
        'details': {'readonly': True},
        'end_offset': {'readonly': True},
        'error_id': {'readonly': True},
        'file_path': {'readonly': True},
        'help_link': {'readonly': True},
        'internal_diagnostics': {'readonly': True},
        'line_number': {'readonly': True},
        'message': {'readonly': True},
        'resolution': {'readonly': True},
        'inner_error': {'readonly': True},
        'severity': {'readonly': True},
        'source': {'readonly': True},
        'start_offset': {'readonly': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
        'end_offset': {'key': 'endOffset', 'type': 'int'},
        'error_id': {'key': 'errorId', 'type': 'str'},
        'file_path': {'key': 'filePath', 'type': 'str'},
        'help_link': {'key': 'helpLink', 'type': 'str'},
        'internal_diagnostics': {'key': 'internalDiagnostics', 'type': 'str'},
        'line_number': {'key': 'lineNumber', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'resolution': {'key': 'resolution', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'JobInnerError'},
        'severity': {'key': 'severity', 'type': 'SeverityTypes'},
        'source': {'key': 'source', 'type': 'str'},
        'start_offset': {'key': 'startOffset', 'type': 'int'},
    }

    def __init__(self):
        self.description = None
        self.details = None
        self.end_offset = None
        self.error_id = None
        self.file_path = None
        self.help_link = None
        self.internal_diagnostics = None
        self.line_number = None
        self.message = None
        self.resolution = None
        self.inner_error = None
        self.severity = None
        self.source = None
        self.start_offset = None
