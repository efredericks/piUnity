# piUnity

Branch for Unity code for the `piUnity` project.

Each device is on a separate branch:

* Raspberry Pi code is on the `pi` branch
* Unity code is on the `unity` branch

---

Caveat: ensure that the port you are using for UDP communications is unblocked, as well as all ports related to the Unity editor (in Windows, there are some "hidden" firewall rules that block communication to Unity).

There are three scenes currently, one of which is working and two of which were works in progress before my time to update this ended.  **PiScene** is the main scene that you see in the video demo.  **MarbleMaze** had some physics-related issues that I haven't yet resolved, and **ForestMaze** was intended to become some sort of procedurally-generated maze.  If time permits I'll revisit them (though feel free to fork and update if you wish).

In **PiScene**, simply run the project.  Make sure that the Python script on your Pi (or controller faking the sensor readings) is running as well.

`RPIComm.cs` is the main script for this project and defines port 50001 to use as default.  Feel free to re-configure that as you prefer.  
