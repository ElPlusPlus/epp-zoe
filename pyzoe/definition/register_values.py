from pyzoe.definition.models import ModbusRegister, ModbusType, ModbusUnit

device_communication_status = ModbusRegister(26, 1, 3, ModbusType.U16, ModbusUnit.NONE)
emu_status = ModbusRegister(56, 1, 3, ModbusType.U16, ModbusUnit.NONE)
emu_boot_ver = ModbusRegister(59, 1, 3, ModbusType.U16, ModbusUnit.NONE)
emu_s_ver = ModbusRegister(60, 1, 3, ModbusType.U16, ModbusUnit.NONE)
emu_h_ver = ModbusRegister(61, 1, 3, ModbusType.U16, ModbusUnit.NONE)

board_serial_number = ModbusRegister(4142, 12, 3, ModbusType.STRING, ModbusUnit.NONE)
serial_number = ModbusRegister(4142, 12, 3, ModbusType.STRING, ModbusUnit.NONE)

# Historical data
history_year_month = ModbusRegister(4600, 1, 3, ModbusType.U16, ModbusUnit.NONE)
history_day_hour = ModbusRegister(4601, 1, 3, ModbusType.U16, ModbusUnit.NONE)
history_minute_second = ModbusRegister(4602, 1, 3, ModbusType.U16, ModbusUnit.NONE)
history_systick = ModbusRegister(4603, 1, 3, ModbusType.U16, ModbusUnit.NONE)
history_pcs_charge_energy = ModbusRegister(4604, 2, 3, ModbusType.I32, ModbusUnit.KWH, gain=0.1)
history_pcs_discharge_energy = ModbusRegister(4606, 2, 3, ModbusType.I32, ModbusUnit.KWH, gain=0.1)
history_battery_charge_energy = ModbusRegister(4608, 2, 3, ModbusType.I32, ModbusUnit.KWH, gain=0.1)
history_battery_discharge_energy = ModbusRegister(4610, 2, 3, ModbusType.I32, ModbusUnit.KWH, gain=0.1)

# Operation Logs
operation_datetime = ModbusRegister(9600, 9, 3, ModbusType.STRING, ModbusUnit.NONE)
operation_status_tag = ModbusRegister(9612, 5, 3, ModbusType.STRING, ModbusUnit.NONE)
operation_event_description = ModbusRegister(9617, 32, 3, ModbusType.STRING, ModbusUnit.NONE)


#Battery
battery_communication_status = ModbusRegister(20104, 1, 3, ModbusType.U16, ModbusUnit.NONE)
battery_cluster_total_voltage = ModbusRegister(20105, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=0.01)
battery_cluster_total_current = ModbusRegister(20107, 2, 3, ModbusType.I32, ModbusUnit.NONE, gain=0.01)
battery_cluster_soc = ModbusRegister(20109, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, gain=0.1)


soc = ModbusRegister(24682, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, gain=0.1)
pcs_running_state = ModbusRegister(40005, 1, 3, ModbusType.U16, ModbusUnit.NONE)

grid_frequency = ModbusRegister(40018, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=0.01)
