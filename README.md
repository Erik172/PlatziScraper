# PlatziScraper

_Programa para hacer web scraping al sitio web de [platzi](https://platzi.com), extrae todos los cursos y posts del sitio, este proyecto tambien hace parte del proyecto(*no official*) [PlatziAPI](https://github.com/Erik172/PlatziAPI)_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Requisitos 📋

- [Scrapy](https://scrapy.org/) - _Framework para el web scraping_
- [Shub](https://shub.readthedocs.io/en/stable/) - _Para el despliege en [scrapinghub]() (**Opcional**)_
- [scrapyd](https://scrapyd.readthedocs.io/en/stable/) - _para el despliegue local (**Opcional**)_

```
pip install scrapy
```
(***Opcional***)
Para hacer el despliegue en [scrapinghub](https://app.scrapinghub.com/)
```
pip install shub
```

(***Opcional***)
para hacer un despliegue local puedes instalar scrapyd
```
pip install scrapyd
```  

### Instalación 🔧

_Para poder ejecutar el programa simplemente debemos clonar el repositorio, instalar las dependencias y iniciar el programa_

```
git clone https://github.com/Erik172/PlatziScraper.git
```

```
cd PlatziScraper
```

_con este comando podemos ejecutar el spider platzi si queremos ejecutar el spider de blog solo tenemos que cambiar **platzi** por ***blog***_

```
scrapy crawl platzi
```
_al finalizar nos va a dejar un archivo **json** con el nombre del spider, en este caso **platzi.json**_

<!-- ## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
``` -->

<!-- ## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

### Despliegue en ScrapingHub

### Despliege en una maquina -->

## Construido con 🛠️

* [Python3](https://www.python.org/) - Lenguaje de Programacion
* [Scrapy](https://scrapy.org/) - Framework para el web scraping

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

<!-- ## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki) -->

<!-- ## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags). -->

## Autores ✒️

* **Erik Garcia** - *Programador* - [Erik172](https://github.com/Erik172)

<!-- También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto.  -->

## Licencia 📄

Este proyecto está bajo la Licencia **MIT** - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Gracias al profesor [@facmartoni](https://twitter.com/facmartoni) por enseñarme a usar el framework **Scrapy** 🤓.

## Cursos de Platzi Recomendados
* [Curso Básico de Python](https://platzi.com/cursos/python/)
* [Curso de Fundamentos de Web Scraping con Python y Xpath](https://platzi.com/cursos/web-scraping/)
* [Curso De Scrapy](https://platzi.com/cursos/scrapy/)

---
hecho con ❤️ por [Erik172](https://github.com/Erik172) 😊
