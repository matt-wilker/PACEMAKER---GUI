from serial import Serial
import struct
import serial
import sys
import glob
import struct
from serial.tools.list_ports import comports
import time

FRDM_HWID = "1366:1015"  # JLink
NUCLEO_HWID = "0483:374B"  # ST-Link


class serial_packet:

    def __init__(self, user_params):
        self.user_params = user_params

    def __findPorts(self):
        frdmFound = False
        nucleoFound = False
        nucleoPort = ""
        frdmPort = ""
        while (True):
            for port in comports():
                if FRDM_HWID in port.hwid:
                    frdmFound = True
                    frdmPort = port.device
                elif NUCLEO_HWID in port.hwid:
                    nucleoFound = True
                    nucleoPort = port.device
            if (frdmFound and nucleoFound):
                return [nucleoPort, frdmPort]

    def transmit_params(self, fn_code):
        ports = self.__findPorts()

        # Struct.pack everything
        params = b''
        params += struct.pack('B', 1)  # SYNC
        params += struct.pack('B', fn_code)  # FN Code - always going to be set

        params += struct.pack('d', user_params["lrl"])  # LRL
        params += struct.pack('H', user_params["url"])  # URL
        params += struct.pack('f', user_params["aa"])  # AA
        params += struct.pack('f', user_params["va"])  # VA
        params += struct.pack('d', user_params["apw"])  # APW
        params += struct.pack('d', user_params["vpw"])  # VPW
        params += struct.pack('d', user_params["ARP"])  # ARP
        params += struct.pack('d', user_params["VRP"])  # VRP
        params += struct.pack('d', user_params["msr"])  # msr
        params += struct.pack('d', user_params["favd"])  # favd
        params += struct.pack('f', user_params["asen"])  # asen
        params += struct.pack('f', user_params["vsen"])  # vsen
        params += struct.pack('H', user_params["PVARP"])  # PVARP
        params += struct.pack('B', user_params["hys"])  # hys
        params += struct.pack('B', user_params["rs"])  # rs
        params += struct.pack('d', user_params["at"])  # at
        params += struct.pack('d', user_params["rct"])  # rct
        params += struct.pack('d', user_params["rf"])  # rf
        params += struct.pack('d', user_params["rvt"])  # rvt
        params += struct.pack('B', user_params["mode"])  # MODE

        print(len(params))

        with Serial(ports[1], 115200, timeout=3) as pacemaker:
            pacemaker.flush()

            print(ports[1])
            pacemaker.write(params)

            if params[1] == 3:
                receive = pacemaker.read(size=21)

                params = struct.unpack("=dHffddddddffHBBddddB", receive)
                print(params)
                return params

            elif params[1] == 4:
                receive = pacemaker.read(size=37)
                params = struct.unpack("=dHffddddddffHBBddddBdd", receive)
                print("(", params[20], ",", params[21], ")\n")
                atrium_amp = params[20]
                ven_amp = params[21]
                return [atrium_amp, ven_amp]

    def receive_egram(self):
        params = b''
        params += struct.pack('B', 1)  # SYNC
        params += struct.pack('B', 4)  # FN Code - always going to be 4 for receive

        params += struct.pack('H', user_params["lrl"])  # LRL
        params += struct.pack('H', user_params["url"])  # URL
        params += struct.pack('f', user_params["aa"])  # AA
        params += struct.pack('f', user_params["va"])  # VA
        params += struct.pack('H', user_params["apw"])  # APW
        params += struct.pack('H', user_params["vpw"])  # VPW
        params += struct.pack('H', user_params["ARP"])  # ARP
        params += struct.pack('H', user_params["VRP"])  # VRP
        params += struct.pack('H', user_params["msr"])  # msr
        params += struct.pack('H', user_params["favd"])  # favd
        params += struct.pack('H', user_params["asen"])  # asen
        params += struct.pack('H', user_params["vsen"])  # vsen
        params += struct.pack('H', user_params["PVARP"])  # PVARP
        params += struct.pack('H', user_params["hys"])  # hys
        params += struct.pack('H', user_params["rs"])  # rs
        params += struct.pack('H', user_params["at"])  # at
        params += struct.pack('H', user_params["rct"])  # rct
        params += struct.pack('H', user_params["rf"])  # rf
        params += struct.pack('H', user_params["rvt"])  # rvt
        params += struct.pack('B', user_params["mode"])  # MODE

        with Serial(ports[1], 115200, timeout=3) as pacemaker:
            print(ports[1])
            pacemaker.write(params)

            receive = pacemaker.read(size=42)

            params = struct.unpack("=HHffHHHHB", receive)
            print(params)
