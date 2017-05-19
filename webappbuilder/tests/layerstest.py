# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
import unittest
import sys
import utils
import os

try:
    from qgis.core import QGis
except ImportError:
    from qgis.core import Qgis as QGis

from utils import *


class LayersTest(unittest.TestCase):

    def setUp(self):
        if QGis.QGIS_VERSION_INT < 21500:
            utils.loadTestProject("layers-2.14")
        else:
            utils.loadTestProject("layers")

    def testLocalRasterLayer(self):
        """Check that raster layers processed correctly"""
        folder = createAppFromTestAppdef("localraster")
        appFile = os.path.join(folder, "webapp", "app_prebuilt.js")
        self.assertTrue(compareWithExpectedOutputFile(appFile, "layers_localraster.js"))

    def testWMSLayer(self):
        """Check that WMS layers processed correctly"""
        folder = createAppFromTestAppdef("layerwms")
        appFile = os.path.join(folder, "webapp", "app_prebuilt.js")
        self.assertTrue(compareWithExpectedOutputFile(appFile, "layers_wms.js"))

    def testLayerGroup(self):
        """Check that groups of layers processed correctly"""
        folder = createAppFromTestAppdef("layergroup")
        appFile = os.path.join(folder, "webapp", "app_prebuilt.js")
        self.assertTrue(compareWithExpectedOutputFile(appFile, "layers_layergroup.js"))

    def testMultipleBaseLayers(self):
        """Check that base and overlay layers processed correctly"""
        folder = createAppFromTestAppdef("multiplebaselayers")
        appFile = os.path.join(folder, "webapp", "app_prebuilt.js")
        self.assertTrue(compareWithExpectedOutputFile(appFile, "layers_multiplebaselayers.js"))

    def testPopups(self):
        """Check that popups can be added"""
        folder = createAppFromTestAppdef("popupsonhover")
        appFile = os.path.join(folder, "webapp", "app_prebuilt.js")
        self.assertTrue(checkTextInFile(appFile, 'popupInfo: "<b>n</b>: [n]"'))

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(LayersTest, 'test'))
    return suite

def run_tests():
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite())
