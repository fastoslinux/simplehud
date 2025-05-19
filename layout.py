from profile import horizontal, vertical, vertical_complete

def getlayout(layout, gpu_load_color, gpu_color, cpu_load_color, cpu_color, posicao, valor_fps, valor_scale):
    if layout == "horizontal":
        return horizontal(gpu_load_color, gpu_color, cpu_load_color, cpu_color, posicao, valor_fps, valor_scale)
    elif layout == "vertical":
        return vertical(gpu_load_color, gpu_color, cpu_load_color, cpu_color, posicao, valor_fps, valor_scale)
    elif layout == "completo":
        return vertical_complete(gpu_load_color, gpu_color, cpu_load_color, cpu_color, posicao, valor_fps, valor_scale)
    else:
        raise ValueError(f"Layout desconhecido: {layout}")
