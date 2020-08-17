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