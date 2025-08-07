from elasticsearch import Elasticsearch
from datetime import datetime

class ESClient:
    def __init__(self):
        self.es = Elasticsearch(['http://localhost:9200'])
        
    def log_access(self, employee_id, confidence, status):
        doc = {
            'timestamp': datetime.utcnow(),
            'employee_id': employee_id,
            'confidence': float(confidence),
            'status': status
        }
        self.es.index(index='access_logs', document=doc)
        
    def get_recent_access(self, limit=10):
        query = {
            "query": {"match_all": {}},
            "size": limit,
            "sort": [{"timestamp": {"order": "desc"}}]
        }
        return self.es.search(index='access_logs', body=query)