# %%
import os
from pathlib import Path
import sys

if hasattr(sys, 'ps1'):
    from utils import Singleton
else:    
    from .utils import Singleton

DIRNAME = Path(os.path.dirname(__file__))
if hasattr(sys, 'ps1'):
    LIBDIR = DIRNAME / '../../build'
    LIBDIR = LIBDIR.resolve()
    sys.path.append(str(LIBDIR))
    from iri20shim import iri20_init, iri20_eval
    DATADIR = DIRNAME / '../IRI2020/data'
    DATADIR = DATADIR.resolve()
else:
    from .iri20shim import iri20_init, iri20_eval
    DATADIR = DIRNAME / "data"
    DATADIR = DATADIR.resolve()


class Iri2020(Singleton):
    def _init(self):
        iri20_init(str(DATADIR))
    
    
# %%
