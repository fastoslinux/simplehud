def set_position(template,position):
    positions = {
        "top-left",
        "top-right",
        "middle-left",
        "middle-right",
        "bottom-left",
        "bottom-right",
        "top-center",
        "bottom-center"
    }
    if position not in positions:
        raise ValueError(f"Invalid position")
    return template.format(position=position)
    