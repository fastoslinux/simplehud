from layout import getlayout
from color import setcolor
from save import save_mangohud_config
from input import sethud 



if __name__ == "__main__":
    layout_input, position_input, scale_input, color_choice, fps_limit_input = sethud()
    colors = setcolor(color_choice)
    hud_preview = getlayout(
        layout=layout_input,
        gpu_load_color=colors["gpu_load_color"],
        gpu_color=colors["gpu_color"],
        cpu_load_color=colors["cpu_load_color"],
        cpu_color=colors["cpu_color"],
        posicao=position_input,
        valor_fps=str(fps_limit_input), 

        valor_scale=str(scale_input)
    )

    print("\nPreview")
    print(hud_preview)

    salvar = input("\nDeseja salvar esta configuração no MangoHud.conf? (s/n): ").strip().lower()
    if salvar == "s":
        save_mangohud_config(hud_preview)
    else:
        print("Configuração não salva.")
