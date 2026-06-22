# test_zerogrid.py
"""
Tests for ZeroGrid module.
"""

import unittest
from zerogrid import ZeroGrid

class TestZeroGrid(unittest.TestCase):
    """Test cases for ZeroGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZeroGrid()
        self.assertIsInstance(instance, ZeroGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZeroGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
