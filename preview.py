from color import setcolor
from layout import getlayout


def preview_hud(layout, position, scale):
    colors = setcolor(0)  # esquema de cor padrão

    # Você pode passar valores default para fps, ou pegar de outro lugar
    valor_fps = "0"

    hud = getlayout(
        layout=layout,
        gpu_load_color=colors["gpu_load_color"],
        gpu_color=colors["gpu_color"],
        cpu_load_color=colors["cpu_load_color"],
        cpu_color=colors["cpu_color"],
        posicao=position,
        valor_fps=valor_fps,
        valor_scale=str(scale)
    )

    print("\nHUD config:")
    print(hud)