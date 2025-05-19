def setcolor(color):
    """
    Retorna um dicionário com cores conforme o esquema fornecido:
    0 - Padrão (None, para não modificar)
    1 - Vermelho
    2 - Verde
    3 - Azul
    """

    if color == 1:  # Vermelho
        return {
            "gpu_color": "ff4444",
            "cpu_color": "ff8888",
            "gpu_load_color": "ff2222,ff0000",
            "cpu_load_color": "ff2222,ff0000",
        }
    elif color == 2:  # Verde
        return {
            "gpu_color": "44ff44",
            "cpu_color": "88ff88",
            "gpu_load_color": "22ff22,00ff00",
            "cpu_load_color": "22ff22,00ff00",
        }
    elif color == 3:  # Azul
        return {
            "gpu_color": "4444ff",
            "cpu_color": "8888ff",
            "gpu_load_color": "2222ff,0000ff",
            "cpu_load_color": "2222ff,0000ff",
        }
    else:  # 0 ou inválido = default (nenhuma alteração)
        return {
            "gpu_color": "2e9762",
            "cpu_color": "2e97cb",
            "gpu_load_color": "FFFFFF,FFAA7F,CC0000",
            "cpu_load_color": "FFFFFF,FFAA7F,CC0000",
        }
