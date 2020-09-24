# Import Pytest Package
import pytest

from solution import alternatingCharacters

def test_result():
    assert alternatingCharacters("AABBAB") == 2