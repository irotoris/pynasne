# pynasne
python wrapper for Nasne's REST API in LAN

## Requirements
* python 3.5 or later

## Install
```
$ python setup.py install
```

## Usage
Run script in intranet
```
import pynasne

nasne = pynasne.Nasne('192.168.11.12')

# get json of REC titles
nasne.get_title_list()

# get json of HDD total, usage and free volume size
nasne.get_hdd_usage_info()

# get json of REC errors
nasne.get_rec_ng_list()
```

## License
MIT
