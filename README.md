# AirBnB_clone_v3: RESTful API

![hbnb](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
* [Requirements](#requirements)
* [File Descriptions](#file-descriptions)
* [Environmental Variables](#environmental-variables)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Description

**hbnb** is a full-stack clone of the web application [AirBnB](https://www.airbnb.com/). This clone was built in four iterative phases. This version includes completion of Phase 1 from [AirBnB_clone_v1: Console and web static](https://github.com/bchen528/AirBnB_clone_v1), Phase 2 from [AirBnB_clone_v2](https://github.com/bchen528/AirBnB_clone_v2) plus Phase 3, which involves exposing stored objects via a JSON web interface and manipulating objects via a custom RESTful API.

### Create a custom RESTful API, expose stored objects via JSON web interface, manipulate objects via custom RESTful API
![restful_api](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step4.png)

**Links to other versions:**
* [AirBnB_clone_v1: Console and web static](https://github.com/bchen528/AirBnB_clone_v1)
* [AirBnB_clone_v2: MySQL, deploy web static, web framework](https://github.com/bchen528/AirBnB_clone_v2)
* [AirBnB_clone_v4: Web dynamic](https://github.com/bchen528/AirBnB_clone_v4) (Final version!)

## Purpose
The purpose of Phase 3 is to learn how to:
* create a RESTful API
* use CORS
* request RESTful API
* retrieve, create, update, delete a resource with HTTP methods

## Requirements
* All files compiled with Ubuntu 14.04 LTS
* Documentation
* Organized files in proper folders
* Python unit tests for all files
* All files must be pep8 compliant

## File Descriptions
  **Note:** Below highlights only new file additions for Phase 2. For Phase 1 file descriptions, click [here](https://github.com/bchen528/AirBnB_clone_v1).
  * [console.py](console.py) - command interpreter from Phase 1 that includes updated `do_create` function that allows object creation with given arameters with syntax `<key name>=<value>`
  * [setup_mysql_dev.sql](setup_mysql_dev.sql) - script that prepares a MySQL development server for the project
  * [setup_mysql_test.sql](setup_mysql_test.sql) - script that prepares a MySQL test server for the project
  * [0-setup_web_static.sh](0-setup_web_static.sh) - Bash script that sets up web servers for `web_static` deployment
  * [1-pack_web_static.py](1-pack_web_static.py) - a Fabric script that generates a .tgz archive from the contents of the `web_static` folder
    * `do_pack` - generates a .tgz archive from the contents of the `web_static` folder using Fabric
  * [2-do_deploy_web_static.py](2-do_deploy_web_static.py) - a Fabric script (based on 1-pack_web_static.py) that distributes an archive to web servers
    * `do_deploy` - distributes an archive to web servers
    * `do_pack` - generates a .tgz archive from the contents of the `web_static` folder using Fabric
  * [3-deploy_web_static.py](3-deploy_web_static.py) - a Fabric script (based on 2-do_deploy_web_static.py) that creates and distributes an archive to my web servers 
    * `deploy` - creates and distributes an archive to web servers
    * `do_deploy` - distributes an archive to web servers
    * `do_pack` - generates a .tgz archive from the contents of the `web_static` folder using Fabric
  * [models](models) - contains models for relevant AirBnB objects
    * [`__init__.py`](models/__init__.py) - switch to file storage or database storage modes
    * [base_model.py](models/base_model.py) - class BaseModel, parent class that will take care of initialization/serialization/deserialization of future instances
      * `__init__` - initialize instance attributes
      * `__str__` - returns formatted string representation of instance
      * `__repr__` - returns string representation of instance
      * save - updates `updated_at` attribute for new instance
      * to_dict - returns dictionary representation a BaseModel object
    * [user.py](models/user.py) - class User
    * [city.py](models/city.py) - class City
    * [state.py](models/state.py) - class State
    * [place.py](models/place.py) - class Place
      * `reviews` - get list of Review instances with place_id (equals current Place.id)
      * `amenities` getter - returns list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
      * `amenities` setter - adds an Amenity.id to attribute amenity_ids if obj is an instance of Amenity
    * [review.py](models/review.py) - class Review
    * [amenity.py](models/amenity.py) - class Amenity
  * [tests](/tests/) - unit test files
  * [engine](models/engine) - contains storage engines
    * [`__init__.py`](/models/engine/__init__.py) - empty `__init__.py` file for packages
    * [file_storage.py](/models/engine/file_storage.py) - class FileStorage; serializes instances to JSON file and deserializes from a JSON file
      * `all` - returns the dictionary `__objects`
      * `new` - sets in `__objects` the obj with key `<obj class name>.id`
      * `save` - serializes `__objects` to the JSON file (path: `__file_path`)
      * `reload` - deserializes the JSON file to `__objects`
      * `delete` - delete object from `__objects` if exists
      * `close` - call reload
    * [db_storage.py](/models/engine/db_storage.py) - class DBStorage; 
      * `__init__` - initalize instances
      * `all` - return dictionary of instance attributes
      * `new` - add new object to current database session
      * `save` - commit all changes of the current database session
      * `delete` - delete from the current database session obj if not None
      * `reload` - create all tables in database and current database session
      * `close` - close session


## Environmental Variables
```
HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
HBNB_MYSQL_USER: the username of your MySQL
HBNB_MYSQL_PWD: the password of your MySQL
HBNB_MYSQL_HOST: the hostname of your MySQL
HBNB_MYSQL_DB: the database name of your MySQL
HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
```

## Usage
Run the following in your terminal:
```
user@ubuntu:~/AirBnB_v2$ curl -o 100-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
user@ubuntu:~/AirBnB_v2$ cat 100-dump.sql | mysql -uroot -p
Enter password: 
user@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
Open up a web browser and type `0.0.0.0:5000/hbnb`.
Voila! You should see a lovely webpage like below:
  ![8-index.html_part0](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb_0.jpg)

## Bugs

At this time, there are no known bugs.

## Authors
Phase 3:
* Becky Chen | [GitHub](https://github.com/bchen528) | [Twitter](https://twitter.com/bchen803)
* Alex Allen | [GitHub](https://github.com/aDENTinTIME) | [Twitter](https://twitter.com/adentintime)

Phase 2 codebase: (For practice working with new codebases)
* Melissa Ng | [Github](https://github.com/MelissaN)
* Adriel Tolentino | [Github](https://github.com/adrielt07)

Phase 1 codebase: (For practice working with new codebases)
* Binita Rai | [Github](https://github.com/rayraib)
* Steven Garcia | [Github](https://github.com/stvngrcia)

## License

**hbnb** is open source and free to download and use
