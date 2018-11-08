import os
import shutil
import sys


def main():
    project_type = '{{ cookiecutter.project_type }}'
    remove_unused_project_files(project_type)
    display_getting_started_instructions(project_type)
    return 0


# TODO: Selected project files based on user choices
def remove_unused_project_files(project_type):
    working_dir = os.path.abspath(os.path.curdir)
    metad_dir = os.path.join(working_dir, 'MetaD')
    pbmetad_dir = os.path.join(working_dir, 'PBMetaD')

    if project_type == 'Classical':
        shutil.rmtree(metad_dir, ignore_errors=True)
        shutil.rmtree(pbmetad_dir, ignore_errors=True)
    elif project_type == 'MetaD':
        shutil.rmtree(pbmetad_dir, ignore_errors=True)
    elif project_type == 'PBMetaD':
        shutil.rmtree(metad_dir, ignore_errors=True)

    return 0


def delete_files(file_list, working_dir):
    for file in file_list:
        full_path = os.path.join(working_dir, file)
        if os.path.exists(full_path):
            os.remove(full_path)
        else:
            print(f'WARNING: could not find file to remove'
                  f'in hook {full_path}.')


# TODO: Display instructions for getting started
def display_getting_started_instructions(project_type):
    print(f'----------------------------------------------------')
    print(f'Your {project_type} simulation project was created!')
    print(f'----------------------------------------------------')
    return


if __name__ == '__main__':
    sys.exit(main())
