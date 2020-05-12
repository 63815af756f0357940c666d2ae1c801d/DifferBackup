import os
import ruamel.yaml as yaml


def load_config(config_folder='config', config_filename='differ_backup.yml'):
    if not os.path.exists(config_folder):
        os.mkdir(config_folder)
    config_data = {}
    config_full_name = os.path.join(config_folder, config_filename)
    if not os.path.exists(config_full_name):
        f = open(config_full_name, 'w')
        config_data['backup_folder'] = 'differ_backup'
        config_data['server_folder'] = 'server'
        config_data['backup_paths'] = ['world', 'world_nether', 'world_the_end']
        yaml.dump(config_data, f)
        f.close()


def list_all_folder(folder_name: str, list_file: bool = True) -> list:
    all_things = os.listdir(folder_name)
    result = []
    if list_file:
        for sth in all_things:
            new_path = os.path.join(folder_name, sth)
            result.append(new_path)
            if os.path.isdir(new_path):
                result.extend(list_all_folder(new_path, list_file))
    else:
        for sth in all_things:
            new_path = os.path.join(folder_name, sth)
            if os.path.isdir(new_path):
                result.append(new_path)
                result.extend(list_all_folder(new_path))
    return result
