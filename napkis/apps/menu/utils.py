
import datetime , re, hmac, redis, hashlib

from django.utils import simplejson

from napkis.settings import SECRET_KEY, REDIS_PORT

REDIS = redis.StrictRedis(host='127.0.0.1', port=REDIS_PORT, db=0)

def pubLog(msg=''):
    """ sends log statement to node so you can monitor live
        logs from node in terminal.
    """
    REDIS.publish(0,simplejson.dumps({'TYPE':'log', 'log':msg}))
    return msg