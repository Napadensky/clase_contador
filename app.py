class Conter:  
    def print_words(self):
        try:  
            nombre_archivo = input('\n \nIntroduce el nombre del archivo y su extencion como txt:  ').strip()
            archivo = open(nombre_archivo)
            objeto_archivo_texto = archivo.read()
            words_separadas = objeto_archivo_texto.split()
            words = dict()

            for palabra in words_separadas: 
                if palabra in words:  
                    words[palabra] += 1
                else:
                    words[palabra] = 1

            input('\n Enter para continuar y ver las 10 más repetidas\n') # Aqui enter para saber los resultados

            words_acomodadas = sorted(words, key = words.get, reverse=True) #Esto se supone nos regresa tuplas para trabajar con ellas
            for palabra in words_acomodadas[0:10]:
                    print('\n', '-> ' + palabra, ':', words[palabra])

        except:
            print('-- Algo salió mal --\n Verifica, puede ser que el archivo este mal escrito o no exista ')

task = Conter()
task.print_words()