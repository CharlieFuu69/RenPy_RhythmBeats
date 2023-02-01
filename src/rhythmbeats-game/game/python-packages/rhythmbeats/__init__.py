## CharlieFuu69
## Ren'Py RhythmBeats!

## Script: Inicializador de módulos

################################################################################

import rhythmbeats

## Esto expone de forma global a la clase RhythmPlayground()
RhythmPlayground = rhythmbeats.RhythmPlayground

## Esto comprueba si el módulo ha sido importado en la fase de arranque
if not rhythmbeats.init_flag():
    raise rhythmbeats.RhythmBeatsException(u"Importar \"rhythmbeats.py\" durante la marcha puede provocar errores colaterales en tu juego.\nSe recomienda importar este módulo en la etapa de arranque de tu juego, es decir,\nun bloque \"init python\".")
