from pathlib import Path

with open(Path(__file__).with_name("carros.txt"), "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())