from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

def init_db():
    # Create indexes if they don't exist
    if not es.indices.exists(index="access_logs"):
        es.indices.create(index="access_logs")
    if not es.indices.exists(index="employees"):
        es.indices.create(index="employees")