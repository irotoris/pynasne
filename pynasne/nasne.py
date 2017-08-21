# -*- coding: utf-8 -*-

import requests
import logging

logger = logging.getLogger('pynasne')


class NasneAPIException(Exception):
    pass


class Nasne():

    def __init__(self, nasne_ip, timeout=5):
        self._nasne_ip = nasne_ip
        self._headers = {"content-type": "application/json"}
        self._timeout = timeout

    def _call_get_api(self, port, path, payload=None):
        url = 'http://{}:{}{}'.format(self._nasne_ip, port, path)
        try:
            res = requests.get(url, params=payload, headers=self._headers, timeout=self._timeout)
        except requests.exceptions.RequestException as e:
            logger.error('Nasne http get request is failed. {}'.format(url))
            raise e
        if res.status_code != 200:
            raise NasneAPIException('Nasne http get request is failed. {}, status code:{}'.format(url, res.status_code))
        return res

    def get_title_list(self):
        payload = {
            'searchCriteria': 0,
            'filter': 0,
            'startingIndex': 0,
            'requestedCount': 0,
            'sortCriteria': 0,
            'withDescriptionLong': 1,
            'withUserData': 0
        }
        res = self._call_get_api(port='64220', path='/recorded/titleListGet', payload=payload)
        return res.json()

    def get_hdd_list(self):
        res = self._call_get_api(port='64210', path='/status/HDDListGet')
        return res.json()

    def get_hdd_info(self, hdd_id):
        payload = {
            'id': hdd_id,
        }
        res = self._call_get_api(port='64210', path='/status/HDDInfoGet', payload=payload)
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
        res = self._call_get_api(port='64210', path='/status/recNgListGet')
        return res.json()

    def get_reserved_title_list(self):
        payload = {
            'searchCriteria': 0,
            'filter': 0,
            'startingIndex': 0,
            'requestedCount': 0,
            'sortCriteria': 0,
            'withDescriptionLong': 1,
            'withUserData': 0
        }
        res = self._call_get_api(port='64220', path='/schedule/reservedListGet', payload=payload)
        return res.json()
