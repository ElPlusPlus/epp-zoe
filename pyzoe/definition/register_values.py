from pyzoe.definition.models import ModbusRegister, ModbusType, ModbusUnit

serial_number = ModbusRegister(10000, 8, 3, ModbusType.STRING, ModbusUnit.NONE, gain=1)
