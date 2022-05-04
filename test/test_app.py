
import unittest
# from unittest.mock import Mock, patch

from mypackage.app import MyApp


class TestApp(unittest.TestCase):
  def test_do_plus(self):
    self.assertEqual(MyApp.do_plus(1, 1), 2)

  def test_do_minus(self):
    self.assertEqual(MyApp.do_minus(1, 1), 0)

  @unittest.skip("skip failing test")
  def test_fail(self):
    self.assertEqual(1, 2)

