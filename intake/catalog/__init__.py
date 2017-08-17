from .local import LocalCatalog
from .remote import RemoteCatalog

def load_catalog(uri):
    '''Returns a Catalog object read from filename'''

    if uri.startswith('tcp://'):
        return RemoteCatalog(uri)
    else:
        return LocalCatalog(uri)
