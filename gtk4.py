import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, Pango

import sys

from layout import getlayout
from color import setcolor
from save import save_mangohud_config
LAYOUT_OPTIONS = ["horizontal", "vertical", "complete"]
POSITION_OPTIONS = [
    "top-left", "top-right", "top-center",
    "middle-left", "middle-right",
    "bottom-left", "bottom-right", "bottom-center"
]
COLOR_PROFILES = {
    0: "Default",
    1: "Red",
    2: "Green",
    3: "Blue"
}
COLOR_NAMES_TO_KEYS = {name: key for key, name in COLOR_PROFILES.items()}
INITIAL_COLOR_NAME = COLOR_PROFILES[0]

MIN_SCALE = 0.1
MAX_SCALE = 1.5
INITIAL_SCALE = 1.0

INITIAL_FPS_LIMIT = 0

class SimpleHUDMainWindow(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title("SimpleHUD Configurator")
        self.set_default_size(700, 780)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_data("""
            textview {
                font-family: Monospace;
                font-size: 10pt; /* Adjust as needed */
            }
        """)
        Gtk.StyleContext.add_provider_for_display(
            self.get_display(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        # --- Layout Principal ---
        self.main_content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)

        header_bar = Adw.HeaderBar()
        self.save_button = Gtk.Button(label="Save Configuration")
        self.save_button.add_css_class("suggested-action")
        header_bar.pack_end(self.save_button)
        
        toolbar_view = Adw.ToolbarView()
        toolbar_view.add_top_bar(header_bar)
        toolbar_view.set_content(self.main_content_box) 

        self.set_content(toolbar_view)

        self._create_widgets()
        self._connect_signals()
        self.update_preview()

    def _create_widgets(self):
        preferences_page = Adw.PreferencesPage()
        self.main_content_box.append(preferences_page)

        settings_group = Adw.PreferencesGroup(title="HUD Settings")
        preferences_page.add(settings_group)

        self.combo_layout_model = Gtk.StringList.new(LAYOUT_OPTIONS)
        self.combo_layout_row = Adw.ComboRow(
            title="Layout",
            model=self.combo_layout_model
        )
        self.combo_layout_row.set_selected(0)
        settings_group.add(self.combo_layout_row)

        self.combo_position_model = Gtk.StringList.new(POSITION_OPTIONS)
        self.combo_position_row = Adw.ComboRow(
            title="Position",
            model=self.combo_position_model
        )
        self.combo_position_row.set_selected(0)
        settings_group.add(self.combo_position_row)

        self.scale_adjustment = Gtk.Adjustment(
            value=INITIAL_SCALE, lower=MIN_SCALE, upper=MAX_SCALE,
            step_increment=0.1, page_increment=0.1
        )
        self.scale_slider = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL,
            adjustment=self.scale_adjustment,
            digits=1,
            draw_value=False 
        )
        self.scale_value_label = Gtk.Label(label=f"{INITIAL_SCALE:.1f}")
        scale_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        scale_box.append(self.scale_slider)
        self.scale_slider.set_hexpand(True)
        scale_box.append(self.scale_value_label)
        scale_row = Adw.ActionRow(title="Scale")
        scale_row.add_suffix(scale_box)
        settings_group.add(scale_row)

        self.color_profile_names = list(COLOR_PROFILES.values())
        self.combo_color_model = Gtk.StringList.new(self.color_profile_names)
        self.combo_color_row = Adw.ComboRow(
            title="Color Profile",
            model=self.combo_color_model
        )
        try:
            initial_color_idx = self.color_profile_names.index(INITIAL_COLOR_NAME)
            self.combo_color_row.set_selected(initial_color_idx)
        except ValueError:
            self.combo_color_row.set_selected(0)
        settings_group.add(self.combo_color_row)

        self.entry_fps_row = Adw.EntryRow(title="FPS Limit (0=Unlimited)")
        self.entry_fps_row.set_text(str(INITIAL_FPS_LIMIT))
        self.entry_fps_row.set_input_purpose(Gtk.InputPurpose.NUMBER)
        settings_group.add(self.entry_fps_row)

        preview_group = Adw.PreferencesGroup(title="Preview")
        preferences_page.add(preview_group)

        self.preview_textview = Gtk.TextView()
        self.preview_textview.set_editable(False)
        self.preview_textview.set_cursor_visible(False)
        self.preview_textview.set_wrap_mode(Gtk.WrapMode.NONE)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_child(self.preview_textview)
        scrolled_window.set_vexpand(True)
        scrolled_window.set_hexpand(True)
        scrolled_window.set_min_content_height(250)

        preview_container_row = Adw.ActionRow()
        preview_container_row.set_child(scrolled_window)
        preview_group.add(preview_container_row)


    def _connect_signals(self):
        self.combo_layout_row.connect("notify::selected-item", self.on_config_change)
        self.combo_position_row.connect("notify::selected-item", self.on_config_change)
        self.combo_color_row.connect("notify::selected-item", self.on_config_change)
        self.scale_adjustment.connect("value-changed", self._on_scale_value_change)
        self.entry_fps_row.connect("notify::text", self.on_config_change)
        self.save_button.connect("clicked", self._on_save_clicked)

    def _on_scale_value_change(self, adjustment):
        value = adjustment.get_value()
        self.scale_value_label.set_text(f"{value:.1f}")
        self.on_config_change(None)

    def on_config_change(self, widget, _param_spec=None):
        self.update_preview()

    def update_preview(self):
        selected_layout_item = self.combo_layout_row.get_selected_item()
        selected_layout = selected_layout_item.get_string() if selected_layout_item else LAYOUT_OPTIONS[0]

        selected_position_item = self.combo_position_row.get_selected_item()
        selected_position = selected_position_item.get_string() if selected_position_item else POSITION_OPTIONS[0]

        selected_color_item = self.combo_color_row.get_selected_item()
        selected_color_name = selected_color_item.get_string() if selected_color_item else INITIAL_COLOR_NAME
        
        selected_scale = self.scale_adjustment.get_value()
        selected_color_idx = COLOR_NAMES_TO_KEYS.get(selected_color_name, 0)

        try:
            fps_text = self.entry_fps_row.get_text()
            if not fps_text.strip():
                selected_fps_limit = INITIAL_FPS_LIMIT
            else:
                selected_fps_limit = int(fps_text)
            if selected_fps_limit < 0:
                selected_fps_limit = 0
        except ValueError:
            selected_fps_limit = INITIAL_FPS_LIMIT

        try:
            current_colors = setcolor(selected_color_idx)
            hud_content = getlayout(
                layout=selected_layout,
                gpu_load_color=current_colors["gpu_load_color"],
                gpu_color=current_colors["gpu_color"],
                cpu_load_color=current_colors["cpu_load_color"],
                cpu_color=current_colors["cpu_color"],
                posicao=selected_position,
                valor_fps=str(selected_fps_limit),
                valor_scale=f"{selected_scale:.1f}"
            )
            buffer = self.preview_textview.get_buffer()
            buffer.set_text(hud_content)
        except Exception as e:
            buffer = self.preview_textview.get_buffer()
            buffer.set_text(f"Error generating preview:\n{e}")

    def _on_save_clicked(self, button):
        buffer = self.preview_textview.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        hud_content = buffer.get_text(start_iter, end_iter, True).strip()

        dialog = None
        if hud_content and not hud_content.startswith("Error"):
            try:
                save_mangohud_config(hud_content)
                dialog = Adw.MessageDialog.new(self, "Success", "Configuration saved successfully!")
                dialog.add_response("ok", "OK")
                dialog.set_default_response("ok")
            except Exception as e:
                dialog = Adw.MessageDialog.new(self, "Error Saving", f"Could not save configuration:\n{e}")
                dialog.add_response("ok", "OK")
                dialog.set_response_appearance("ok", Adw.ResponseAppearance.DESTRUCTIVE)
        elif hud_content.startswith("Error"):
            dialog = Adw.MessageDialog.new(self, "Error", "Cannot save, there is an error in the preview.")
            dialog.add_response("ok", "OK")
            dialog.set_response_appearance("ok", Adw.ResponseAppearance.DESTRUCTIVE)
        else:
            dialog = Adw.MessageDialog.new(self, "Warning", "Nothing to save. Preview is empty.")
            dialog.add_response("ok", "OK")

        if dialog:
            dialog.connect("response", lambda d, r_id: d.close())
            dialog.present()


class SimpleHUDApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="org.example.SimpleHUD",
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = SimpleHUDMainWindow(application=app)
        self.win.present()

if __name__ == "__main__":
    app = SimpleHUDApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
