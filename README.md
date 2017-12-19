# BsPipe #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Pipeline tools for Asset creation to asset publish, and shot build to cache publish. 
* Version
v-0.1

### How do I get set up? ###

* copy "bsw_programation" folder in any directory.
* make project folder.
* Dependencies (python standard library functions and some add-on site-packages.)
* Database configuration (MySQL)
* Deployment instructions will share soon.

### Folder Structure ###

* if project is series then folder structure is to be like
* base directory.
* project folder.
    * "01_pre"
        * "00_inputs"
        * "01_char"
            * "ep000"
                * "kicko"
                    * "01_design"
                        * "version"
                    * "02_model"
                        * "version"
                    * "03_texture"
                        * "sourceimages"
                        * "version"
                    * "04_light"
                        * "version"
                    * "05_rig"
                        * "version"
            * "ep001"
                * "drCrazy"
                    * "01_design"
                        * "version"
                    * "02_model"
                        * "version"
                    * "03_texture"
                        * "sourceimages"
                        * "version"
                    * "04_light"
                        * "version"
                    * "05_rig"
                        * "version"
        * "02_props"
            * "ep000"
                * "bottle"
                    * "01_design"
                        * "version"
                    * "02_model"
                        * "version"
                    * "03_texture"
                        * "sourceimages"
                        * "version"
                    * "04_light"
                        * "version"
                    * "05_rig"
                        * "version"
        * "03_set"
        * "04_setElement"
        * "05_vehicle"
    * "02_prod"
    * "03_post"

### Python Site Packages list ###
* standard library packages
* pymysql
