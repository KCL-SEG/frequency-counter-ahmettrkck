"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        item_str = str(item)
        frequencies[item_str] = frequencies.get(item_str, 0) + 1
    
    return frequencies
