import wpilib

stick = None
drive = None

def robotInit():
  global stick, drive
  stick = wpilib.Joystick(1)
  drive = wpilib.RobotDrive((wpilib.CANTalon(0)), (wpilib.CANTalon(1)))

def teleopPeriodic():
  global drive, stick
  drive.arcadeDrive((stick.getAxis(1)), (stick.getAxis(0)))