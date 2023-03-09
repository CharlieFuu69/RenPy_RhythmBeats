## CharlieFuu69
## Ren'Py RhythmBeats!

## Script: Clase de conversión y lectura de beatmaps.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

import pretty_midi as pm
import itertools, csv, sys, os, utils
import easygui_qt as window
from tabulate import tabulate

## -------------------------------------------------------------------------- ##

class BeatmapMaster:

    def __init__(self):
        self.tracks = {}

    ## ------------}--------------------------------------------------------- ##
    def open_midi(self, fn):
        """Procesa las secuencias de archivos MIDI y crea listas de timestamps
        según los Pitchs detectados."""

        timestamps = []
        pitchs_detected = []

        ## Abre el archivo MIDI
        utils.log("Task", f"Procesando MIDI ({fn})...")
        data = pm.PrettyMIDI(fn)

        ## Detecta los pitchs, que para el sistema rítmico se traduce en la cantidad de
        ## pistas visibles en el juego.
        utils.log("Task", "Detectando pitchs (posibles tracks de notas)...")
        for inst in data.instruments:
            for note in inst.notes:
                if not note.pitch in pitchs_detected:
                    print(f"           Pitch detectado: {utils.red}{note.pitch}{utils.end}.")
                    pitchs_detected.append(note.pitch)
                timestamps.append(note)

        ## La cascada (Waterfall) se construirá SOLO si se detectaron 2 pitchs.
        if len(pitchs_detected) < 3:
            self.tracks.update({pitchs_detected[0] : [], pitchs_detected[1] : []})

            utils.log("Task", "Construyendo el waterfall...")
            for now_note in timestamps:
                self.tracks[now_note.pitch].append(now_note.start)

            return pitchs_detected

        else:
            raise Exception("Conversión abortada. Se detectaron más de 2 pitchs en la secuencia MIDI.")


    ## ---------------------------------------------------------------------- ##
    def open_beatmap(self, fn):
        """Abre un archivo de beatmap y procesa sus timestamps para obtener sus
        estadísticas."""

        self.tracks.update({"left" : [], "right" : []})

        with open(fn, "r") as beatmap:
            data = csv.DictReader(beatmap,
                                delimiter = "|",
                                quotechar= "|",
                                quoting=csv.QUOTE_MINIMAL)

            for column in data:
                if column["Keypad_L"] != "End":
                    self.tracks["left"].append(float(column["Keypad_L"]))
                if column["Keypad_R"] != "End":
                    self.tracks["right"].append(float(column["Keypad_R"]))

            beatmap.close()


    ## ---------------------------------------------------------------------- ##
    def read_map(self):
        """Abre archivos MIDI o BEAT en modo de solo lectura para obtener sus
        estadísticas."""

        track_L = []
        track_R = []

        utils.log("Task", "Solicitando archivo de secuencias MIDI/BEAT...")
        fn = window.get_file_name(title = "Abrir archivo MIDI o BEAT",
                                filetype = "Archivos MIDI/BEAT (*.mid; *.beat)")

        if len(fn) == 0:
            raise Exception("No has seleccionado ningún archivo MIDI/BEAT.")

        if fn.endswith(".mid"):
            utils.log("OK", "Se detectó una secuencia MIDI. Procediendo con el análisis...")
            pitchs = self.open_midi(fn)
            track_L = self.tracks[pitchs[0]]
            track_R = self.tracks[pitchs[1]]

        elif fn.endswith(".beat"):
            utils.log("OK", "Se detectó un archivo BEAT. Procesando beatmap...")
            self.open_beatmap(fn)
            track_L = self.tracks["left"]
            track_R = self.tracks["right"]

        else:
            raise Exception("Se seleccionó un archivo con una extensión no válida para esta herramienta.")


        utils.log("OK", "Secuencias analizadas correctamente.")

        notes_left = len(track_L)
        notes_right = len(track_R)
        full_combo = notes_left + notes_right

        print(f"""
\n{utils.white}Estadísticas:{utils.end}
|   -> {utils.cyan}Pista L:{utils.end} {notes_left} notas.
|   -> {utils.cyan}Pista R:{utils.end} {notes_right} notas.
|   -> {utils.purple}Full Combo:{utils.end} {full_combo} notas.
""")


        choice = input(f"\n{utils.yellow_rbs}¿Mostrar tabla de timestamps? (Y/N):{utils.end} ")

        if choice.lower() == "y":
            print(tabulate(
                [(l, r) for l, r in itertools.zip_longest(track_L, track_R, fillvalue = "End")],
                headers = (f"{utils.cyan}Pista L{utils.end}", f"{utils.cyan}Pista R{utils.end}"),
                showindex = True,
                tablefmt = "simple_outline"))


    ## ---------------------------------------------------------------------- ##
    def write_map(self):
        """Realiza el proceso de conversión de MIDI a Beatmap.
        Solo permite detectar 2 pitchs, pues el sistema rítmico solo posee 2
        pistas en la cascada visual de notas durante el juego."""

        utils.log("Task", "Solicitando archivo MIDI...")

        ## Obtiene la ruta del archivo MIDI
        fn = window.get_file_name(title = "Abrir archivo MIDI",
                                filetype = "Archivos MIDI (*.mid)")

        if len(fn) == 0:
            raise Exception("No has seleccionado ningún archivo MIDI.")

        ## Procesa el archivo MIDI y abre una ventana para guardar el archivo de beatmap.
        pitchs = self.open_midi(fn)

        ## Guarda el beatmap basado en formato CSV
        utils.log("Task", "Guardando archivo Beatmap...")
        savefn = window.get_save_file_name(title = "Guardar beatmap como...",
                                        filetype = "Archivos BEAT (*.beat)")

        if len(savefn) == 0:
            raise Exception("No se seleccionó ninguna ruta para guardar el beatmap.")

        else:
            with open(savefn[0], "w") as beatmap:
                w_object = csv.writer(beatmap,
                                    delimiter = "|",
                                    quotechar= "|",
                                    quoting=csv.QUOTE_MINIMAL)

                w_object.writerow(["Keypad_L", "Keypad_R"])

                for l_time, r_time in list(itertools.zip_longest(self.tracks[pitchs[0]], self.tracks[pitchs[1]], fillvalue = "End")):
                    w_object.writerow([l_time, r_time])

                beatmap.close()

            utils.log("OK", "Beatmap construido.")

            output_path = savefn[0]
            notes_left = len(self.tracks[pitchs[0]])
            notes_right = len(self.tracks[pitchs[1]])
            full_combo = notes_left + notes_right

            print(f"""
|   -> {utils.cyan}Ruta de guardado:{utils.end} {output_path}\n
{utils.white}Estadísticas:{utils.end}
|   -> {utils.cyan}Pista L:{utils.end} {notes_left} notas.
|   -> {utils.cyan}Pista R:{utils.end} {notes_right} notas.
|   -> {utils.purple}Full Combo:{utils.end} {full_combo} notas.
""")
