# coding: utf-8
import nose
from unittest import TestCase
from staticbl import gen_slug

class TestStaticbl(TestCase):

    def test_restat_return_value(self):
        assert gen_slug(u'Привет') == 'privet'

nose.main()