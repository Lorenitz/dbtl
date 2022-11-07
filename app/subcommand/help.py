def show_help():
    help = """dbtl allows you to transform data in data warehouses
    usage:
    dbtl [sub-command]

    sub-commands:
        show    Show the transformation that will take place
        lint    Lint SQL files using SQLFluff
        run     Run all transformations
        test    Test transformations in test environment
    """
    print(help)