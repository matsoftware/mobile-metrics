#!/usr/bin/env python3
from typing import List,Dict

class DataSourcing(object):
    
    def fetch_raw_app_size(self) -> List[Dict]:
        raise NotImplementedError

    def fetch_code_metrics(self) -> List[Dict]:
        raise NotImplementedError
