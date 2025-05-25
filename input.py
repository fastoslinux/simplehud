def sethud() -> tuple[str, str, float, int, int]:
    """
    Collects HUD configuration settings from the user.

    Returns:
        tuple[str, str, float, int, int]: A tuple containing the selected
                                          layout, position, scale, color choice (key),
                                          and FPS limit.
    """
    layouts = ["horizontal", "vertical", "completo"]
    positions = [
        "top-left",
        "top-right",
        "middle-left",
        "middle-right",
        "bottom-left",
        "bottom-right",
        "top-center",
        "bottom-center"
    ]
    colors = {
        0: "Default",
        1: "Red",
        2: "Green",
        3: "Blue"
    }

    # Layout selection
    print("\nChoose a layout:")
    for i, layout_name in enumerate(layouts, 1):
        print(f"{i}. {layout_name}")
    while True:
        try:
            layout_choice_idx = int(input(f"Layout number (1-{len(layouts)}): "))
            if 1 <= layout_choice_idx <= len(layouts):
                layout_input = layouts[layout_choice_idx - 1]
                break
            else:
                print(f"Invalid option. Please choose a number between 1 and {len(layouts)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Position selection
    print("\nChoose the HUD position:")
    for i, pos_name in enumerate(positions, 1):
        print(f"{i}. {pos_name}")
    while True:
        try:
            position_choice_idx = int(input(f"Position number (1-{len(positions)}): "))
            if 1 <= position_choice_idx <= len(positions):
                position_input = positions[position_choice_idx - 1]
                break
            else:
                print(f"Invalid option. Please choose a number between 1 and {len(positions)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Scale input
    while True:
        try:
            scale_str = input("\nChoose the scale (from 0.1 to 1.5, e.g., 1.0): ").strip()
            scale_input = float(scale_str)
            if 0.1 <= scale_input <= 1.5:
                break
            else:
                print("Scale value out of allowed range (0.1 to 1.5). Try again.")
        except ValueError:
            print("Invalid input. Please enter a number for the scale (e.g., 1.0).")

    # Color profile selection
    print("\nChoose a color profile:")
    for key, value in colors.items():
        print(f"{key}. {value}")
    while True:
        try:
            color_choice_str = input(f"Color profile number ({', '.join(map(str, sorted(colors.keys())))}): ").strip()
            color_choice_key = int(color_choice_str)
            if color_choice_key in colors:
                break
            else:
                print("Invalid color profile. Using Default (0).")
                color_choice_key = 0
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # FPS limit input
    while True:
        try:
            fps_limit_str = input("\nSet FPS limit (0 for unlimited, e.g., 60): ").strip()
            fps_limit_input = int(fps_limit_str)
            if fps_limit_input >= 0:
                break
            else:
                print("FPS limit cannot be negative. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer for the FPS limit.")

    return layout_input, position_input, scale_input, color_choice_key, fps_limit_input
