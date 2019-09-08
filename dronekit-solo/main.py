from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command

vehicle = connect("udp:0.0.0.0:14552", wait_ready=True)

vehicle.mode = VehicleMode('HOLD')