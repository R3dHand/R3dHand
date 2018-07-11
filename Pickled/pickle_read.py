import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# Format data frame output
pd.set_option('display.height', -1)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'left')

print(.head())
