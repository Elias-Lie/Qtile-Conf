from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from libqtile.dgroups import simple_key_binder


########## setting variables ##########

mod = "mod4"
terminal = "kitty"
browser = "brave"
editor = "code"
colors = {
    "background": "#2f343f",
    "light-background": "#404552",
    "foreground": "#e1e3e7",
}


########## setting keybinds ##########

keys = [
    # apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "c", lazy.spawn(editor), desc="Launch editor"),
    Key([mod], "d", lazy.run_extension(extension.DmenuRun(
        background=colors["background"],
        foreground=colors["foreground"],
        selected_background=["light-background"],
        dmenu_bottom=False,
        fontsize=14,
    ))),
    
    # window movement
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    
    # misc
    Key([mod], "f", lazy.hide_show_bar(), desc="Toggle bar (fullscreen)"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # special keys (from xev)
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")), #FN+F1 mute audio
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --unmute --decrease 5")), #FN+F2 volume down
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --unmute --increase 5")), #FN+F3 volume up
    #Key([], "XF86AudioMicMute", lazy.spawn("pamixer --default-source --toggle-mute")), #FN+F4 mute mic
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")), #FN+F5 brightness down
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")), #FN+F6 brightness up
    #FN+F7
    #FN+F8
    #FN+F9
    #FN+F10
    #FN+F11
    #FN+F12
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


########## setting groups ##########

groups = [Group(i) for i in "123456789"]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")


########## setting layouts ##########

# default layout
layout_theme = {
    "border_width": 0,
    "margin": 0,
    "border_focus": colors["light-background"],
    "border_normal": colors["background"],
}

layouts = [
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.Floating(**layout_theme),
]


########## setting widgets ##########

def right_arrow(foreground, background):
    return widget.TextBox(
        text="\uE0B0",
        padding=-1,
        fontsize=32,
        foreground=foreground,
        background=background,
    )
    
def left_arrow(foreground, background):
    return widget.TextBox(
        text="\uE0B2",
        padding=-1,
        fontsize=32,
        foreground=foreground,
        background=background,
    )
    
def sep():
    return widget.Sep(
        linewidth = 0,
        padding = 6,
    )

def text_sep():
    return widget.TextBox(
        text="|",
        padding=6,
        foreground=colors["foreground"],
    )

# default widget theme
widget_defaults = dict(
    font="sans",
    fontsize=16,
    foreground=colors["foreground"],
    background=colors["background"],
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    margin_x = 0,
                    margin_y = 3,
                    padding_x = 6,
                    padding_y = 5,
                    borderwidth = 0,
                    rounded = False,
                    disable_drag=True, 
                    highlight_method="block",
                    active=colors["foreground"],
                    inactive=colors["foreground"],
                    this_current_screen_border=colors["light-background"],
                ),
                widget.WindowName(
                    foreground=colors["foreground"],
                    background=colors["light-background"],
                    padding=12,
                ),
                sep(),
                widget.PulseVolume(
                ),
                text_sep(),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    change_command=None,
                ),
                text_sep(),
                widget.Net(
                    prefix="M",
                ),
                text_sep(),
                widget.CPU(
                    format="{load_percent}%",
                ),
                text_sep(),
                widget.Memory(
                    measure_mem="G",
                ),
                text_sep(),
                widget.Battery(
                    #format="{char} {percent:2.0%}",
                    format="{char} {percent:2.0%}  {hour:d}:{min:02d}",
                    charge_char="charging",
                    update_interval=10,
                ),
                text_sep(),
                widget.Clock(
                    format="%H:%M",
                ),
                widget.Systray(
                    padding = 6,
                ),
                sep(),
            ],
            size=25,
        ),
    ),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
