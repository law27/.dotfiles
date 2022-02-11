from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile import hook
from libqtile.lazy import lazy
from gruvbox.gruvbox import *
from theme import *
import os
import subprocess

mod = "mod4"

slash = " "
separator = slash
                     
#programs are handled by sxhkd
keys = [

    # SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),

    Key([mod], "h", lazy.layout.left(), ),
    Key([mod], "l", lazy.layout.right(), ),
    Key([mod], "j", lazy.layout.down(), ),
    Key([mod], "k", lazy.layout.up(), ),
    
    # QTILE LAYOUT KEYS
    
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),


    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), ),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), ),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), ),

    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),


    Key([mod], "Tab", lazy.screen.toggle_group(), ),
    Key([mod, "control"], "r", lazy.restart(), ),
    Key([mod, "control"], "q", lazy.shutdown(), ),

    Key([mod, "shift"], "space",lazy.window.toggle_floating(),),
    Key([mod], "t",lazy.hide_show_bar(),),
    Key([mod], "Return", lazy.spawn("kitty -d ~"), desc="Launch Terminal"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-")),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -q -D pulse sset Master toggle"),
    ),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),
    Key([mod], "r", lazy.spawn("/home/lawrance/.config/qtile/scripts/launcher.sh"), desc="run rofi"),
    Key([mod], "b", lazy.spawn("google-chrome-stable"), desc="Launch Browser"),
    Key([mod, "shift"], "c", lazy.spawn("speedcrunch"), desc="Launch Calculator"),
]

groups = [
    Group("1", layout="monadtall"),
    Group("2", matches=[Match(wm_class=["Code", "jetbrains-idea", "jetbrains-webstorm"])], layout="max"),
    Group("3", matches=[Match(wm_class=["brave-browser", "google-chrome", "firefox"])], layout="max"),
    Group("4", matches=[Match(wm_class=["ghostwriter", "notion-app-enhanced"])],layout="monadtall"),
    Group("5", matches=[Match(wm_class=["Thunar"])], layout="monadtall"),
    Group("6", layout="monadtall"),
    Group("7", layout="monadtall"),
    Group("8", layout="monadtall"),
    Group("9", matches=[Match(wm_class=["spotify"])],layout="monadtall"),
    Group("0", matches=[Match(wm_class=["skype"])], layout="monadtall"),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),),
    ])

layouts = [
    layout.MonadTall(margin=8, border_width=2, border_focus=red, border_normal=normal_t),
    layout.Max(),
]

widget_defaults = dict(
    font='Iosevka Term Extended',
    fontsize=16,
    padding=5,
    foreground=foreground,
    background=background,

)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag=True,
                    spacing=0,
                    center_aligned=True,
                    active=active,
                    inactive=inactive,
                    highlight_method="block",
                    this_current_screen_border=mark,
                    urgent_border=warning,
                ),
                widget.WindowName(
                    foreground=foreground,
                    padding=5
                    ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=purple,
                    ),
                widget.TextBox(
                    text= 'bright:',
                    background=purple,
                    foreground=white0,
                    ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    background=purple,
                    foreground=white0,
                ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=yellow,
                    background=purple,
                    ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=green,
                    background=yellow,
                    ),
                widget.TextBox(
                    text= 'vol:',
                    background=yellow,
                    foreground=white0,
                    ),
                widget.Volume(
                    background=yellow,
                    foreground=white0,
                ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=green,
                    background=yellow,
                    ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=aqua,
                    background=green,
                    ),
                widget.TextBox(
                    text= 'bat:',
                    background=green,
                    foreground=white0,
                    ),
                widget.Battery(
                    format='{percent:2.0%}',
                    low_percentage=0.2,
                    low_foreground=warning,
                    background=green,
                    foreground=white0,
                ),
                widget.BatteryIcon(
                    background=green,
                    update_interval=2
                ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=aqua,
                    background=green,
                    ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=purple,
                    background=blue,
                    ),
                widget.Clock(
                    #format='%I:%M %p',
                    format='%d.%m',
                    background=blue,
                    foreground=white0,
                    ),
                widget.TextBox(
                    padding=0,
                    text= separator,
                    foreground=purple,
                    background=blue,
                    ),
                widget.Clock(
                    #format='%d.%m.%Y',
                    format='%I:%M',
                    background=purple,
                    foreground=white0,
                    ),
                widget.Systray(
                    background=aqua,
                    icon_size=15,
                    ),
            ],
            20,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
        border_focus=focus_f,
        border_normal=normal_f,
        border_width=3,
        float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-tweak-tool.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='arcolinux-logout'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='skype'),
    Match(wm_class='speedcrunch'),
    Match(wm_class='stretchly'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


# Needed by some Java programs
wmname = "LG3D"
