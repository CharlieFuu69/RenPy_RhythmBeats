## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Ren'Py) Screens principales.

## © 2023 CharlieFuu69 - GNU GPL v3.0

#############################################################

## Prioridad de inicialización
init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    hover_underline True
    color "#CF0"

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    font gui.text_font
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size

style vbar:
    xsize gui.bar_size

style scrollbar:
    ysize gui.scrollbar_size

style vscrollbar:
    xsize 5
    base_bar Frame(Solid("#777"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(Solid("#9F9"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size

style vslider:
    xsize gui.slider_size

style frame:
    padding gui.frame_borders.padding

################################################################################
## Pantallas internas a juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto visualizable con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también visualizables
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Si hay una imagen lateral, la muestra encima del texto. No la muestra en
    ## la variante de teléfono - no hay lugar.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un displayable 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

screen choice(items):
    add Null(100, 100)

screen quick_menu():
    add Null(100, 100)

screen navigation():
    add Null(100, 100)

screen main_menu():
    add Null(100, 100)

screen game_menu(title, scroll=None, yinitial=0.0):
    add Null(100, 100)

screen about():
    add Null(100, 100)


screen save():
    add Null(100, 100)

screen load():
    add Null(100, 100)

screen file_slots():
    add Null(100, 100)

screen preferences():
    add Null(100, 100)

screen history():
    add Null(100, 100)

screen help():
    add Null(100, 100)


################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    use notify_window(_("VENTANA DE CONFIRMACIÓN"), notify_sound=audio.ui_sound_notify):
        vbox:
            spacing 30
            text _(message)

        hbox:
            xalign 0.5
            ypos 0.8
            spacing 15

            textbutton _("Sí") action yes_action
            textbutton _("No") action no_action

    ## Clic derecho o escape responden "no".
    key "game_menu" action no_action

style confirm_frame is update_frame

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_label is update_label
style confirm_label_text is update_label_text
style confirm_text is update_text
style confirm_button is main_ui_button:
    activate_sound audio.ui_sound_btn01
style confirm_button_text is main_ui_button_text:
    font gui.text_font
style confirm_vbox is update_vbox


## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

## -------------------------------------------------------------------------- ##
## Notificación minimizada

screen custom_notify(status=0, icon=None, content):
    style_prefix "custom_notify"
    zorder 130

    default _suffix = "success" if status == 0 else "error"

    on "show" action Play("ui_02", audio.ui_sound_notify_small)

    frame at notify_small_bg:
        background "ui_notify_%s" %(_suffix)
        has hbox

        if icon:
            add icon yalign 0.5

        text content at notify_small_text(0.2)


screen notify(message):
    zorder 900

    on "show" action Hide("custom_notify"), Show("custom_notify", content=__(message))
    timer 5.0 action Hide("notify")


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Pantalla NVL ################################################################

screen nvl(dialogue, items=None):
    add Null(100, 100)

screen nvl_dialogue(dialogue):
    add Null(100, 100)

define config.nvl_list_length = gui.nvl_list_length

## ------------------------------------------------------------------------------------------------------------- ##
## Pantalla de inicio del juego

screen main_advice():
    style_prefix "startscreen"
    timer 3.0 action [Hide("main_advice", transition = dissolve), Return()]

    add "tex_black_solid"

    vbox:
        xsize 900
        add "ui_icon_headphones" at headphone_blink
        text _("Usa auriculares para una mejor experiencia.")


screen startscreen():
    style_prefix "startscreen"

    timer 3.0 action [Hide("startscreen", transition = dissolve), Return()]

    vbox:
        add "ui_icon_logo" zoom 0.8 xalign 0.5
        label config.name
        text config.version

    text "[game_license]" ypos 0.9

style startscreen_vbox:
    align(0.5, 0.5)
    spacing 15

style startscreen_label:
    xalign 0.5

style startscreen_label_text:
    color "#CF0"
    outlines [(2, "#000", 1, 1)]
    size 44

style startscreen_text:
    xalign 0.5
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 18


## -------------------------------------------------------------------------- ##
## Ventana de notificaciones prefeterminada

screen notify_window(title = "", level = 0, notify_sound = None, shadow=True):
    modal True
    zorder 110
    style_prefix "confirm"

    timer 0.01 action Play("notify_01", notify_sound)

    if shadow:
        add "tex_black"

    frame at msgwindow_anim:
        frame:
            style_prefix ("msg_success" if level == 0 else "msg_failed")
            label title

        transclude


screen lang_first_run():
    style_prefix "confirm"

    use notify_window(_("IDIOMA DE LA INTERFAZ"),
                        notify_sound=audio.ui_sound_notify,
                        shadow=False):

        vbox:
            spacing 15
            xalign 0.5

            textbutton "Español" action Language(None) xalign 0.5

            for lang_chunk in chunkdata(renpy.known_languages(), 2):
                hbox:
                    spacing 15
                    xalign 0.5

                    for lang in lang_chunk:
                        textbutton lang.capitalize() action Language(lang)


        hbox:
            xalign 0.5
            ypos 0.8
            textbutton _("Aceptar y continuar"):
                action [Hide("lang_first_run"),
                        SetVariable("persistent.language_choice", True),
                        Return()]

## -------------------------------------------------------------------------- ##
## Screen de actualización global necesaria

screen msg_global_update(now_version = ""):
    modal True
    zorder 200
    style_prefix "confirm"

    default latest_url = "https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/latest"

    use notify_window(_("ACTUALIZACIÓN GLOBAL NECESARIA"), notify_sound=audio.ui_sound_notify, shadow=False):
        vbox:
            spacing 30
            text __("La versión que tienes ({color=cf0}[config.version]{/color}) está descontinuada. Debes actualizar a la versión {color=cf0}[now_version]{/color} para continuar jugando.")
            text _("Entra al repositorio de GitHub desde el botón acá abajo, y sigue las instrucciones para actualizar el juego.")

        hbox:
            xalign 0.5
            ypos 0.8
            spacing 20

            textbutton _("Ir a GitHub") action OpenURL(latest_url)
            textbutton _("Cerrar el juego") action Quit(confirm = False)


screen download_complete():
    modal True
    zorder 200
    style_prefix "confirm"

    use notify_window(_("DESCARGA FINALIZADA"), notify_sound = audio.ui_sound_notify, shadow=False):
        vbox:
            text _("Los recursos de {color=cf0}Ren'Py RhythmBeats{/color} han sido descargados completamente.")

            if renpy.android:
                text _("El juego debe cerrarse y volver a iniciar para aplicar los cambios. Presiona {color=cf0}\"Cerrar el juego\"{/color} para continuar.")
            else:
                text _("Presiona \"Reiniciar el juego\" para aplicar los cambios de los archivos descargados.")

        hbox:
            style_prefix "main_ui"
            xalign 0.5 ypos 0.8 spacing 20

            textbutton "%s" % (_("Cerrar el juego") if renpy.android else _("Reiniciar el juego")):
                action [Hide("download_complete"),
                Return()]
                activate_sound audio.ui_sound_btn03


## -------------------------------------------------------------------------- ##
## Pantalla/UI de búsqueda de actualizaciones.

screen update(inst):
    style_prefix "update"
    timer 0.5 action Function(renpy.invoke_in_thread, fn=inst.run)

    if inst.request_end:
        if inst.exception_break and inst.pass_flag():
            use notify_window(title = _("ERROR DE CONEXIÓN"), level=1, notify_sound=audio.ui_sound_error, shadow=False):
                vbox:
                    text inst.exception_body

                hbox:
                    xalign 0.5 ypos 0.78 spacing 20
                    textbutton _("Reintentar") action [Hide("update"), Return(), Jump("check_updates")]
                    textbutton _("Cerrar el juego") action [Hide("update"), Quit(confirm=False)]

        else:
            if len(update.update_queue) != 0:
                use notify_window(title = _("CONFIRMACIÓN DE DESCARGA"), notify_sound=audio.ui_sound_notify, shadow=False):
                    vbox:
                        text __("Tamaño de la descarga: %.02f MB") % inst.update_size underline True
                        text _("Esta descarga contiene las pistas musicales y 2DMVs incluidos en la demostración de {color=CF0}Ren'Py RhythmBeats!{/color}.")
                        text _("La velocidad de descarga puede variar en función del tráfico en GitHub, o de la estabilidad de tu conexión.")

                    hbox:
                        xalign 0.5 ypos 0.8
                        textbutton _("Iniciar descarga") action [Hide("update"), Jump("download_sequence")]

            else:
                timer 0.01 action [Hide("update"), Return()]

    else:
        vbox:
            ypos 0.9
            text _("Buscando actualizaciones (GitHub)...")
            bar:
                value StaticValue(inst.progress[0], inst.progress[1] or 0.1)


## ------------------------------------------------------------------------------------------------------------- ##
## Pantalla/UI de descarga de recursos.

screen download():
    style_prefix "update"
    modal True

    default dl = update

    on "show" action Function(renpy.invoke_in_thread, fn=dl.start_download)

    if dl.request_end:
        if dl.exception_break:
            use notify_window(title = _("ERROR DURANTE LA DESCARGA"), level=1, notify_sound=audio.ui_sound_error, shadow=False):
                vbox:
                    text dl.exception_content

                hbox:
                    xalign 0.5 ypos 0.78 spacing 20
                    textbutton _("Reintentar") action [Hide("download"), Return(), Jump("download_sequence")]
                    textbutton _("Cerrar el juego") action [Hide("download"), Quit(confirm=False)]

        else:
            timer 0.01 action [Hide("download"), Return()]

    else:
        vbox:
            ypos 0.85 spacing 5
            text _("Descargando recursos...")
            text "%s (%s/%s)" % (dl.download_fmt(), dl.batch_progress[0], dl.batch_progress[1])
            bar:
                value StaticValue(dl.current_size, dl.file_size or 0.1)
            null height 7
            bar:
                value StaticValue(dl.mb_received, dl.update_size or 0.1)


init python:
    config.per_frame_screens.append("download")


## -------------------------------------------------------------------------- ##
style button_skin:
    background Frame("gui/button/btn_[prefix_]skin.png", 24, 24, 24, 24)
    padding(20, 10, 20, 10)
    minimum(50, 50)

style frame_skin:
    background Frame("gui/overlay/ui_frame_skin.png", 12, 12, 12, 12)

style main_ui_button is button_skin:
    minimum(200, 50)

style main_ui_button_text:
    idle_color "#999"
    hover_color "#FFF"
    selected_color "#CF0"
    size 18
    text_align 0.5
    xalign 0.5

## -------------------------------------------------------------------------- ##

style update_frame is frame_skin:
    xysize(600, 400)
    align(0.5, 0.5)

style update_label:
    xalign 0.5

style update_label_text:
    color "#000"
    size 20

style update_text:
    xalign 0.5
    text_align 0.5
    xmaximum 550
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 18

style update_vbox:
    xalign 0.5 ypos 0.3
    spacing 10

style update_bar:
    xalign 0.5
    xysize(1100, 4)
    left_bar Solid("#CF0")
    right_bar Solid("777")

style update_button is main_ui_button:
    activate_sound audio.ui_sound_btn01
style update_button_text is main_ui_button_text

## -------------------------------------------------------------------------- ##

style msg_success_frame:
    background Frame(Solid("#CF0"), 5, 5, 5, 5)
    padding(10, 5, 10, 5)
    xalign 0.5 ypos 0.1
    minimum(500, 20)

style msg_success_label is update_label
style msg_success_label_text is update_label_text

style msg_failed_frame:
    background Frame(Solid("#FF233B"), 5, 5, 5, 5)
    xalign 0.5 ypos 0.1
    padding(10, 5, 10, 5)
    minimum(500, 20)

style msg_failed_label is update_label
style msg_failed_label_text is update_label_text

## -------------------------------------------------------------------------- ##
## Screen "custom_notify"

## Prefijo "custom_notify"
style custom_notify_frame:
    padding(40, 10, 40, 10)
    minimum(28, 28)
    xmaximum 700
    xalign 0.5 yalign 0.1

style custom_notify_hbox:
    spacing 10
    align(0.5, 0.5)

style custom_notify_text:
    yalign 0.5
