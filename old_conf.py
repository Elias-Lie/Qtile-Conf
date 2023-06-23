from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from libqtile.dgroups import simple_key_binder


########## setting variables ##########

mod = "mod4"
terminal = "kitty"
browser = "brave"
editor = "code"
colors = {
    "background": "#283141",
    "sec-background": "#43485D",
    "green": "#BDD586",
    "red": "#EA7A70",
    "purple": "#C197E0",
    "blue": "#8CBFF9",
    "black": "#030202"
}


########## seting keybinds ##########

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key({mod}, "b", lazy.spawn(browser), desc="Launch browser"),
    Key({mod}, "c", lazy.spawn(editor), desc="Launch editor"),
    
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
    
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
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
    "border_focus": "e1acff",
    "border_normal": "1D2330",
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

# default widget theme
widget_defaults = dict(
    font="SF-Mono",
    fontsize=18,
    padding=2,
    background=colors["background"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                sep(),
                widget.GroupBox(
                    fontsize = 18,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors["red"],
                    inactive = colors["blue"],
                    rounded = False,
                    highlight_color = colors["sec-background"],
                    highlight_method = "line",
                    this_current_screen_border = colors["black"],
                    this_screen_border = colors["black"],
                    other_current_screen_border = colors["black"],
                    other_screen_border = colors["black"],
                ),
                sep(),
                widget.Prompt(),
                sep(),
                widget.WindowName(
                    foreground = colors["blue"],
                    padding = 0
                ),
                
                
                
                left_arrow(colors["sec-background"], colors["background"]),
                widget.Systray(
                    background=colors["sec-background"],
                    padding = 5
                ),
                left_arrow(colors["green"], colors["sec-background"]),
                widget.Net(
                    background=colors["green"]
                ),
                #widget.Battery(
                #    background=colors["green"]
                #),
                left_arrow(colors["purple"], colors["green"]),
                widget.CPU(
                    background=colors["purple"]  
                ),
                left_arrow(colors["blue"], colors["purple"]),
                widget.Memory(
                    background=colors["blue"]
                ),
                left_arrow(colors["red"], colors["blue"]),
                widget.Wallpaper(
                    directory='~/Pictures/Wallpapers',
                    background=colors["red"],
                    label='wallpaper'
                    ),
                left_arrow(colors["black"], colors["red"]),
                widget.Clock(
                    background=colors["black"],
                    format = "%A, %B %d - %H:%M",
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    background = colors["black"]
                    ),
            ],
            size=30,
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
