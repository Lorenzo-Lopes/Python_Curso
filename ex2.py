nome= 'Lorenzo'
altura= 1.85
peso = 100

imc = (peso/(altura*altura))

print(f'Seu nome é: {nome}, Seu peso é: {peso}, e sua altura é: {altura} ')
print (f'Calculamos seu imc e o resultado foi; {round(imc,2)}')

if imc<=18.5 :
    print(f'Imc  baixo {imc}')
elif imc > 18.5 and imc <= 24.9:
    print(f'Imc Ideal {imc}')
elif imc >24.9 and imc <= 29.9:
    print(f'Imc levemente acima {imc}')
elif imc >29.9 and imc <= 34.9:
    print(f'Obsidade 1 {imc}')
elif imc >34.9 and imc <= 39.9:
    print(f'Obsidade 2 {imc}')
elif imc >39.9 :
    print(f'Obsidade 3 {imc}')
