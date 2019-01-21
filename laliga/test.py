import pandas as ps
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import numpy as np
import json
df01 = ps.read_json(\"../datasets/playerslabseriesseasonstats.json\")