### 2.2.12. Archivos

Python permite leer y escribir archivos utilizando la función `open`. Para leer un archivo, se utiliza el modo `r`, y para escribir un archivo, se utiliza el modo `w`.

```python


# Leer un archivo


withopen("archivo.txt","r")as archivo:



    contenido = archivo.read()



    print(contenido)


# Escribir un archivo


withopen("archivo.txt","w")as archivo:



    archivo.write("Hola, mundo!")


```
