import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))

from common import opendata_scraper2

# Change to what you need (remove what you don't)
save_url = [
    ["uof_stats/", "https://opendata.howardcountymd.gov/resource/aas5-u28t.csv"],
    ["cfs/", "https://opendata.howardcountymd.gov/resource/qccx-65fg.csv"],
    ["crime_by_type/", "https://opendata.howardcountymd.gov/resource/hrwk-c83k.csv"],
]

save_folder = "./data/"

opendata_scraper2(save_url, save_folder)
