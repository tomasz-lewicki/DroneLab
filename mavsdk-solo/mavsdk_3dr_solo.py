import asyncio
from concurrent.futures import ThreadPoolExecutor

from mavsdk import start_mavlink, connect

start_mavlink(connection_url="udp://:14550")

drone = connect(host="127.0.0.1")

#executor = ThreadPoolExecutor(2)

#doesn't work
#await drone.action.arm()


async def run():
    async for pos in drone.telemetry.position():
        print(pos)

#doesn't work
async def print_flight_mode():
    async for flight_mode in drone.telemetry.flight_mode():
        print("FlightMode:", flight_mode)

loop = asyncio.get_event_loop()

loop.run_until_complete(run())
