meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY":  "aterrador, siniestro"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(word,':', meme_dict[word])
else:
    print("Esa palabra no está en el diccionario, revisa si has escritó bien")
    
    
