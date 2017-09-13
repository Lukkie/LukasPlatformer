from cx_Freeze import setup, Executable

base = None


executables = [Executable("main.py", base=base)]

packages = ["pygame"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Cafeetje",
    options = options,
    version = "1.0.0",
    description = 'Platformer van Lukas',
    executables = executables
)