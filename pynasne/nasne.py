# -*- coding: utf-8 -*-

import requests
import logging

logger = logging.getLogger('Nasne')


class Nasne():
    _nasen_ip = None
    _headers = {"content-type": "application/json"}

    def __init__(self, nasne_ip):
        self._nasne_ip = nasne_ip

    def _call_api(self, req_url, payload=None):
        try:
            res = requests.get(req_url, params=payload, headers=self._headers)
        except requests.exceptions.RequestException as e:
            logger.error('Nasne http request is failed. {}'.format(req_url))
            raise e
        return res

    def get_title_list(self):
        req_url = 'http://{}:64220/recorded/titleListGet'.format(self._nasne_ip)
        payload = {
            'searchCriteria': 0,
            'filter': 0,
            'startingIndex': 0,
            'requestedCount': 0,
            'sortCriteria': 0,
            'withDescriptionLong': 1,
            'withUserData': 0
        }
        res = self._call_api(req_url=req_url, payload=payload)
        return res.json()

    def get_hdd_list(self):
        req_url = 'http://{}:64210/status/HDDListGet'.format(self._nasne_ip)
        res = self._call_api(req_url=req_url)
        return res.json()

    def get_hdd_info(self, hdd_id):
        req_url = 'http://{}:64210/status/HDDInfoGet'.format(self._nasne_ip)
        payload = {
            'id': hdd_id,
        }
        res = self._call_api(req_url=req_url, payload=payload)
        return res.json()

    def get_hdd_usage_info(self):
        hdds = self.get_hdd_list()
        total_vol = 0
        usage_vol = 0
        free_vol = 0
        for num in range(hdds['number']):
            hdd_info = self.get_hdd_info(hdd_id=num)
            if hdd_info['HDD']['registerFlag'] == 1:
                total_vol = total_vol + hdd_info['HDD']['totalVolumeSize']
                usage_vol = usage_vol + hdd_info['HDD']['usedVolumeSize']
                free_vol = free_vol + hdd_info['HDD']['freeVolumeSize']
        return {
            'total_vol': total_vol,
            'usage_vol': usage_vol,
            'free_vol': free_vol
        }

    def get_rec_ng_list(self):
        req_url = 'http://{}:64210/status/recNgListGet'.format(self._nasne_ip)
        res = self._call_api(req_url=req_url)
        return res.json()

    def get_reserved_title_list(self):
        req_url = 'http://{}:64220/schedule/reservedListGet'.format(self._nasne_ip)
        payload = {
            'searchCriteria': 0,
            'filter': 0,
            'startingIndex': 0,
            'requestedCount': 0,
            'sortCriteria': 0,
            'withDescriptionLong': 1,
            'withUserData': 0
        }
        res = self._call_api(req_url=req_url, payload=payload)
        return res.json()
