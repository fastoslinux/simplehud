def set_scale(template, scale):
    scales = []
    for value in range(1, 16):
        scales.append(value / 10)

    if scale not in scales:
        raise ValueError(f"Invalid scale")

    return template.format(scale=scale)