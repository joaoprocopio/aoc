from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "input.txt"


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
    total = 0

    for line in file:
        index = 0
        last_l_paren_index = None

        while index < len(line):
            char = line[index]
            mul_instr_substr = line[index : index + MUL_INSTR_LEN]

            if mul_instr_substr == MUL_INSTR:
                # aqui dentro desse if, já encontramos a substring que da match em `mul(`
                # pode dar um shift de 3 pro lado, e pegar o index do parenteses esquerdo
                last_l_paren_index = index + len(MUL)
                # agora que encontramos encontramos o que importa, podemos saltar
                # isso aqui já vai cair dentro do corpo do parenteses, é só parsear e multiplicar
                index += MUL_INSTR_LEN
                continue

            if (last_l_paren_index is not None) and (char == R_PAREN):
                l_paren_substr = line[last_l_paren_index + 1 : index]

                if (len(l_paren_substr) in IN_PAREN_RANGE) and (
                    COMMA in l_paren_substr
                ):
                    x, y = l_paren_substr.split(",")

                    if not y.isdigit():
                        y = "".join(char for char in y if char.isdigit())

                    total += int(x) * int(y)

            index += 1

    print(total)
