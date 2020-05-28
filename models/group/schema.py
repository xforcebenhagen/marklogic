# -*- coding: utf-8 -*-
#
# Copyright 2015 MarkLogic Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0#
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# File History
# ------------
#
# Norman Walsh      08/09/2015     Initial development

"""
Classes for dealing with group auditing
"""

from __future__ import unicode_literals, print_function, absolute_import
from marklogic.models.model import Model

class Schema(Model):
    def __init__(self, namespace, schemaloc):
        """
        Create a schema.
        """
        self._config = {
            'namespace-uri': namespace,
            'schema-location': schemaloc
            }
