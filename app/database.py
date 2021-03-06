# Third party libs
import pymongo

class EventsDB(object):
    db = None

    @classmethod
    def init(cls, app_config):
        try:
            mongo_client = pymongo.MongoReplicaSetClient(app_config['EVENTS_DB_HOST'], replicaSet=app_config['EVENTS_DB_REPLICA_SET'])
        except KeyError:
            mongo_client = pymongo.MongoClient(app_config['EVENTS_DB_HOST'])

        cls.db = mongo_client[app_config['EVENTS_DB_NAME']]

        if app_config.get('EVENTS_DB_USER') and app_config.get('EVENTS_DB_PASSWORD'):
            cls.db.authenticate(app_config['EVENTS_DB_USER'], app_config['EVENTS_DB_PASSWORD'])

