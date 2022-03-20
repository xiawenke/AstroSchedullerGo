from schedule import schedule
from core import core

s = schedule()
s.set_duration(begin = 1627110000, end = 1627196340, format = "timestamp")
s.set_telescope(latitude = 32.7015, longitude = -109.891284, altitude = 3185, velocity = [0.5, 0.6])
s.set_elevation(minimal = 30, maximal = 80)
s.set_escape(sun = 20)
s.add_object(
    identifier= "J0437–4715", 
    ra= "69.3167",
    dec= "-47.2527", 
    duration= "3555"
)
s.add_object(
    identifier= "J1012+5307", 
    ra= "153.13930897",
    dec= "53.11737904", 
    duration= "800", 
    weight= "0.2", 
    important= True
)
# (print(s.to_dict()))
# (print(s.to_json()))
# print(s.to_xml())

coreHandle = core()
coreHandle.update()

s2 = schedule()
s2.from_xml(open("./tests/psr_list_debug.xml").read())
# print(s2.to_xml())
s2.schedule()
s2.stats()