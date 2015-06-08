#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import unittest
from pynos.netconf.system import System
import xml.etree.ElementTree as ET

class _Tester(object):
    '''
    Tester object
    '''
    def __init__(self):
        self.system = System(self._callback)
        self.output = None

    def _callback(self, config):
        '''
        Callback function to return text of XML
        '''
        self.output = ET.tostring(config)

TESTER = _Tester()

class TestSystem(unittest.TestCase):
    '''
    Testing System
    '''
    def test_add_snmp_community(self):
        '''
        Test adding an SNMP community
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><community><community>test</community></community></snmp-server></config>'

        TESTER.system.add_snmp_community('test')
        self.assertEqual(TESTER.output, output)

    def test_del_snmp_community(self):
        '''
        Test delete SNMP community
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><community operation="delete"><community>test</community></community></snmp-s\
erver></config>'

        TESTER.system.del_snmp_community('test')
        self.assertEqual(TESTER.output, output)

    def test_add_snmp_host(self):
        '''
        Test add snmp host
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><host><ip>10.0.0.1</ip><community>Public</community><udp-port>161</udp-port><\
/host></snmp-server></config>'

        TESTER.system.add_snmp_host(('10.0.0.1', '161'))
        self.assertEqual(TESTER.output, output)

    def test_del_snmp_host(self):
        '''
        Test delete snmp host
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><host operation="delete"><ip>10.0.0.1</ip><community>Public</community><udp-p\
ort>161</udp-port></host></snmp-server></config>'

        TESTER.system.del_snmp_host(('10.0.0.1', '161'))
        self.assertEqual(TESTER.output, output)
