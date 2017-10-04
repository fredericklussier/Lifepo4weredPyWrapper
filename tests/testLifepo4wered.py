#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../tests')

import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
from lifepo4weredEnum import lifepo4weredEnum

class Lifepo4weredPyWrapperTest(unittest.TestCase):
    """
    canRead
    """
    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testReadAccess_ShouldReturnTrue(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action
        actualValue = lifepo4weredOperations.canRead(lifepo4weredEnum.VBAT)

        # Assert
        self.assertTrue(actualValue)

    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testReadAccess_WhenUnknownEnum_ShouldRaiseError(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action and Assert
        with self.assertRaises(ValueError):
            actualValue = lifepo4weredOperations.canRead(100)

    """
    canWrite
    """
    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testWriteAccess_ShouldReturnTrue(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action
        actualValue = lifepo4weredOperations.canWrite(lifepo4weredEnum.VBAT)

        # Assert
        self.assertTrue(actualValue)

    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testWriteAccess_WhenUnknownEnum_ShouldRaiseError(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action and Assert
        with self.assertRaises(ValueError):
            actualValue = lifepo4weredOperations.canWrite(100)

    """
    Read
    """
    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testRead_ShouldReturnTrue(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action
        actualValue = lifepo4weredOperations.read(lifepo4weredEnum.VBAT)

        # Assert
        self.assertEqual(actualValue, 1)

    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testRead_WhenUnknownEnum_ShouldRaiseError(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action and Assert
        with self.assertRaises(ValueError):
            actualValue = lifepo4weredOperations.read(100)

    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.access_lifepo4wered', return_value = False)
    def testRead_WhenNotAccess_ShouldRaiseError(self, mockedLib):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = False

        # Action and Assert
        with self.assertRaises(RuntimeError):
            actualValue = lifepo4weredOperations.read(lifepo4weredEnum.CFG_WRITE)

    """
    Write
    """
    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testWrite_ShouldReturnTrue(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action
        actualValue = lifepo4weredOperations.write(lifepo4weredEnum.VBAT_SHDN, 12)

        # Assert
        self.assertEqual(actualValue, 12)

    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testWrite_WhenUnknownEnum_ShouldRaiseError(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action and Assert
        with self.assertRaises(ValueError):
            actualValue = lifepo4weredOperations.write(100, 12)

    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.access_lifepo4wered', return_value = False)
    def testWrite_WhenNotAccess_ShouldRaiseError(self, mockedLib):
        # Arrange
        import lifepo4weredOperations

        # Action and Assert
        with self.assertRaises(RuntimeError):
            actualValue = lifepo4weredOperations.write(lifepo4weredEnum.VBAT, 1234)

    @patch('lifepo4weredOperations.lifepo4weredSO', new=mockLifepo4weredSO)
    def testWrite_UnitNotNumber_ShouldRaiseError(self):
        # Arrange
        import lifepo4weredOperations
        #mockLifePO4weredSO.access_lifepo4wered.return_value = True

        # Action and Assert
        with self.assertRaises(TypeError):
            actualValue = lifepo4weredOperations.write(lifepo4weredEnum.VBAT_SHDN, "Now")

if __name__ == '__main__':
    unittest.main()