"""
Custom prompts
"""


def confirm(overwrite):
    """
    Confirm
    :param overwrite:
    :return:
    """
    return not overwrite["overwrite"]


prompt_overwrite = [
    {
        'type': 'confirm',
        'name': 'overwrite',
        'message': 'Path already exists! Do you want to overwrite?',
        'when': lambda overwrite: overwrite.get('overwrite', bool)
    }
]


prompt_rename = [
    {
        'type': 'confirm',
        'name': 'rename',
        'message': 'Would you like to rename root directory?',
        'when': lambda overwrite: overwrite.get('overwrite', bool)
    }
]
