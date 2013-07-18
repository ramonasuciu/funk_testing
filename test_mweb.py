# -*- coding: iso-8859-15 -*-
"""basic_navigation FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
#from funkload.utils import xmlrpc_get_credential


class PerformanceTests(FunkLoadTestCase):
    """These tests use a configuration file PerformanceTests.conf."""

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')
        # XXX here you can setup the credential access like this
        # credential_host = self.conf_get('credential', 'host')
        # credential_port = self.conf_getInt('credential', 'port')
        # self.login, self.password = xmlrpc_get_credential(credential_host,
        #                                                   credential_port,
        #                                                   'members')

    def test_get_home_page(self):
        server_url = self.server_url
        self.get(server_url,
                 description="Get home page")

        #text_to_find = "Expiring Soon"
        #self.assert_(text_to_find in self.getBody(),
        #             "No such text %s found on home page" % text_to_find)

    def test_get_programs_page(self):
        server_url = self.server_url
        self.get(server_url + '/programs/',
                 description="Get programs page")

        #text_to_find = "More Programs"
        #self.assert_(text_to_find in self.getBody(),
        #             "No such text %s found on programs page" % text_to_find)

    def test_see_all_programs(self):
        server_url = self.server_url
        self.get(server_url + '/all-programs-az/',
                 description="Get a-z programs page")

        #text_to_find = "videos"
        #self.assert_(text_to_find in self.getBody(),
        #             "No such text %s found on programs page" % text_to_find)

    def test_get_single_program_page(self):
        server_url = self.server_url
        self.get(server_url + '/program/masterpiece/',
                 description="Get single program page")

        #text_to_find = "As the longest-running primetime drama on American"
        #self.assert_(text_to_find in self.getBody(),
        #             "No such text %s found on Masterpiece program page"
        #             % text_to_find)

    def test_get_single_video_page(self):
        server_url = self.server_url
        self.get(server_url + '/video/2365042061/',
                 description="Get single video page")

        #text_to_find = "Bill Moyers has been following the story"
        #self.assert_(text_to_find in self.getBody(),
        #            "No such text %s on single video page" % text_to_find)

    def test_get_full_episodes(self):
        server_url = self.server_url
        self.get(server_url + '/program/masterpiece/episodes/',
                 description="Get full episodes for Masterpiece program")

    def test_get_clips(self):
        server_url = self.server_url
        self.get(server_url + '/program/masterpiece/shorts/',
                 description="Get clips for Masterpiece program")

    def test_get_previews(self):
        server_url = self.server_url
        self.get(server_url + '/program/masterpiece/shorts/',
                 description="Get previews for Masterpiece program")

    def test_get_local_videos(self):
        # code to simulate localization

        server_url = self.server_url
        self.get(server_url + '/local/',
                 description="Get local videos")

    def test_get_expiring_videos(self):
        server_url = self.server_url
        self.get(server_url + '/expiring/',
                 description="Get expiring videos")

    def test_get_tvschedules(self):
        # code to simulate localization

        server_url = self.server_url
        self.get(server_url + '/schedules/',
                 description="Get TV Schedules page")

    def test_get_search_results(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a',
                 description="Get search results page")

    def test_refine_search_results_by_program(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&program=Chicago%20Tonight',
                 description="Refine search results by program")

    def test_refine_results_by_type_episode(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&type=episode',
                 description="Get refined page")

    def test_refine_results_by_type_clips(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&type=clips',
                 description="Get refined page")

    def test_refine_results_by_type_previews(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&type=promotion',
                 description="Get refined page")

    def test_refine_results_by_10_min(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&length=..600/',
                 description="Get refined page")

    def test_refine_results_by_10_30_min(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&length=601..1800/',
                 description="Get refined page")

    def test_refine_results_by_30_60_min(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&length=1801..3600/',
                 description="Get refined page")

    def test_refine_results_by_over_60_min(self):
        server_url = self.server_url
        a = server_url + '/search/?q=a&length=3601../'
        print a
        self.get(server_url + '/search/?q=a&length=3601../',
                 description="Get refined page")

    def test_sort_results_by_expiring(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&order=expiring/',
                 description="Get sorted page by expiration date")

    def test_sort_results_by_airdate(self):
        server_url = self.server_url
        self.get(server_url + '/search/?q=a&order=airdate/',
                 description="Get sorted page by airdate")

    def tearDown(self):
        """Tearing down test."""
        self.logd("tearDown.\n")


if __name__ in ('main', '__main__'):
    unittest.main()
