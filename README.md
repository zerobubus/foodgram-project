
# Project Title
foodgram-project - project, where people can create, share and save cooking recipes

### Prerequisites

Need to install Docker.

For Windows or MacOS  - https://www.docker.com/products/docker-desktop
Instructions for Linux:

curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh 


### Installing

In the project directory run terminal and use command 'docker-compose up'

In another terminal use command 'docker conteiner ls' to see running conteiners.

In list will be 3 conteiners( first - project , second - db, third - nginx)

Need to enter in project conteiner. Use command 'docker exec -it <CONTAINER ID> bash'

Then use in order this commands:

'python manage.py migrate'
'python manage.py collectstatic'
'exit'

Done. Project running in 0.0.0.0:8000 - gunicorn, 0.0.0.0 - nginx

Now project running in http://84.252.130.63

## Technologies

A list of technologies used within the project:
* [Python](https://www.python.org/): Version 3.8.5
* [linux ubuntu](https://releases.ubuntu.com/20.04/): Version 20.04
* [Docker](https://www.docker.com/): Version 20.10.2
* [Git](https://git-scm.com/downloads): Version 2.25.1
* [Visual Studio Code](https://code.visualstudio.com/): Version 1.53.2

## Authors

**Konstantin Malov** - *Initial work* - [zerobubus](https://github.com/zerobubus)

## License&copyrirht

Copyright © 2021 Konstantin Malov






