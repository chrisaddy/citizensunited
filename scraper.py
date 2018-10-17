import numpy as np
import pandas as pd

def phetch_philly(url: str) -> pd.DataFrame:
    """Get all year-to-date-transactions for a given year (currently a full url) in data frame form."""

    return pd.read_csv(url, sep = '\t', encoding = 'latin1', low_memory=False)

