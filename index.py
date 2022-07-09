#programa que leia o nome de uma cidade e diga se ela começa ou não com a plavra "Santo"
cd =str(input('Digite o nome de uma cidade:')).strip()
print(cd[:5].upper() =='SANTO')