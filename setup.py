import cx_Freeze

executables = [cx_Freeze.Executable("TicTacToe.py")]

cx_Freeze.setup(
    name="tictactoe",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["python.png"]}},
    executables = executables

    )
