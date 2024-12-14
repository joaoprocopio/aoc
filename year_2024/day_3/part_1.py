from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


MUL = "mul"
L_PAREN = "("
COMMA = ","
R_PAREN = ")"

MUL_INSTR = MUL + L_PAREN
MUL_INSTR_LEN = len(MUL_INSTR)

# procurar dentro da string por `mul(`, guarda o index que começa
# uma vez que encontrar o `mul(`, procurar pelo próximo `)`, guarda o index
# se a diferença entre o index do primeiro parenteses e a do último parenteses estiver entre 3 e 7, aí dá pra fazer o parse a multiplicação

with open(file_path, "r") as file:
    for line in file:
        index = 0
        last_mul_instr_index = 0
        # total = 0

        while index < len(line):
            mul_instr_substr = line[index : index + MUL_INSTR_LEN]

            if mul_instr_substr == MUL_INSTR:
                # encontra e guarda o index da substring que da match em `mul(`
                last_mul_instr_index = index
                # agora que encontramos encontramos o que importa, podemos saltar
                index += MUL_INSTR_LEN
                continue

            index += 1

        # print(total)
