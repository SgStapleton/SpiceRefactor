import pytest

import numpy as np

from ale.base import data_naif

# 'Mock' the spice module where it is imported
from conftest import SimpleSpice

simplespice = SimpleSpice()
data_naif.spice = simplespice

def test_naif_keywords():
    naif_data = data_naif.NaifSpice()
    naif_data.instrument_id = "INSTRUMENT"
    naif_data.target_name = "TARGET"

    assert naif_data._naif_keywords == {'BODY-12345_RADII': np.ones(3),
                                        'INS-12345_PIXEL_SIZE': np.ones(1),
                                        'INS-12345_ITRANSL': np.ones(3),
                                        'INS-12345_ITRANSS': np.ones(3),
                                        'INS-12345_FOCAL_LENGTH': np.ones(1),
                                        'INS-12345_BORESIGHT_LINE': np.ones(1),
                                        'INS-12345_BORESIGHT_SAMPLE': np.ones(1)}
