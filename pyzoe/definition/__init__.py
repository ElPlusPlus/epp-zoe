from pyzoe.definition.register_names import *
from pyzoe.definition.register_values import *

modbus_map = {
    device_communication_status_n: device_communication_status,
    emu_status_n: emu_status,
    emu_boot_ver_n: emu_boot_ver,
    emu_s_ver: emu_s_ver,
    emu_h_ver: emu_h_ver,
    serial_number_n: serial_number,
    soc_n: soc,
    pcs_running_state_n: pcs_running_state,
    board_serial_number_n: board_serial_number,
    grid_frequency_n: grid_frequency,
}