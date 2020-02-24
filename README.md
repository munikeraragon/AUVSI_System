# AUVSI System

Front-end and Back-end end system that will be utilized to partcipate in the [AUVSI Student Unmanned Aerial System Competition](https://www.auvsi-suas.org/).

### Table of contents
- Description
- System layout
- Completion status

## Description
This is the developed system that will be utilized by the Clark college's Aerospace clut to participate in the AUVSI-SUAS competion.
### Technologies
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [Django](https://www.djangoproject.com/)
- [MAVSDK-Python](https://github.com/mavlink/MAVSDK-Python)
- [Docker](https://www.docker.com/)
- css/html/bootstrap



## System_layout
AUVSI_System
 <p style="text-indent: 40px">Control Center</p>
 <p style="text-indent: 60px">-templates/controlcenter<br>

 <p style="text-indent: 100px"> -controlCenter.html</p>
 <p style="text-indent: 100px"> -startConnection.html</p>
 <p style="text-indent: 100px"> -get_mission.html</p>

 <p style="text-indent: 100px"> The files below incorporate js scripts to communicate with Google Maps API</p>
 <p style="text-indent: 100px"> -boundaryGrid.html</p>
 <p style="text-indent: 100px"> -completeMap.html</p>
 <p style="text-indent: 100px"> -searchGrid.html</p>
 <p style="text-indent: 100px"> -wayPointsGrid.html</p>

 </p>
 
 <p style="text-indent: 60px">-models.py: Entity model that will store InteropServer conneciton info. </p>
 <p style="text-indent: 60px">-connect.py: Performs system call  to Interop Server and request a mission file.</p>
 <p style="text-indent: 60px">-views.py: Controls the logic to handle various interface views.</p>
 





## Completion_status
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

