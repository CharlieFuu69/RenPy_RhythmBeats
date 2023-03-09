## CharlieFuu69
## Ren'Py RhythmBeats!

## Script: Secuencia principal.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

import os, sys, beatmap, utils
import easygui_qt as window

## -------------------------------------------------------------------------------------------------------------- ##
## Secuencia principal

if __name__ == "__main__":
    os.system("color")

    utils.start()

    while True:
        inst = beatmap.BeatmapMaster()
        command = input(f"\n{utils.cyan}[COMANDO]>{utils.end} ")

        try:
            if command in utils.commands:
                task_execute = eval(utils.commands[command])
                task_execute()
            else:
                raise Exception(f"'{utils.cyan}{command}{utils.end}' no es un comando válido para esta herramienta.")

        except Exception as task_error:
            utils.log("Error", str(task_error))

        finally:
            del inst
