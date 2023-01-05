## CharlieFuu69
## Ren'Py RhythmBeats!

## Código fuente de la herramienta de conversión "beatmap.exe"
## Python v3.10.4

## ----------------------------------------------------------------------------------------------------------- ##

import pretty_midi as pm
import itertools, csv, sys, os
import easygui_qt as window
from tabulate import tabulate

## ----------------------------------------------------------------------------------------------------------- ##
## Colores para el texto en el terminal

def color_palette(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"

red = color_palette(255, 0, 0)
green = color_palette(0, 255, 0)
blue = color_palette(0, 0, 255)
cyan = color_palette(0, 255, 255)
yellow = color_palette(255, 255, 0)
purple = color_palette(255, 0, 255)
white = color_palette(255, 255, 255)
end = f"\x1b[0m"

## Formato común para imprimir actividades del programa
def log(level = "Process", msg = ""):
    color_per_level = {
                "Process" : white,
                "Build" : yellow,
                "OK" : green,
                "Error" : red}

    level = f"%s[{level}]{end}" % (color_per_level[level])

    print(f"{level} {msg}")

## -------------------------------------------------------------------------------------------------------------- ##

class BeatmapMaster:

    def __init__(self):
        self.tracks = {}

    ## ----------------------------------------------------------------------------------------------------------- ##
    def open_midi(self, fn):
        """Procesa las secuencias de archivos MIDI y crea listas de timestamps según los Pitchs
        detectados."""

        timestamps = []
        pitchs_detected = []

        ## Abre el archivo MIDI
        log("Process", f"Procesando MIDI ({fn})...")
        data = pm.PrettyMIDI(fn)

        ## Detecta los pitchs, que para el sistema rítmico se traduce en la cantidad de
        ## pistas visibles en el juego.
        log("Process", "Detectando pitchs (posibles tracks de notas)...")
        for inst in data.instruments:
            for note in inst.notes:
                if not note.pitch in pitchs_detected:
                    print(f"|   - Pitch detectado: {red}{note.pitch}{end}.")
                    pitchs_detected.append(note.pitch)
                timestamps.append(note)

        print("")

        ## La cascada (Waterfall) se construirá SOLO si se detectaron 2 pitchs.
        if len(pitchs_detected) < 3:
            self.tracks.update({pitchs_detected[0] : [], pitchs_detected[1] : []})

            log("Build", "Construyendo el waterfall...")
            for now_note in timestamps:
                self.tracks[now_note.pitch].append(now_note.start)

            return pitchs_detected

        else:
            raise Exception("Conversión abortada. Se detectaron más de 2 pitchs en la secuencia MIDI.")


    ## ----------------------------------------------------------------------------------------------------------- ##
    def open_beatmap(self, fn):
        """Abre un archivo de beatmap y procesa sus timestamps para obtener sus estadísticas."""

        self.tracks.update({"left" : [], "right" : []})

        with open(fn, "r") as beatmap:
            data = csv.DictReader(beatmap, delimiter = "|", quotechar= "|", quoting=csv.QUOTE_MINIMAL)

            for column in data:
                if column["Keypad_L"] != "End":
                    self.tracks["left"].append(float(column["Keypad_L"]))
                if column["Keypad_R"] != "End":
                    self.tracks["right"].append(float(column["Keypad_R"]))

            beatmap.close()


    ## ----------------------------------------------------------------------------------------------------------- ##
    def read_map(self):
        """Abre archivos MIDI o BEAT en modo de solo lectura para obtener sus estadísticas."""

        track_L = []
        track_R = []

        log("Process", "Solicitando archivo de secuencias MIDI/BEAT...")
        fn = window.get_file_name(title = "Abrir archivo MIDI o BEAT", filetype = "Archivos MIDI/BEAT (*.mid; *.beat)")

        if len(fn) == 0:
            raise Exception("No has seleccionado ningún archivo MIDI/BEAT.")

        if fn.endswith(".mid"):
            log("OK", "Se detectó una secuencia MIDI. Procediendo con el análisis...")
            pitchs = self.open_midi(fn)
            track_L = self.tracks[pitchs[0]]
            track_R = self.tracks[pitchs[1]]

        elif fn.endswith(".beat"):
            log("OK", "Se detectó un archivo BEAT. Procesando beatmap...")
            self.open_beatmap(fn)
            track_L = self.tracks["left"]
            track_R = self.tracks["right"]

        else:
            raise Exception("Se seleccionó un archivo con una extensión no válida para esta herramienta.")


        log("OK", "Secuencias analizadas correctamente.")
        print(f"\n{white}Estadísticas:{end}")
        print(f"|   -> {cyan}Track L:{end} %s" % len(track_L))
        print(f"|   -> {cyan}Track R:{end} %s" % len(track_R))
        print(f"|   -> {purple}Full Combo:{end} %s" % (len(track_L) + len(track_R)))


        choice = input(f"\n{yellow}¿Mostrar listas de timestamps? (Y/N):{end} ")

        if choice.lower() == "y":
            print(tabulate(
                [(l, r) for l, r in itertools.zip_longest(track_L, track_R, fillvalue = "End")],
                headers = (f"{cyan}Pista L{end}", f"{cyan}Pista R{end}"),
                showindex = True,
                tablefmt = "simple_outline"))


    ## ----------------------------------------------------------------------------------------------------------- ##
    def write_map(self):
        """Realiza el proceso de conversión de MIDI a Beatmap.
        Solo permite detectar 2 pitchs, pues el sistema rítmico solo posee 2 pistas en la
        cascada visual de notas durante el juego."""

        log("Process", "Solicitando archivo MIDI...")

        ## Obtiene la ruta del archivo MIDI
        fn = window.get_file_name(title = "Abrir archivo MIDI", filetype = "Archivos MIDI (*.mid)")

        if len(fn) == 0:
            raise Exception("No has seleccionado ningún archivo MIDI.")

        ## Procesa el archivo MIDI y abre una ventana para guardar el archivo de beatmap.
        pitchs = self.open_midi(fn)

        ## Guarda el beatmap basado en formato CSV
        log("Process", "Guardando archivo Beatmap...")
        savefn = window.get_save_file_name(title = "Guardar beatmap como...", filetype = "Archivos BEAT (*.beat)")

        if len(savefn) == 0:
            raise Exception("No se seleccionó ninguna ruta para guardar el beatmap.")

        else:
            with open(savefn[0], "w") as beatmap:
                w_object = csv.writer(beatmap, delimiter = "|", quotechar= "|", quoting=csv.QUOTE_MINIMAL)
                w_object.writerow(["Keypad_L", "Keypad_R"])

                for l_time, r_time in list(itertools.zip_longest(self.tracks[pitchs[0]], self.tracks[pitchs[1]], fillvalue = "End")):
                    w_object.writerow([l_time, r_time])

                beatmap.close()

            log("OK", "Beatmap construido.")
            print(f"|   -> {cyan}Ruta de guardado:{end} %s\n" % savefn[0])
            print(f"{white}Estadísticas:{end}")
            print(f"|   -> {cyan}Track L:{end} %s" % len(self.tracks[pitchs[0]]))
            print(f"|   -> {cyan}Track R:{end} %s" % len(self.tracks[pitchs[1]]))
            print(f"|   -> {purple}Full Combo:{end} %s" % (len(self.tracks[pitchs[0]]) + len(self.tracks[pitchs[1]])))


## -------------------------------------------------------------------------------------------------------------- ##
## Mensaje de inicio/ayuda

def main_msg(advert = None):
    print(f"{yellow}=======================================================================================================")
    print(f"                                        Ren'Py RhythmBeats!                                            ")
    print("                             Herramienta CLI de conversión MIDI a beatmaps                              ")
    print(f"                            © CharlieFuu69 - Creative Commons CC-BY-SA v4.0                             ")
    print(f"======================================================================================================={end}\n")

    if advert:
        log("Error", advert)

        print(f"\nUso en el terminal: {white}beatmap{end} {cyan}<comando>{end}\n")
        print(f"{yellow}Comandos de trabajo:{end}")
        print(f"|   -> {cyan}/convert{end}: Convierte un archivo MIDI a un beatmap con un formato legible")
        print(f"|               para el sistema rítmico.")
        print(f"|   -> {cyan}/read{end}   : Abre un archivo MIDI o un beatmap (BEAT) en modo de solo lectura para")
        print(f"|               mostrar las estadísticas juego posibles.\n")

        print(f"Si tienes dudas, consulta el tutorial completo aquí:\n{green}https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/TUTORIAL_BEATMAPS.md{end}")


## -------------------------------------------------------------------------------------------------------------- ##
## Secuencia principal

if __name__ == "__main__":
    os.system("color")
    inst = BeatmapMaster()

    try:
        if len(sys.argv) == 2:
            if sys.argv[1] == "/read":
                main_msg()
                inst.read_map()
            elif sys.argv[1] == "/convert":
                main_msg()
                inst.write_map()
            else:
                main_msg(f"Woops! Al parecer, escribiste un comando no válido para la herramienta: {red}%s{end}." % sys.argv[1])
        else:
            main_msg("Woops! Creo que ejecutaste el EXE directamente. Debes usarlo desde el terminal (CMD).")
            os.system("pause")

    except Exception as terminal_error:
        log("Error", str(terminal_error))
        window.show_message(
                    title = "Ocurrió un error durante el proceso - Ren'Py RhythmBeats!",
                    message = f"Error: {terminal_error}")
