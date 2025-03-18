from pathlib import Path
import yaml
import time
from doe_dap_dl import DAP


ROOT = Path(__file__).parent

config = yaml.safe_load(Path(ROOT / "config.yaml").read_text())

print(config)

a2e = DAP('a2e.energy.gov')

a2e.setup_two_factor_auth(username=config['username'],
                          password='',
                          authcode=None,
                          )

filenames = a2e.search(config['filter'])
#[print(f) for f in filenames]

list_of_data = [item.name for item in Path(ROOT / "data").iterdir()]
missing_files = []

#print(sorted(list_of_data))

#start = time.perf_counter()

for f in filenames:
        if f['Filename'] in list_of_data:
            pass
        else:
            print(f"{f['Filename']} is not in {Path(ROOT / 'data')}")
            missing_files.append(f)

#end = time.perf_counter()

if missing_files:
    files = a2e.download_files(missing_files, path="data")

else:
     print(f"All {config['filter']['file_type']} files for dates: "
            f"{config['filter']['date_time']} accounted for in "
            f"{Path(ROOT / 'data')}")
    #a2e.download_with_order(filter, path= ROOT / "data")
