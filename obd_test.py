import obd
import time




# OBD setup
obd.logger.setLevel(obd.logging.DEBUG)

# Connect to OBDII adapter
ports = obd.scan_serial()
print("gagan is testing")
connection = obd.OBD(ports[0])


def writetoFile(s):
    f = open("data.txt", "a")
    f.write(s)
    f.close()


# Scheduler 
def repeat():
  
  speedCmd = connection.query(obd.commands.SPEED)
  speedVal = str(speedCmd.value)
  
  fuelCmd = connection.query(obd.commands.FUEL_LEVEL)
  fuelVal = str(fuelCmd.value)
  
  rpmCmd = connection.query(obd.commands.RPM)
  rpmVal = str(rpmCmd.value)
  
  timeCmd = connection.query(obd.commands.RUN_TIME_MIL)
  timeVal = str(timeCmd.value)
  
  oilCmd = connection.query(obd.commands.OIL_TEMP)
  oilVal = str(oilCmd.value)
  
  engineLoadCmd = connection.query(obd.commands.ENGINE_LOAD)
  engineLoadVal = str(engineLoadCmd.value)
  
  coolantTempCmd = connection.query(obd.commands.COOLANT_TEMP)
  coolantTempVal = str(coolantTempCmd.value)
  
  accelerationPosDCmd = connection.query(obd.commands.ACCELERATOR_POS_D)
  accelerationPosDVal = str(accelerationPosDCmd.value)


  
  print("Oil:"+ oilVal)
  print("Time:"+ timeVal)
  print("Speed: " + speedVal + ", fuel: " + fuelVal)
  print("Rpm : "+ rpmVal)
  print("acceleration pas d: "+accelerationPosDVal)
  print("coolant temp:"+coolantTempVal)
  print("engineLoadVal:"+engineLoadVal)
  print("-------------------------------")
  data=oilVal+","+timeVal+","+speedVal+","+fuelVal+","+rpmVal+","+accelerationPosDVal+","+coolantTempVal+","+engineLoadVal+"\n"
  writetoFile(data)
  
  
while True: 
    repeat()
    time.sleep(1)
