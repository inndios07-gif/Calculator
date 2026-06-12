def calculadora():
    """
    Programa de calculadora simples que realiza operações matemáticas básicas.
    Solicita ao usuário uma operação e dois números, e retorna o resultado.
    Repete até que o usuário digite "saída".
    """
    
    print("=" * 40)
    print("      BEM-VINDO À CALCULADORA")
    print("=" * 40)
    
    while True:
        # Solicita a operação
        print("\nOperações disponíveis:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair (saída)")
        
        operacao = input("\nEscolha uma operação (+, -, *, /) ou digite 'saída' para sair: ").strip().lower()
        
        # Verifica se o usuário quer sair
        if operacao == "saída" or operacao == "sair":
            print("\n" + "=" * 40)
            print("Obrigado por usar a Calculadora!")
            print("Até logo! 👋")
            print("=" * 40)
            break
        
        # Valida a operação
        operacoes_validas = ['+', '-', '*', '/']
        if operacao not in operacoes_validas:
            print("❌ Operação inválida! Use +, -, * ou /")
            continue
        
        # Solicita o primeiro número
        try:
            numero1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("❌ Por favor, digite um número válido!")
            continue
        
        # Solicita o segundo número
        try:
            numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("❌ Por favor, digite um número válido!")
            continue
        
        # Realiza a operação
        if operacao == '+':
            resultado = numero1 + numero2
            operacao_nome = "Adição"
        elif operacao == '-':
            resultado = numero1 - numero2
            operacao_nome = "Subtração"
        elif operacao == '*':
            resultado = numero1 * numero2
            operacao_nome = "Multiplicação"
        elif operacao == '/':
            if numero2 == 0:
                print("❌ Erro: não é possível dividir por zero!")
                continue
            resultado = numero1 / numero2
            operacao_nome = "Divisão"
        
        # Exibe o resultado
        print("\n" + "=" * 40)
        print(f"Operação: {operacao_nome}")
        print(f"{numero1} {operacao} {numero2} = {resultado}")
        print("=" * 40)


if __name__ == "__main__":
    calculadora()
