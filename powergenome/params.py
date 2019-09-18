"""
Parameters and settings
"""

from pathlib import Path
from powergenome import __file__

# Not convinced this is the best way to set folder paths but it works!
powergenome_path = Path(__file__).parent
project_path = powergenome_path.parent

DATA_PATHS = {}
DATA_PATHS["results"] = project_path / "results"
DATA_PATHS['powergenome'] = project_path / "powergenome"
DATA_PATHS['data'] = project_path / 'data'
DATA_PATHS['ipm_shapefiles'] = DATA_PATHS['data'] / "IPM Regions v617 04-05-17"
DATA_PATHS['tests'] = project_path / 'tests'
DATA_PATHS['test_data'] = DATA_PATHS['tests'] / 'data'

IPM_SHAPEFILE_PATH = DATA_PATHS['ipm_shapefiles'] / "IPM_Regions_201770405.shp"
IPM_GEOJSON_PATH = DATA_PATHS['data'] / "ipm_regions_simple.geojson"