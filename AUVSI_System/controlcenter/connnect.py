from auvsi_suas.client import client
from auvsi_suas.proto import interop_api_pb2

def connect(URL,Userame,Password):
    client = client.Client(url=URL,
                        username=Userame,
                        password=Password)
    teams = client.get_teams()
    mission = client.get_mission(1)
    print(teams)
    print(mission)