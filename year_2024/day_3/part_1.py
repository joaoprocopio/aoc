from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


MUL = "mul"
L_PAREN = "("
COMMA = ","
R_PAREN = ")"

# procurar dentro da string por `mul(`, guarda o index que começa
# uma vez que encontrar o `mul(`, procurar pelo próximo `)`, guarda o index
# se a diferença entre o index do primeiro parenteses e a do último parenteses estiver entre 3 e 7, aí dá pra fazer o parse a multiplicação

with open(file_path, "r") as file:
    for line in file:
        pass
