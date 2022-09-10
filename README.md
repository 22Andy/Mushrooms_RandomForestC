# Mushrooms_RandomForestC

En este repositorio se tiene encuentra el Notebook donde preprocesan los datos,
se construyen los modelos MUSHROOMS.ipynb.
En el notebook Load_Models.ipynb se tiene como se cargan los modelos para predecir
En el script main.py se tiene tiene el scripyt donde se crea el servicio
En la carpeta DOCKER se tiene cada uno de los archivos que se requieren para construir la imagen 
docker asi como el archivo dockerfile, donde estan los comando para crear la imagen docker desde terminal


para probar el modelo que levantamos con el docker lo podemos hacer con:
curl -X POST "http://localhost:8500/predict/5/3/8/1/0/1/0/0/5/0/2/2/2/7/7/2/1/4/3/2/1"
