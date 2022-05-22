words = input().split()
prefixes = ('https://', 'http://', 'www.')
print('\n'.join([
    address for address in words if address.lower().startswith(prefixes)
]))
