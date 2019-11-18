import cx_Freeze

executables = [cx_Freeze.Executable("TicTacToe.py")]

cx_Freeze.setup(
    name="TicTacToe",
    options={"build_exe": {"packages":["pygame"]
                           }},
    executables = executables

    )