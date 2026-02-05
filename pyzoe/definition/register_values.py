from pyzoe.definition.models import ModbusRegister, ModbusType, ModbusUnit

board_serial_number = ModbusRegister(4142, 12, 3, ModbusType.STRING, ModbusUnit.NONE)
serial_number = ModbusRegister(4142, 12, 3, ModbusType.STRING, ModbusUnit.NONE)

soc = ModbusRegister(24682, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, gain=0.1)
pcs_running_state = ModbusRegister(40005, 1, 3, ModbusType.U16, ModbusUnit.NONE)

grid_frequency = ModbusRegister(40018, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=0.01)
