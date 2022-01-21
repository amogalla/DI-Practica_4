# Herramientas utilizadas

### Herramientas de diseño
El diseño original se ha realizado en papel, y se ha trasladado al programa Qt Designer, con el podemos diseñar y crear interfaces gráficas de usuario. Posteriormente, este diseño, ya definitivo, es el que se ha convertido a código python para PySide6.

### Herramientas de desarrollo
La herramienta utilizada ha sido el editor de texto Visual Studio Code, que ha sido muy útil para el desarrollo de código en lenguaje Python, su depuración, e integración con control de versiones Git.

### Herramientas de prueba
Las pruebas unitarias del componente se han llevado a cabo con la librería **unittest**. Con ella se ha probado tanto la creación de los componentes como los valores de sus atributos.

Por otro lado, las pruebas de interacción se han realizado con la librería **qtbot**, con la que hemos comprobado el comportamiento del componente ante los posibles eventos que puede realizar el usuario.

### Librerías
Las librerías utilizadas en el desarrollo, además de las comentadas en el apartado anterior para las pruebas, son las siguientes:
- QtWidgets, necesaria para la utilización del MainWindow y de los layouts. También se ha utilizado para poder modificar la opacidad del componente, por medio de *QGraphicsOpacityEffect*
- QtCore, necesaria para establecer el tamaño del componente, y para definir algunos de sus atributos como propiedades (properties).
