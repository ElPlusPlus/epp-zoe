from pyzoe.definition.models import ModbusRegister, ModbusType, ModbusUnit

serial_number = ModbusRegister(4127, 12, 3, ModbusType.STRING, ModbusUnit.NONE, gain=1)
