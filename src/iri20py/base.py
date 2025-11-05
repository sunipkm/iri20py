# %%
from __future__ import annotations
from datetime import datetime, UTC
from numbers import Number
import os
from pathlib import Path
import sys
from dataclasses import dataclass
from typing import List, Literal, Optional, Tuple

import numpy as np
from xarray import Dataset

if hasattr(sys, 'ps1'):
    from utils import Singleton, glowdate
    from settings import Settings, ComputedSettings
else:
    from .utils import Singleton, glowdate
    from .settings import Settings, ComputedSettings

DIRNAME = Path(os.path.dirname(__file__))
if hasattr(sys, 'ps1'):
    LIBDIR = DIRNAME / '../../build'
    LIBDIR = LIBDIR.resolve()
    sys.path.append(str(LIBDIR))
    from iri20shim import iri20_init, iri20_eval  # type: ignore
    DATADIR = DIRNAME / '../IRI2020/data'
    DATADIR = DATADIR.resolve()
else:
    from .iri20shim import iri20_init, iri20_eval  # type: ignore
    DATADIR = DIRNAME / "data"
    DATADIR = DATADIR.resolve()


class Iri2020(Singleton):
    def _init(self):
        iri20_init(str(DATADIR))

    def _iricall(self, lat: Number, lon: Number, alt: np.ndarray, year: int, day: int, ut: Number, settings: ComputedSettings) -> Dataset:
        outf = np.zeros((len(alt), 15), dtype=np.float32, order='F')
        alt = alt.astype(np.float32, order='F')
        iri20_eval(settings.jf, 0, lat, lon, year, day, ut, alt, outf, settings.oarr, settings.logfile)
        

    def calculate(self, time: datetime, lat: Number, lon: Number, alt: np.ndarray, settings: Optional[Settings | ComputedSettings] = None) -> Tuple[ComputedSettings, Dataset]:
        if time.tzinfo is not None:
            time = time.astimezone(UTC)
        year, idate, utsec = glowdate(time)
        return self.evaluate(lat, lon, alt, year, idate, utsec, settings)

    def evaluate(self, lat: Number, lon: Number, alt: np.ndarray, year: int, day: int, ut: Number, settings: Optional[Settings | ComputedSettings] = None) -> Tuple[ComputedSettings, Dataset]:
        if settings is None:
            settings = Settings()
        if isinstance(settings, Settings):
            settings = ComputedSettings.from_settings(settings)
        if not isinstance(settings, ComputedSettings):
            raise TypeError(
                "settings must be of type Settings or ComputedSettings")
        ds = self._iricall(lat, lon, alt, year, day, ut, settings)
        return settings, ds
# %%
