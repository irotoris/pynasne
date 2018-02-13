# -*- coding: utf-8 -*-

import os
from nose.tools import raises
from requests.exceptions import RequestException
from mock import patch
from pynasne import Nasne, NasneAPIException

class TestNasne():

    def __init__(self):
        self.nasne = Nasne(os.getenv('NASNE_IPADDRESS'))

    def setup(self):
        self.nasne = Nasne(os.getenv('NASNE_IPADDRESS'))

    @raises(RequestException)
    def test_call_get_api_with_error(self):
        self.nasne = Nasne('127.0.0.1')
        self.nasne._call_get_api('80', '/')

    @raises(NasneAPIException)
    def test_call_get_api_with_http404(self):
        self.nasne = Nasne('google.co.jp')
        self.nasne._call_get_api('80', '/aaaa')

    def test_get_box_name(self):
        res = self.nasne.get_box_name()
        assert 'name' in res

    def test_box_status_list(self):
        res = self.nasne.get_box_status_list()
        assert 'powerStatus' in res

    def test_title_list(self):
        res = self.nasne.get_title_list()
        assert 'item' in res

    def test_get_hdd_list(self):
        res = self.nasne.get_hdd_list()
        assert 'HDD' in res

    def test_get_hdd_info(self):
        res = self.nasne.get_hdd_info(0)
        assert 'HDD' in res

    def test_get_hdd_usage_info(self):
        res = self.nasne.get_hdd_usage_info()
        assert isinstance(res, dict)

    def test_rec_ng_list(self):
        res = self.nasne.get_rec_ng_list()
        assert 'number' in res

    def test_get_reserved_title_list(self):
        res = self.nasne.get_reserved_title_list()
        assert 'item' in res

    def test_convert_item(self):
        api_res = {
            'item': [
                {'title': '\ue0fd'},
                {'title': '\ue0fe'},
                {'title': '\ue0ff'},
                {'title': '\ue180'},
                {'title': '\ue182'},
                {'title': '\ue183'},
                {'title': '\ue184'},
                {'title': '\ue185'},
                {'title': '\ue18c'},
                {'title': '\ue18d'},
                {'title': '\ue190'},
                {'title': '\ue191'},
                {'title': '\ue192'},
                {'title': '\ue193'},
                {'title': '\ue194'},
                {'title': '\ue195'},
                {'title': '\ue196'},
                {'title': '\ue19c'}
            ]
        }
        converted_item = [
            {'title': '[手]'},
            {'title': '[字]'},
            {'title': '[双]'},
            {'title': '[デ]'},
            {'title': '[二]'},
            {'title': '[多]'},
            {'title': '[解]'},
            {'title': '[SS]'},
            {'title': '[映]'},
            {'title': '[無]'},
            {'title': '[前]'},
            {'title': '[後]'},
            {'title': '[再]'},
            {'title': '[新]'},
            {'title': '[初]'},
            {'title': '[終]'},
            {'title': '[生]'},
            {'title': '[他]'}
        ]
        res = self.nasne._convert_item(api_res)
        assert res['item'] == converted_item

    def test_convert_item_with_error(self):
        with patch('logging.Logger.warning') as m:
            api_res = {}
            res = self.nasne._convert_item(api_res)
            m.assert_called_with('Not found title name')
