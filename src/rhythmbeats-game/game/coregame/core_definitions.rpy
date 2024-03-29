## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Coregame) Definiciones elementales del programa.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

init offset = -4

init:
    ## ---------------------------------------------------------------------- ##
    ## Variables/objetos utilizados posterior a entrar al juego

    default persistent.highscores = dict()
    default persistent.operating_stats = False
    default persistent.failsafe = False
    default persistent.discord_rpc = False
    default persistent.category = "all"
    default persistent.song_selected = None
    default rpc = None

    ## ---------------------------------------------------------------------- ##
    ## Definiciones de audio

    define audio.sfx_stage_failed = "audio/coregame/sfx_coregame_failed.ogg"
    define audio.sfx_stage_cleared = "audio/coregame/sfx_coregame_cleared.ogg"
    define audio.sfx_stage_full_combo = "audio/coregame/sfx_coregame_full_combo.ogg"
    define audio.sfx_stage_all_perfect = "audio/coregame/sfx_coregame_all_perfect.ogg"
    define audio.sfx_note_miss = "audio/coregame/ui_coregame_note_miss.ogg"
    define audio.sfx_results_intro = "audio/coregame/sfx_results_intro.ogg"
    define audio.sfx_results_scoreframe = "audio/coregame/sfx_results_scoreframe.ogg"

    define audio.ui_sound_radiobutton = "audio/coregame/ui_sound_radiobutton.ogg"

    define audio.bgm_0047 = "audio/coregame/bgm_0047.ogg"


    ## ---------------------------------------------------------------------- ##
    ## Capas de video (2DMV)

    image 2dmv_0001 = Movie(play="MV/2dmv_0001.webm", loop = False)
    image 2dmv_0002 = Movie(play="MV/2dmv_0002.webm", loop = False)
    image 2dmv_0003 = Movie(play="MV/2dmv_0003.webm", loop = False)
    image 2dmv_0005 = Movie(play="MV/2dmv_0005.webm", loop = False)
    image 2dmv_0006 = Movie(play="MV/2dmv_0006.webm", loop = False)
    image 2dmv_0007 = Movie(play="MV/2dmv_0007.webm", loop = False)
    image 2dmv_0008 = Movie(play="MV/2dmv_0008.webm", loop = False)
    image 2dmv_0010 = Movie(play="<from 5.05>MV/2dmv_0010.webm", loop = False)
    image 2dmv_0011 = Movie(play="MV/2dmv_0011.webm", loop = False)
    image 2dmv_0013 = Movie(play="MV/2dmv_0013.webm", loop = False)
    image 2dmv_0014 = Movie(play="MV/2dmv_0014.webm", loop = False)
    image 2dmv_0015 = Movie(play="MV/2dmv_0015.webm", loop = False)
    image 2dmv_0017 = Movie(play="MV/2dmv_0017.webm", loop = False)
    image 2dmv_0018 = Movie(play="MV/2dmv_0018.webm", loop = False)
    image 2dmv_0020 = Movie(play="<from 6.0>MV/2dmv_0020.webm", loop = False)
    image 2dmv_0021 = Movie(play="<from 6.19>MV/2dmv_0021.webm", loop = False)
    image 2dmv_0022 = Movie(play="MV/2dmv_0022.webm", loop = False)
    image 2dmv_0023 = Movie(play="MV/2dmv_0023.webm", loop = False)
    image 2dmv_0026 = Movie(play="MV/2dmv_0026.webm", loop = False)
    image 2dmv_0027 = Movie(play="MV/2dmv_0027.webm", loop = False)

    ## ---------------------------------------------------------------------- ##
    ## Imágenes de UI

    ## Displayables de color sólido
    image ui_tex_black:
        Solid("#000")
        alpha 0.0
        ease 1.0 alpha 0.45

    image ui_tex_white = Solid("#FFF")
    image ui_black_solid = Solid("#000")

    ## Interfaz de partidas
    image ui_coregame_note_lane = "coregame/ui/overlay/ui_overlay_note_lane.png"
    image ui_coregame_note_tap = Transform("coregame/ui/ui_coregame_note_tap.png", zoom = 1.3)
    image ui_coregame_bg_failed = "coregame/ui/ui_coregame_bg_failed.png"

    image ui_performance_alert = Transform("coregame/ui/icon/ui_icon_performance_alert.png", zoom = 0.5)
    image ui_icon_github = Transform("coregame/ui/icon/ui_icon_github.png", zoom = 0.1)
    image ui_icon_discord = "coregame/ui/icon/ui_icon_discord.png"
    image ui_icon_exit = "coregame/ui/icon/ui_icon_exit.png"

    image ui_icon_singleplayer = Transform("coregame/ui/icon/ui_icon_singleplayer.png", zoom=0.6)
    image ui_icon_server_party = Transform("coregame/ui/icon/ui_icon_server_party.png", zoom=0.6)

    image ui_icon_rank_s = "coregame/ui/icon/ui_icon_rank_s.png"
    image ui_icon_rank_a = "coregame/ui/icon/ui_icon_rank_a.png"
    image ui_icon_rank_b = "coregame/ui/icon/ui_icon_rank_b.png"
    image ui_icon_rank_c = "coregame/ui/icon/ui_icon_rank_c.png"

    image ui_icon_song_info = Transform("coregame/ui/icon/ui_icon_song_info.png", zoom=0.6)


    image ui_iconfps_now_playing = anim.Filmstrip("coregame/ui/icon/ui_iconfps_now_playing.png",
                                        (32, 32),
                                        (8, 1),
                                        0.1)

    image ui_overlay_results = Frame("coregame/ui/overlay/ui_overlay_results.png", 200, 0, 300, 0)

    ## ---------------------------------------------------------------------- ##
    ## Texturas y efectos

    image ui_tex_flashlight = "coregame/textures/ui_tex_flashlight.png"

    image tex_show_end_blue = anim.Filmstrip("coregame/textures/ui_tex_show_end_blue.png",
                                        (32, 32),
                                        (8, 1),
                                        0.04)
    image tex_show_end_green = anim.Filmstrip("coregame/textures/ui_tex_show_end_green.png",
                                        (32, 32),
                                        (8, 1),
                                        0.05)
    image tex_show_end_orange = anim.Filmstrip("coregame/textures/ui_tex_show_end_orange.png",
                                        (32, 32),
                                        (8, 1),
                                        0.03)
    image tex_show_end_red = anim.Filmstrip("coregame/textures/ui_tex_show_end_red.png",
                                        (32, 32),
                                        (8, 1),
                                        0.03)
    image tex_show_end_violet = anim.Filmstrip("coregame/textures/ui_tex_show_end_violet.png",
                                        (32, 32),
                                        (8, 1),
                                        0.05)
    image tex_show_end_yellow = anim.Filmstrip("coregame/textures/ui_tex_show_end_yellow.png",
                                        (32, 32),
                                        (8, 1),
                                        0.06)

    image tex_show_cleared:
        Fixed(
        SnowBlossom("tex_show_end_blue", border = 50, yspeed = 150, start = 4.0, count = 7),
        SnowBlossom("tex_show_end_green", border = 50, yspeed = 150, start = 4.0, count = 7),
        SnowBlossom("tex_show_end_orange", border = 50, yspeed = 150, start = 4.0, count = 7),
        SnowBlossom("tex_show_end_red", border = 50, yspeed = 150, start = 4.0, count = 7),
        SnowBlossom("tex_show_end_violet", border = 50, yspeed = 150, start = 4.0, count = 7),
        SnowBlossom("tex_show_end_yellow", border = 50, yspeed = 150, start = 4.0, count = 7))
        alpha 0.0
        pause 2.0
        ease 0.8 alpha 1.0
