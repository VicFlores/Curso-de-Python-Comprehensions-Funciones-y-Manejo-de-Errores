try:
    print(0/0)

    assert 1 + 1 == 3, "La suma de 1 + 1 deberia ser 2"

    age = 10

    if age < 18:
        raise Exception("Eres menor de edad")

except ZeroDivisionError as error:
    print("No se puede dividir por cero")
    print(error)

except AssertionError as error:
    print("No se cumple la condicion")
    print(error)

except Exception as error:
    print("No eres mayor de edad")
    print(error)

print("Todo salio bien o mal")
