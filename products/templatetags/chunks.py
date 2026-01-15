from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    """
    Break a list into chunks of size 'chunk_size'.
    Returns a list of lists.
    """
    chunk_size = int(chunk_size)
    if not list_data:
        return []

    result = []
    chunk = []
    i = 0
    for item in list_data:
        chunk.append(item)
        i += 1
        if i == chunk_size:
            result.append(chunk)
            chunk = []
            i = 0
    if chunk:
        result.append(chunk)
    return result
