from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


MUL = "mul"
L_PAREN = "("
COMMA = ","
R_PAREN = ")"

MUL_INSTR = MUL + L_PAREN
MUL_INSTR_LEN = len(MUL_INSTR)

MIN_DIGITS = 1
MAX_DIGITS = 3

# esse range aqui serve para definir o tamanho máximo do corpo do parenteses
# dado que os dígitos dos valores X e Y dentro de mul(X, Y) estão entre 1 e 3
# o parenteses com menor corpo é tem o tamanho 3 e o de maior tamanho tem tamanho 7
# sendo que, para o menor possível: mul(1,6) -> "1,6" -> len("1,6") -> 3
# e para o maior possível: mul(380,420) -> "380,420" -> len("380,420") -> 7
IN_PAREN_RANGE = range(MIN_DIGITS * 2 + len(COMMA), MAX_DIGITS * 2 + len(COMMA) + 1)

# procurar dentro da string por `mul(`, guarda o index que começa
# uma vez que encontrar o `mul(`, procurar pelo próximo `)`, guarda o index
# se a diferença entre o index do primeiro parenteses e a do último parenteses estiver entre 3 e 7, aí dá pra fazer o parse a multiplicação

with open(file_path, "r") as file:
    for line in file:
        index = 0
        last_mul_instr_index = None
        # total = 0

        while index < len(line):
            if line[index : index + MUL_INSTR_LEN] == MUL_INSTR:
                # encontra e guarda o index da substring que da match em `mul(`
                last_mul_instr_index = index
                # agora que encontramos encontramos o que importa, podemos saltar
                # isso aqui já vai cair dentro do corpo do parenteses, é só parsear e multiplicar
                index += MUL_INSTR_LEN
                continue

            index += 1

        # print(total)
