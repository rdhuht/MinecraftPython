# MinecraftPython
Sample Python scripts and notes for using the Python mpi library for manipulating and working with Minecraft.  
I use these scripts and the library to explore Python3.  

## Getting Started 
You'll need a Minecraft setup that supports interaction via API.  
This is most simply achieved with the Minecraft for Raspberry Pi, but can also work with full blown Minecraft Java Servers with the [Raspberry Juice Server](https://github.com/zhuowei/RaspberryJuice).  

> Details of setting up the server side are out of scope for these instructions, it is assumed you already have the server running and a game client connected.  


1. Setup a Python virtual environment.  Python3.x was used with these examples and is recommended.  Install 

```bash
python -m venv venv
```

2. Install `mpi` 

```bash
pip install mpi
```

3. Verify all is working by running the following in an interpreter.  

```python
from mpi.minecraft import Minecraft

name = "Yourname"
# connect to minecraft
address = "MinecraftServerAddress"
mc = Minecraft.create(address)

# get the x,y,z (position)
entity_id = mc.getPlayerEntityId(name)
position = mc.entity.getPos()

# print position to screen
print("x: {}, y: {}, z: {}".format(position.x, position.y, position.z))
```

## Resources and References 
* [Learn to Program with Minecraft](https://nostarch.com/programwithminecraft)  
* [https://github.com/martinohanlon/mpi](https://github.com/martinohanlon/mpi)
* [https://github.com/zhuowei/RaspberryJuice](https://github.com/zhuowei/RaspberryJuice)
* [https://www.stuffaboutcode.com/p/minecraft-api-reference.html](https://www.stuffaboutcode.com/p/minecraft-api-reference.html) 
* [https://minecraft-stuff.readthedocs.io/en/latest/index.html](https://minecraft-stuff.readthedocs.io/en/latest/index.html)
* [sphinx docs](https://blog.csdn.net/lly1122334/article/details/103970663)
