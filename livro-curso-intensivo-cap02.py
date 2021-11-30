#Strings

##Mudando para Letras maiúsculas e minúsculas
name = "jackson gomes"
print(name.title())
print(name.upper())
print(name.lower())

##Combinando ou Concatenando strings
first_name = "Luiza"
last_name = "love"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
print("Mãe: Marly", "\nPai: José Mário")

##Removendo espaços em branco
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip()) #removendo espaços em branco lado direito
favorite_language = favorite_language.rstrip() #armazenando na variável

favorite_language = " python"
print(favorite_language)
print(favorite_language.lstrip()) #removendo espaços em branco lado esquerdo
favorite_language = favorite_language.rstrip() #armazenando na variável

favorite_language = " python "
print(favorite_language.rstrip().lstrip()) #removendo espaços em branco em ambos os lados
favorite_language = (favorite_language.rstrip().lstrip())