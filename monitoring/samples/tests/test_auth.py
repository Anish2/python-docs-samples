# Copyright 2015, Google, Inc.
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

import os
import re
import unittest

from monitoring.samples import auth

import tests


class TestTimeseriesList(tests.CloudBaseTest):

    @classmethod
    def setUpClass(cls):
        cls.test_project_id = os.environ.get(tests.PROJECT_ID_ENV)

    def test_main(self):
        with tests.capture_stdout() as stdout:
            auth.main(self.test_project_id)
        output = stdout.getvalue().strip()
        self.assertRegexpMatches(
            output, re.compile(r'Timeseries.list raw response:\s*'
                               r'{\s*"kind": "[^"]+",'
                               r'\s*"oldest": *"[0-9]+', re.S))


if __name__ == '__main__':
    unittest.main()
