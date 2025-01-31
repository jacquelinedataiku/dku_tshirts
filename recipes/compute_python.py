# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
web_last_month_enriched = dataiku.Dataset("web_last_month_enriched")
web_last_month_enriched_df = web_last_month_enriched.get_dataframe()

web_last_month_enriched_df['new_col'] = 1

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

python_df = web_last_month_enriched_df # For this sample code, simply copy input to output


# Write recipe outputs
python = dataiku.Dataset("python")
python.write_with_schema(python_df)
