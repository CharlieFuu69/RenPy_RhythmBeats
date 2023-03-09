## CharlieFuu69
## Ren'Py RhythmBeats!

## Script: Customizaciones para la herramienta de conversión.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

## Colores para el texto en el terminal
def colorize(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"

red = colorize(255, 0, 0)
green = colorize(0, 255, 0)
blue = colorize(0, 0, 255)
cyan = colorize(0, 255, 255)
yellow = colorize(255, 255, 0)
yellow_rbs = colorize(204, 255, 0)
purple = colorize(255, 0, 255)
white = colorize(255, 255, 255)
end = f"\x1b[0m"


## Formato común para imprimir actividades del programa
def log(level = "Task", msg = ""):
    lvtext = {
            "Task" : f"[  {white}Task{end}  ]",
            "OK" : f"[   {green}OK{end}   ]",
            "Error" : f"[ {red}Failed{end} ]"}

    print(f"%s {msg}" % (lvtext[level]))


## -------------------------------------------------------------------------- ##
## Mensaje de inicio/ayuda

def start():
    print(f"""{yellow_rbs}
=======================================================================================================
                                        Ren'Py RhythmBeats!
                             Herramienta CLI de conversión MIDI a Beatmap
                                 © 2023 CharlieFuu69 - GNU GPL v3.0
======================================================================================================={end}

{yellow_rbs}Comandos de trabajo:{end}
|   -> {cyan}convert{end}: Convierte un archivo MIDI a un beatmap con un formato legible
|                para el sistema rítmico.
|   -> {cyan}read{end}   : Abre un archivo MIDI o un beatmap (BEAT) en modo de solo lectura para
|                mostrar las estadísticas del beatmap.
|   -> {cyan}exit{end}   : Cierra la herramienta (o puedes cerrar la ventana directamente).

Si tienes dudas, consulta el tutorial completo aquí:
{yellow_rbs}https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/docs/doc_section_05.md{end}
""")


commands = {"convert" : "inst.write_map",
            "read" : "inst.read_map",
            "exit" : "sys.exit"}
