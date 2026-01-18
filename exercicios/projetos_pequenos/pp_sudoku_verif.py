###
## Escrever um programa que:
## * leia 9 linhas do Sudoku
## * verifique se os dados introduzidos são válidos
## * faz o output Yes se o Sudoku for válido, e No caso contrário
## Regras sudoku :
## cada linha do tabuleiro deve conter obrigatoriamente os dígitos de 1 a 9 (a ordem não importa).
## cada coluna do tabuleiro deve conter obrigatoriamente os dígitos de 1 a 9 (a ordem não importa).
## cada uma das nove "regiões" 3x3 (sub-quadrados) da tabela deve conter obrigatoriamente os dígitos de 1 a 9.

# Dicionário com todas as posições
dicionario = {
    # LINHAS (9 linhas)
    "linha1": ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1"],
    "linha2": ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2"],
    "linha3": ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3"],
    "linha4": ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4"],
    "linha5": ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5"],
    "linha6": ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6"],
    "linha7": ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7"],
    "linha8": ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8"],
    "linha9": ["a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9"],
    
    # COLUNAS (9 colunas)
    "coluna1": ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"],
    "coluna2": ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"],
    "coluna3": ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"],
    "coluna4": ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9"],
    "coluna5": ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9"],
    "coluna6": ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"],
    "coluna7": ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"],
    "coluna8": ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9"],
    "coluna9": ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9"],
    
    # QUADRANTES (9 regiões 3x3)
    "quadrante1": ["a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"],
    "quadrante2": ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"],
    "quadrante3": ["g1", "h1", "i1", "g2", "h2", "i2", "g3", "h3", "i3"],
    "quadrante4": ["a4", "b4", "c4", "a5", "b5", "c5", "a6", "b6", "c6"],
    "quadrante5": ["d4", "e4", "f4", "d5", "e5", "f5", "d6", "e6", "f6"],
    "quadrante6": ["g4", "h4", "i4", "g5", "h5", "i5", "g6", "h6", "i6"],
    "quadrante7": ["a7", "b7", "c7", "a8", "b8", "c8", "a9", "b9", "c9"],
    "quadrante8": ["d7", "e7", "f7", "d8", "e8", "f8", "d9", "e9", "f9"],
    "quadrante9": ["g7", "h7", "i7", "g8", "h8", "i8", "g9", "h9", "i9"]
}

def validar_sudoku():
    """
    Recebe 9 linhas de input com números de 1 a 9
    e valida se formam um Sudoku válido
    """
    print("=" * 50)
    print("VALIDADOR DE SUDOKU")
    print("=" * 50)
    print("\nDigite as 9 linhas do Sudoku (apenas números de 1 a 9, sem espaços):")
    print("Exemplo: 123456789")
    
    # Receber as 9 linhas
    linhas_input = []
    for i in range(1, 10):
        while True:
            try:
                linha = input(f"Linha {i}: ").strip()
                
                # Validar entrada
                if len(linha) != 9:
                    print("ERRO: A linha deve ter exatamente 9 caracteres!")
                    continue
                
                if not linha.isdigit():
                    print("ERRO: A linha deve conter apenas números!")
                    continue
                
                # Converter para lista de inteiros
                numeros = [int(num) for num in linha]
                
                # Verificar se todos os números estão entre 1 e 9
                if any(num < 1 or num > 9 for num in numeros):
                    print("ERRO: Os números devem estar entre 1 e 9!")
                    continue
                
                linhas_input.append(numeros)
                break
                
            except ValueError:
                print("ERRO: Entrada inválida!")
    
    print("\n" + "=" * 50)
    print("ANALISANDO SUDOKU...")
    print("=" * 50)
    
    # Criar um dicionário para mapear cada célula ao seu valor
    valores = {}
    
    # Preencher o dicionário de valores
    for linha_num, numeros in enumerate(linhas_input, 1):
        chave_linha = f"linha{linha_num}"
        celulas_linha = dicionario[chave_linha]
        
        for i, celula in enumerate(celulas_linha):
            valores[celula] = numeros[i]
    
    # Função para verificar se um grupo tem duplicados
    def grupo_valido(celulas):
        """Verifica se um grupo de células não tem números repetidos"""
        numeros = [valores[celula] for celula in celulas]
        # Um grupo válido deve ter exatamente os números 1-9 sem repetições
        return sorted(numeros) == list(range(1, 10))
    
    # Verificar todas as LINHAS
    print("\n--- VERIFICANDO LINHAS ---")
    linhas_validas = True
    for i in range(1, 10):
        celulas = dicionario[f"linha{i}"]
        if grupo_valido(celulas):
            print(f"✓ Linha {i}: VÁLIDA")
        else:
            print(f"✗ Linha {i}: INVÁLIDA - Números repetidos ou faltando")
            linhas_validas = False
    
    # Verificar todas as COLUNAS
    print("\n--- VERIFICANDO COLUNAS ---")
    colunas_validas = True
    for i in range(1, 10):
        celulas = dicionario[f"coluna{i}"]
        if grupo_valido(celulas):
            print(f"✓ Coluna {i}: VÁLIDA")
        else:
            print(f"✗ Coluna {i}: INVÁLIDA - Números repetidos ou faltando")
            colunas_validas = False
    
    # Verificar todos os QUADRANTES
    print("\n--- VERIFICANDO QUADRANTES ---")
    quadrantes_validos = True
    for i in range(1, 10):
        celulas = dicionario[f"quadrante{i}"]
        if grupo_valido(celulas):
            print(f"✓ Quadrante {i}: VÁLIDO")
        else:
            print(f"✗ Quadrante {i}: INVÁLIDO - Números repetidos ou faltando")
            quadrantes_validos = False
    
    # Resultado final
    print("\n" + "=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)
    
    if linhas_validas and colunas_validas and quadrantes_validos:
        print("O Sudoku é VÁLIDO!")
        return True
    else:
        print("O Sudoku é INVÁLIDO!")
        
        # Mostrar quais regras foram violadas
        problemas = []
        if not linhas_validas:
            problemas.append("linhas")
        if not colunas_validas:
            problemas.append("colunas")
        if not quadrantes_validos:
            problemas.append("quadrantes")
        
        print(f"Problemas encontrados em: {', '.join(problemas)}")
        return False

# Função para exibir o Sudoku de forma organizada
def exibir_sudoku(valores):
    """Exibe o Sudoku em formato de grade"""
    print("\nSUDOKU INSERIDO:")
    print("+" + "---+" * 9)
    
    for linha_num in range(1, 10):
        linha_str = "|"
        for coluna_letra in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
            celula = f"{coluna_letra}{linha_num}"
            linha_str += f" {valores.get(celula, ' ')} |"
        
        print(linha_str)
        
        # Adicionar separadores para quadrantes
        if linha_num % 3 == 0 and linha_num != 9:
            print("+" + "---+" * 9)
        elif linha_num == 9:
            print("+" + "---+" * 9)
        else:
            print("|" + "   |" * 9)

# Executar o validador
if __name__ == "__main__":
    resultado = validar_sudoku()
    