import asyncio
import logging
from pyzoe import AsyncZoeClient
from pyzoe.definition.register_names import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
#host='10.2.49.41',
#host='10.2.49.70'
class BatteryController:
    def __init__(self, host='10.2.49.70', port=502):
        """Initialize the battery controller"""
        self.client = AsyncZoeClient(host=host, port=port)
        
    async def connect(self):
        """Connect to the inverter"""
        if not await self.client.connect():
            raise ConnectionError("Failed to connect to inverter")
        logger.info("Successfully connected to inverter")

    async def get_battery_status(self):
        """Get current battery status"""
        try:
            status = {
                serial_number_n: (await  self.client.get(serial_number_n)).value,
                board_serial_number_n: (await self.client.get(board_serial_number_n)).value,
                #pcs_running_state_n: (await  self.client.get(pcs_running_state_n)).value
                #soc_n: (await self.client.get(soc_n)).value,
                grid_frequency_n: (await self.client.get(grid_frequency_n)).value,
            }
            return status
        except Exception as e:
            logger.error(f"Error getting battery status: {e}")
            return None

    async def close(self):
        """Close the client connection"""
        if hasattr(self, 'client'):
            await self.client.close()

async def main():
    controller = None
    try:
        # Create and connect controller
        controller = BatteryController()
        await controller.connect()

        status = await controller.get_battery_status()

        logger.info(f"Status: {status}")

    except Exception as e:
        logger.error(f"Error in main: {e}")
    finally:
        if controller:
            await controller.close()

if __name__ == "__main__":
    asyncio.run(main())