
## code created by rank Valcarcel https://github.com/frankV/twenty-pelican-html5up
def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'