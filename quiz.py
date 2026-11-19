while True:
  pontos = 0
  soma = int(input("\nQual é a soma de 5+5: "))
  if(soma == 10):
    print("reposta correta")
    pontos += 1
    print(f"seus pontos são:{pontos}")
  else:
    print("resposta errada")

  Brasil = int(input("\nQuantos estados tem o Brasil:  "))
  if(Brasil == 27):
    print("reposta correta")
    pontos += 1
    print(f"seus pontos são:{pontos}")
  else:
    print("resposta errada")

  oceanos = int(input("\nQuantos oceanos existem: "))
  if(oceanos == 4):
    print("reposta correta")
    pontos += 1
    print(f"seus pontos são:{pontos}")
  else:
    print("resposta errada")

  ossos = int(input("\nQuantos ossos tem um adulto saudavel: "))
  if(ossos == 206):
    print("reposta correta")
    pontos += 1
    print(f"seus pontos são:{pontos}")
  else:
    print("resposta errada")

  elementos = int(input("\nQuantos elementos ha na tabela periodica: "))
  if(elementos == 118):
    print("reposta correta")
    pontos += 1
    print(f"seus pontos são:{pontos}")
  else:
    print("resposta errada")

  print(f"\nseus pontos finais são: {pontos}")
  if pontos == 5:
    print("\nParabens voce atingiu a pontuação maxima")
    break
  else:
    print(f"\nComo sua pontuação foi {pontos} você não atingiu a pontuação maxima de 5 pontos")
    print("Você retornara ao inicio")
      