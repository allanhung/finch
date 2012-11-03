# -*- coding: utf-8 -*-
#
# Copyright 2012 Jaime Gil de Sagredo Luna
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module is a wrapper on top of the Tornado's HTTPClient."""

from finch.auth import HTTPBasicAuth


class Session(object):
    def __init__(self, http_client, auth=None):
        self.http_client = http_client

        if auth is not None:
            self.auth = HTTPBasicAuth(*auth)
        else:
            self.auth = None

    def fetch(self, *args, **kwargs):
        if self.auth is not None:
            args, kwargs = self.auth(args, kwargs)

        self.http_client.fetch(*args, **kwargs)
