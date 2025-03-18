from pathlib import Path
import copy
import yaml
import time
from doe_dap_dl import DAP

SRC = Path(__file__).parent
ROOT = SRC.parent

class A2EAPI:

    def __init__(self, config, data_path=None):
        """ Creates an instance of A2EAPI. """

        print(config)
        self.config = config

    def run(self):
        """ Run method for API. """

        self.a2e = DAP('a2e.energy.gov')
        self.a2e.setup_two_factor_auth(username=self.config['username'],
                                        password='',
                                        authcode=None,
        )

        self.download_files(self.find_missing_files())

    def find_missing_files(self):

        files = self.a2e.search(self.config['filter'])

        list_of_data = [item.name for item in Path(ROOT / "data").iterdir()]

        missing_files = []

        for f in files:
            if f['Filename'] not in list_of_data:
                print(f"{f['Filename']} is not in {Path(ROOT / 'data')}")
                missing_files.append(f)

            else:
                pass

        return missing_files

    def download_files(self, missing_files):
        if missing_files:
            files = self.a2e.download_files(missing_files, path="../data")

        else:
            print(f"All {config['filter']['file_type']} files for dates: "
            f"{config['filter']['date_time']} accounted for in "
            f"{Path(ROOT / 'data')}")

if __name__ == "__main__":

    config_path = Path(ROOT / "config.yaml")
    config = yaml.safe_load(config_path.read_text())

    a2eapi = A2EAPI(config)
    a2eapi.run()









