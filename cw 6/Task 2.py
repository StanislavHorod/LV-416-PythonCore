def sorter(textbooks):
    return sorted(textbooks, key=lambda c: c.lower() if c.isupper() else c.upper())