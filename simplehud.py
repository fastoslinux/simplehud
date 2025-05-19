from layout import getlayout
from position import set_position
from scale import set_scale 
from color import setcolor
import os
from flask import Flask, render_template

def sethud():
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
        0: "Padrão",
        1: "Vermelho",
        2: "Verde",
        3: "Azul"
    }

    print("Escolha um layout:")
    for i, layout in enumerate(layouts, 1):
        print(f"{i}. {layout}")
    layout_choice = int(input("Número do layout: "))
    if not 1 <= layout_choice <= len(layouts):
        raise ValueError("Opção de layout inválida.")
    layout_input = layouts[layout_choice - 1]

    print("\nEscolha a posição do HUD:")
    for i, pos in enumerate(positions, 1):
        print(f"{i}. {pos}")
    position_choice = int(input("Número da posição: "))
    if not 1 <= position_choice <= len(positions):
        raise ValueError("Opção de posição inválida.")
    position_input = positions[position_choice - 1]

    scale_input = float(input("\nEscolha a escala (de 0.1 até 1.5, exemplo: 1.0): ").strip())

    print("\nEscolha o perfil de cor:")
    for key, value in colors.items():
        print(f"{key}. {value}")
    color_choice = int(input("Número do perfil de cor: "))
    if color_choice not in colors:
        print("Perfil de cor inválido. Usando Padrão.")
        color_choice = 0
    
    return layout_input, position_input, scale_input, color_choice

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

def save_mangohud_config(hud_content):
    config_dir = os.path.expanduser("~/.config/MangoHud")
    config_file = os.path.join(config_dir, "MangoHud.conf")

    # Cria o diretório se não existir
    os.makedirs(config_dir, exist_ok=True)

    # Escreve o conteúdo no arquivo, substituindo o que houver
    with open(config_file, "w", encoding="utf-8") as f:
        f.write(hud_content)

    print(f"Arquivo MangoHud.conf salvo em: {config_file}")


if __name__ == "__main__":
    layout_input, position_input, scale_input, color_choice = sethud()
    colors = setcolor(color_choice)
    hud_preview = getlayout(
        layout=layout_input,
        gpu_load_color=colors["gpu_load_color"],
        gpu_color=colors["gpu_color"],
        cpu_load_color=colors["cpu_load_color"],
        cpu_color=colors["cpu_color"],
        posicao=position_input,
        valor_fps="0",
        valor_scale=str(scale_input)
    )

    print("\nPreview do HUD com perfil de cor selecionado:")
    print(hud_preview)

    salvar = input("\nDeseja salvar esta configuração no MangoHud.conf? (s/n): ").strip().lower()
    if salvar == "s":
        save_mangohud_config(hud_preview)
    else:
        print("Configuração não salva.")
