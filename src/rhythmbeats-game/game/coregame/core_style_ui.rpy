## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Coregame) Estilos de UI.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

## -------------------------------------------------------------------------- ##
## Screen "song_select"

## Prefijo "songlist"
style songlist_button is button_skin:
    padding(5, 0, 20, 20)
    xysize(600, 70)
    activate_sound audio.ui_sound_btn01

style songlist_vscrollbar:
    xsize 5
    base_bar Frame(Solid("#777"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(Solid("#CF0"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)


## Prefijo "song_level"
style song_level_hbox:
    ysize 70
    spacing 15

style song_level_vbox:
    yalign 0.5

style song_level_label:
    xalign 0.5

style song_level_label_text:
    color "#FFF"
    xalign 0.5
    size 15

style song_level_text:
    color "#FFF"
    size 28
    text_align 0.5
    yalign 0.5


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

style window_title_frame is msg_success_frame

style window_title_label:
    xalign 0.5

style window_title_label_text:
    color "#000"
    size 20


## -------------------------------------------------------------------------- ##
## Estilo de créditos en la sección "Sobre RhythmBeats"

style about_vbox:
    spacing 15
    xalign 0.5

style about_label:
    xalign 0.5

style about_label_text:
    color "#CF0"
    size 21
    text_align 0.5

style about_text:
    color "#FFF"
    size 19
    xalign 0.5
    text_align 0.5


## -------------------------------------------------------------------------- ##
## Screen "song_details"

## Prefijo "score_goal"
style score_goal_frame:
    background Frame("gui/button/btn_selected_skin.png", 24, 24, 24, 24)
    padding(20, 10, 20, 10)
    minimum(50, 50)
    xalign 0.5

style score_goal_label:
    xalign 0.5

style score_goal_label_text is settings_text:
    color "#CF0"
    text_align 0.5

style score_goal_text:
    color "#FFF"
    size 28
    xalign 0.5
    text_align 0.5


## -------------------------------------------------------------------------- ##
## Screen "song_start"

style song_start_vbox:
    xsize 1280
    align(0.5, 0.5)

style song_start_label:
    xalign 0.5

style song_start_label_text:
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 27
    italic True

style song_start_text:
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    xalign 0.5
    size 17


## -------------------------------------------------------------------------- ##
## Screen "playground_hud"

## Prefijo "stats"
style stats_bar:
    left_bar Solid("#9F9")
    right_bar Solid("#777")
    xysize(300, 7)

style stats_text:
    font "gui/font/DIN-Medium.ttf"
    color "#090"
    outlines [(2, "#FFF", 0, 0)]
    size 22

style stats_vbox:
    pos(0.05, 0.05)


## Estilo directo "song_progress"
style song_progress:
    xysize(800, 24)
    xalign 0.5 ypos 0.02

    left_bar Frame("coregame/ui/bar/ui_bar_progress_fill.png", 50, 12, 50, 12)
    right_bar Frame("coregame/ui/bar/ui_bar_progress_base.png", 50, 12, 50, 12)
    thumb "coregame/ui/bar/ui_bar_progress_thumb.png"
    thumb_offset 12


## Prefijo "song_combo"
style song_combo_vbox:
    xsize 200
    spacing 0
    pos(0.75, 0.38)

style song_combo_label:
    xalign 0.5

style song_combo_label_text:
    font "gui/font/DIN-Medium.ttf"
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 22

style song_combo_text:
    font "gui/font/DIN-Medium.ttf"
    color "#FFF"
    outlines [(3, "#000", 0, 0)]
    size 70
    xalign 0.5


## Prefijo "debugger"
style debugger_frame:
    background Frame(Transform(Solid("#242424"), alpha = 0.7), 24, 24, 24, 24)
    padding(30, 30, 30, 30)
    xminimum 200

style debugger_vbox:
    spacing 10

style debugger_label_text:
    color "#CF0"
    size 20

style debugger_text:
    color "#FFF"
    size 18


## Prefijo "score_style"
style score_style_bar:
    right_bar Solid("#777")
    xysize(300, 7)

style score_style_vbox:
    yalign 0.5

style score_style_hbox:
    spacing 10
    pos(0.035, 0.045)

style score_style_frame is score_results_frame:
    yalign 0.8

style score_style_label_text:
    font "gui/font/DIN-Medium.ttf"
    color "#242424"
    outlines [(2, "#FFF", 0, 0)]
    size 22

style score_style_text:
    font "gui/font/DIN-Medium.ttf"
    color "#FFF"
    size 28
    anchor(0.5, 0.5)
    pos(0.5, 0.49)


## -------------------------------------------------------------------------- ##
## Screen "score_frame"

## Prefijo "scorebar"
style scorebar_bar:
    right_bar Solid("#777")
    xysize(500, 10)

style scorebar_frame:
    xysize(215, 165)

style scorebar_label:
    anchor(0.5, 0.5)
    pos(0.5, 0.49)

style scorebar_label_text:
    font "gui/font/DIN-Medium.ttf"
    color "#FFF"
    size 46

style scorebar_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 24
    xalign 0.5

style scorebar_hbox:
    spacing 20

style scorebar_vbox:
    yalign 0.5


## -------------------------------------------------------------------------- ##
## Screen "show_results"

style show_results_frame:
    background Frame(Solid("#242424"), 24, 24, 24, 24)
    padding(30, 30, 30, 30)
    xmaximum 600

style show_results_hbox:
    spacing 40

style show_results_label_text:
    size 38
    color "#CF0"
    outlines [(2, "#000", 1, 1)]
style show_results_text is song_btn_text:
    outlines [(2, "#000", 1, 1)]


## Prefijo "combo_results"
style combo_results_label_text:
    font "gui/font/DIN-Medium.ttf"
    color "#FFF"
    outlines [(3, "#000", 0, 0)]
    size 85

style combo_results_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 19

style combo_results_hbox:
    spacing 40

style combo_results_vbox:
    yalign 0.5


## Prefijo "score_results"
style score_results_hbox is scorebar_hbox:
    xalign 0.5

style score_results_vbox is scorebar_vbox
style score_results_bar is scorebar_bar:
    xysize(400, 7)
style score_results_label is scorebar_label:
    pos(0.5, 0.5)

style score_results_label_text is scorebar_label_text:
    size 26
style score_results_text is scorebar_text:
    size 20

style score_results_frame:
    xysize(103, 79)


## Prefijo "new_record"
style new_record_frame:
    background Frame("coregame/ui/ui_overlay_newrecord.png", 22, 0, 22, 0)
    padding(22, 5, 22, 5)
    minimum(96, 48)
    xalign 0.5

style new_record_text:
    yalign 0.5
    color "#000"
    size 16


## -------------------------------------------------------------------------- ##
## Screen "playground_finish"

## Prefijo "finish_style"
style finish_style_text:
    outlines [(2, "#000", 0, 0)]
    size 70
