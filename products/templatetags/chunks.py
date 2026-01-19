from django import template

# Create a template library instance
register = template.Library()

# ----------------------------
# Custom Template Filter: chunks
# ----------------------------
@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    """
    Break a list into smaller chunks of size 'chunk_size'.
    Useful for displaying items in rows (like products in a grid).
    Returns a list of lists.
    """

    # Convert chunk_size to integer (template values are strings)
    chunk_size = int(chunk_size)

    # If list is empty or None, return empty list
    if not list_data:
        return []

    result = []     # Final list of chunks
    chunk = []      # Temporary list to store each chunk
    i = 0           # Counter for items in current chunk

    # Loop through all items in the list
    for item in list_data:
        chunk.append(item)
        i += 1

        # When chunk reaches required size
        if i == chunk_size:
            result.append(chunk)  # Add chunk to result
            chunk = []            # Reset chunk
