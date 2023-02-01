## CharlieFuu69
## Ren'Py RhythmBeats! Demo

## Script: (Coregame) Estilos de UI.

################################################################################

## -------------------------------------------------------------------------- ##
## Screen "song_select"

## Prefijo "songlist"
style songlist_button is button_skin:
    padding(20, 20, 20, 20)
    xysize(600, 70)
    activate_sound audio.ui_sound_btn01

style songlist_vscrollbar:
    xsize 5
    base_bar Frame(Solid("#777"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(Solid("#CF0"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)


## Prefijo "song_btn"
style song_btn_label_text:
    color "#CF0"
    size 20

style song_btn_text:
    color "#FFF"
    size 16


## Prefijo "now_showing"
style now_showing_frame is frame_skin:
    xysize(500, 450)
    padding(35, 20, 35, 20)

style now_showing_button:
    idle_background Frame(Solid("#A00"), 5, 5, 5, 5)
    hover_background Frame(Solid("#F88"), 5, 5, 5, 5)
    activate_sound audio.ui_sound_btn01
    padding(10, 5, 10, 5)
    xalign 1.0

style now_showing_button_text:
    color "#FFF"
    size 18

style now_showing_label_text:
    xmaximum 470
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 20

style now_showing_text:
    xmaximum 470
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 16

style now_showing_vbox:
    spacing 5
    xfill True


## Prefijo "mv_info"
style mv_info_frame:
    background Solid("#CF0")
    padding(15, 2, 15, 2)
    minimum(10, 10)

style mv_info_text is now_showing_text:
    color "#000"
    outlines []


## Prefijo "sort_music"
style sort_music_button is main_ui_button:
    minimum(250, 50)
    activate_sound audio.ui_sound_btn01
style sort_music_button_text is main_ui_button_text

style sort_music_hbox:
    xalign 0.5 ypos 0.07
    spacing 15


## Prefijo "game_credits"
style game_credits_button is button_skin:
    padding(60, 10, 30, 10)
    activate_sound audio.ui_sound_btn01

style game_credits_button_text is main_ui_button_text


## -------------------------------------------------------------------------- ##
## Estilos de la UI de Configuraciones

## Prefijo "config_panel"
style config_panel_vbox:
    xpos 0.03 yalign 0.5
    spacing 15

style config_panel_hbox:
    xalign 0.5 ypos 0.85

style config_panel_button is main_ui_button:
    activate_sound audio.ui_sound_btn01
style config_panel_button_text is main_ui_button_text


## Prefijo "settings"
style settings_frame is frame_skin:
    padding(40, 40, 40, 40)
    xsize 700
    yminimum 290

style settings_slider:
    xysize(600, 15)
    left_bar Frame("coregame/ui/bar/ui_slider_ctrl_fill.png", 7, 50, 7, 50)
    right_bar Frame("coregame/ui/bar/ui_slider_ctrl_base.png", 7, 51, 7, 51)
    thumb "coregame/ui/bar/ui_slider_ctrl_thumb.png"
    thumb_offset 7

style settings_vbox:
    spacing 20
    xalign 0.5

style settings_text:
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 18
    text_align 0.5

style settings_vscrollbar is songlist_vscrollbar


## Prefijo "config_toggle"
style config_toggle_button is button_skin:
    activate_sound audio.ui_sound_radiobutton
style config_toggle_button_text is offset_setup_button_text

style config_toggle_vbox:
    pos(0.0, 0.0)
    spacing 15

style config_toggle_hbox:
    spacing 15
    xpos 0.0

style config_toggle_text:
    color "#FFF"
    size 18


## Prefijo "offset_setup"
style offset_setup_button is button_skin

style offset_setup_button_text:
    idle_color "#999"
    hover_color "#FFF"
    selected_color "#CF0"
    size 18
    text_align 0.5
    xalign 0.5

style offset_setup_vbox:
    xalign 0.5
    spacing 20

style offset_setup_label is window_title_label
style offset_setup_label_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 60


## -------------------------------------------------------------------------- ##
## Screen "category_switcher"

## Prefijo "switcher"
style switcher_frame is frame_skin:
    modal True
    ypadding 15
    pos(0.185, 0.15)

style switcher_vbox:
    spacing 10
    xsize 200

style switcher_button:
    xalign 0.5
    activate_sound audio.ui_sound_btn03

style switcher_button_text is main_ui_button_text


## -------------------------------------------------------------------------- ##
## Screen "credits_window"

## Prefijo "credits_window"
style credits_window_label is startscreen_label
style credits_window_label_text is startscreen_label_text
style credits_window_text is startscreen_text:
    xalign 0.5
    xmaximum 830
    text_align 0.5
style credits_window_frame is frame_skin:
    padding(20, 20, 20, 20)
    xminimum 900

style credits_window_vscrollbar is songlist_vscrollbar


## -------------------------------------------------------------------------- ##
## Estilo de títulos de ventanas

style window_title_frame is msg_success

style window_title_label:
    xalign 0.5

style window_title_label_text:
    color "#000"
    size 20
