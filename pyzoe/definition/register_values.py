from pyzoe.definition.models import ModbusRegister, ModbusType, ModbusUnit

serial_number = ModbusRegister(4142, 12, 3, ModbusType.STRING, ModbusUnit.NONE, gain=1)

soc = ModbusRegister(20109, 1, 4, ModbusType.U16, ModbusUnit.PERCENTAGE, gain=0.1)
