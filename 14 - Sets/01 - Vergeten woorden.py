def vergeten_woorden(tekst, verplichte_woorden):
    aantal, lijst = len(verplichte_woorden), set(tekst.split())
    gebruikte_woorden = len(verplichte_woorden.intersection(lijst))
    return aantal, aantal - gebruikte_woorden, gebruikte_woorden



print(vergeten_woorden('hello world world world',{'python', 'world', 'hello', 'java'}))
print(vergeten_woorden('',{'python', 'world', 'hello', 'java'}))