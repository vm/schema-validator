import arrow

def item_check(x, schema):
    """
    Checks if an item follows the proper schema. This is a general function
    which recursively calls itself if potential recursion may occur (when the
    type is a dict or array, because this means there could be nested dicts).
    Otherwise, the function checks if the item is the correct base type.

    If no errors are raised, the schema is properly followed.

    :param x: The item, which can be a dict, list, float, int, bool or str.
    :param schema: The schema which the item should follow.
    """
    if isinstance(x, list):
        for element in x:
            item_check(element, schema.get('items'))
    elif isinstance(x, dict):
        dict_check(x, schema)
    else:
        if not isinstance(x, schema.get('type')):
            raise TypeError('Invalid type based on schema.')
        if schema.get('format') == 'date':
            arrow.get(x)


def dict_check(x, schema):
    """
    :param x: A dict.
    :param schema: The schema which the dict should follow.
    :raises ValueError: If missing required item.
    """
    for required_item in schema.get('required', []):
        if not required_item in x.keys():
            raise ValueError('Missing a required item.')
    for key, value in x.iteritems():
        properties = schema.get('properties')
        if key in properties.keys():
            item_schema = properties.get(key)
        else:
            item_schema = schema.get('additional_properties')
        item_check(value, item_schema)


def validate(schema):
    def wraps(fn):
        def noop(param):
            item_check(param, schema)
            fn(param)
        return noop
    return wraps
