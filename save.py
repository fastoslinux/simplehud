import os

def save_mangohud_config(hud_content):
    config_dir = os.path.expanduser("~/.config/MangoHud")
    config_file = os.path.join(config_dir, "MangoHud.conf")

    # Cria o diretório se não existir
    os.makedirs(config_dir, exist_ok=True)

    # Escreve o conteúdo no arquivo, substituindo o que houver
    with open(config_file, "w", encoding="utf-8") as f:
        f.write(hud_content)

    print(f"Arquivo MangoHud.conf salvo em: {config_file}")