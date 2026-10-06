
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def exibir_menu():
    print("\n" + "="*35)
    print("      CONVERSOR DE TEMPERATURAS")
    print("="*35)
    print("[1] Celsius para Fahrenheit")
    print("[2] Celsius para Kelvin")
    print("[3] Fahrenheit para Celsius")
    print("[4] Fahrenheit para Kelvin")
    print("[5] Kelvin para Celsius")
    print("[6] Kelvin para Fahrenheit")
    print("[0] Sair")
    print("="*35)

def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n⚠️ Erro: Digite apenas números inteiros válidos!")
            continue

        if opcao == 0:
            print("\nEncerrando o programa. Até logo!")
            break

        if opcao < 1 or opcao > 6:
            print("\n⚠️ Opção inválida! Escolha um número entre 0 e 6.")
            continue

        try:
            valor = float(input("Digite o valor da temperatura: "))
        except ValueError:
            print("\n⚠️ Erro: Digite um valor numérico válido para a temperatura!")
            continue

        # Processamento das escolhas
        if opcao == 1:
            resultado = celsius_para_fahrenheit(valor)
            print(f"\nResult: {valor:.2f}°C equivalem a {resultado:.2f}°F")
        elif opcao == 2:
            resultado = celsius_para_kelvin(valor)
            print(f"\nResult: {valor:.2f}°C equivalem a {resultado:.2f}K")
        elif opcao == 3:
            resultado = fahrenheit_para_celsius(valor)
            print(f"\nResult: {valor:.2f}°F equivalem a {resultado:.2f}°C")
        elif opcao == 4:
            resultado = fahrenheit_para_kelvin(valor)
            print(f"\nResult: {valor:.2f}°F equivalem a {resultado:.2f}K")
        elif opcao == 5:
            resultado = kelvin_para_celsius(valor)
            print(f"\nResult: {valor:.2f}K equivalem a {resultado:.2f}°C")
        elif opcao == 6:
            resultado = kelvin_para_fahrenheit(valor)
            print(f"\nResult: {valor:.2f}K equivalem a {resultado:.2f}°F")

if __name__ == "__main__":
    main()