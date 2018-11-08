import sys


def validate():
    user_name = '{{ cookiecutter.user_name }}'

    if not user_name.strip():
        print("ERROR: you must give a valid user_name to use this template")
        return 1

    project_type = '{{ cookiecutter.project_type }}'
    if project_type in ['MetaD', 'PBMetaD']:
        print(f'Currently {project_type} is not implemented.')
        return 2

    # return 0 if all goes well!
    return 0


if __name__ == '__main__':
    sys.exit(validate())
