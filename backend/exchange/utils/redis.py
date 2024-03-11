from django.core.cache import cache

EXCHANGE_CACHE_KEY = "exchanges"


def empty_cache(key):
    cache.set(key, {}, timeout=None)


def get_exchanges():
    val = cache.get(EXCHANGE_CACHE_KEY)
    if not val:
        cache.set(EXCHANGE_CACHE_KEY, {}, timeout=None)
        val = cache.get(EXCHANGE_CACHE_KEY)
    return val


def check_pk_key(obj, pk):
    view_count = obj.get(pk, None)
    if not view_count:
        ...
        # obj.update({pk: 1})
    else:
        ...
        # obj.update({pk: view_count+1 })
    return obj


def set_exchange(obj):
    cache.set(EXCHANGE_CACHE_KEY, obj, timeout=None)
