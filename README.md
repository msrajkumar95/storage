# storage
Sacumen Assignment

## Steps to run the code
1. Clone the package into your machine.
2. Install the package using ```python3 setup.py install```.
3. Create a configuration file with all required details (refer ```config.yaml```).
4. Create virtual environment and install requirements ```pip install -r requirements.txt```
5. Import required classes ```Config, Storage``` into your python environment
6. Initialize Config class by passing path of configuration file.<br>
```conf = Config('<config_path>')```
7. Initialize Storage class by passing configuration details.<br>
```storage_obj = Storage(conf.config)```
8. Execute ```process_files``` method to load file details by passing files directory.<br>
```storage_obj.process_files('<upload_files_path>')```
9. Execute ```upload_files``` method to upload files into configured cloud storage.<br>
```storage_obj.upload_files()```
10. Execute ```write_config``` to extract configuration into different file types.<br>
```conf.write_config('<format>', '<file_path>')```

OR

5. Use below snippet by changing necessary arguments to execute complete functionality.<br>
```
from storage import Config, Storage

def main():
    conf = Config('<config_path>')
    storage_obj = Storage(conf.config)
    storage_obj.process_files('<upload_files_path>')
    storage_obj.upload_files()
    conf.write_config('<format>', '<file_path>')


main()
```
