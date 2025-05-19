def horizontal(gpu_load_color, gpu_color, cpu_load_color, cpu_color, posicao, valor_fps, valor_scale): 
    return f"""
    legacy_layout=0
    table_columns=20
    background_alpha=0
    horizontal

    gpu_stats
    gpu_temp
    gpu_load_change
    gpu_load_value=50,90
    gpu_load_color={gpu_load_color}
    gpu_text=GPU
    gpu_color={gpu_color}
    gpu_core_clock

    cpu_stats
    cpu_temp
    cpu_load_change
    core_load_change
    cpu_load_value=50,90
    cpu_load_color={cpu_load_color}
    cpu_color={cpu_color}
    cpu_text=CPU
    cpu_mhz

    vram
    #vram_color=FFAA7F

    ram
    ram_color=62A0EA

    fps
    fps_color_change
    fps_value=30,60,144
    fps_color=b22222,fdfd09,39f900

    engine_color=FFAA7F

    frame_timing=1
    frametime_color=00ff00
    background_alpha=0.4
    font_size=22
    gamemode
    device_battery=gamepad
    gamepad_battery_icon
    vulkan_driver
    position={posicao}
    round_corners=10

    toggle_hud=F1

    fps_limit={valor_fps}
    font_scale={valor_scale}
    """

def vertical(gpu_load_color, gpu_color, cpu_load_color, cpu_color, posicao, valor_fps, valor_scale):
    return f"""
    legacy_layout=false
    gpu_stats
    gpu_temp
    gpu_load_change
    gpu_load_value=50,90
    gpu_load_color={gpu_load_color}
    gpu_text=GPU
    cpu_stats
    cpu_temp
    cpu_load_change
    core_load_change
    cpu_load_value=50,90
    cpu_load_color={cpu_load_color}
    cpu_color={cpu_color}
    cpu_text=CPU
    io_color=a491d3
    vram
    vram_color=FEBD9D
    ram
    ram_color=FEBD9D

    fps
    fps_color_change
    fps_value=30,60,144
    fps_color=b22222,fdfd09,39f900

    engine_color=eb5b5b
    gpu_color={gpu_color}
    wine_color=eb5b5b
    frame_timing=1
    frametime_color=00ff00
    media_player_color=ffffff
    background_alpha=0.4
    font_size=32

    background_color=020202
    position={posicao}
    text_color=ffffff
    round_corners=10

    toggle_hud=F1

    fps_limit={valor_fps}
    font_scale={valor_scale}
    """

def vertical_complete(gpu_load_color, gpu_color, cpu_load_color, cpu_color, posicao, valor_fps, valor_scale): 
    return f"""
    legacy_layout=false

    round_corners=10.0

    gpu_stats
    gpu_temp
    gpu_core_clock
    gpu_mem_clock
    gpu_power
    gpu_load_change
    gpu_load_value=50,90
    gpu_load_color={gpu_load_color}
    gpu_text=GPU
    cpu_stats
    cpu_temp
    core_load
    cpu_power
    cpu_mhz
    cpu_load_change
    core_load_change
    cpu_load_value=50,90
    cpu_load_color={cpu_load_color}
    cpu_color={cpu_color}
    cpu_text=CPU
    io_stats
    io_read
    io_write
    io_color=a491d3
    swap
    vram
    vram_color=ad64c1
    ram
    ram_color=c26693

    fps
    fps_color_change
    fps_value=30,60,144
    fps_color=b22222,fdfd09,39f900
    fps_metrics=avg,0.01,0.001

    engine_version
    engine_color=eb5b5b
    gpu_name
    gpu_color={gpu_color}
    vulkan_driver
    arch
    wine
    wine_color=eb5b5b
    frame_timing=1
    frametime_color=00ff00
    show_fps_limit
    resolution
    gamemode
    gamepad_battery
    gamepad_battery_icon
    battery
    position={posicao}

    toggle_hud=F1

    fps_limit={valor_fps}
    font_scale={valor_scale}
    """
