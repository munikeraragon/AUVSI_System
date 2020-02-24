# AUVSI System

Front-end and Back-end end system that will be utilized to partcipate in the [AUVSI Student Unmanned Aerial System Competition](https://www.auvsi-suas.org/).

### Table of contents
- [Description](#Description)
- [System Layout](#System_Layout)
- [Completion Status](#Completion_Status)

## Description
This is the developed system that will be utilized by the Clark college's Aerospace clut to participate in the AUVSI-SUAS competion.
### Technologies
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [Django](https://www.djangoproject.com/)
- [MAVSDK-Python](https://github.com/mavlink/MAVSDK-Python)
- [Docker](https://www.docker.com/)
- css/html/bootstrap



## System_Layout
<pre>
AUVSI_System
  /controlcenter
        templates/controlcenter
            -controlCenter.html
            -startConnection.html
            -get_mission.html

            The files below incorporate js scripts to communicate with Google Maps API
            -boundaryGrid.html
            -completeMap.html
            -searchGrid.html
            -wayPointsGrid.html

        -models.py: Entity model that will store InteropServer conneciton info. 
        -connect.py: Performs system call  to Interop Server and request a mission file.
        -views.py: Controls the logic to handle various interface views.
 </pre>





## Completion_Status
#### Completed
##### Front end
- Develop Main page interface
- Develop control ceter interface
- Develop Mission visualization interface<br>

##### Back end
- Created database model for connection.
- Develop scripts to request missions from Interop Server
- Develop scripts to parse mission file
- Created View method to send mission file and convereted to visual Map

#### To complete
- Convert mission coordiantes into world coordinates
- Incorporate PythonRobotics library

