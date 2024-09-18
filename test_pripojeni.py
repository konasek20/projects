from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusIOException, ModbusException

# Vytvoření klienta bez argumentu "method"
client = ModbusSerialClient(port='/dev/ttyUSB0', baudrate=9600, timeout=1, parity='N', stopbits=1, bytesize=8) #když na windowsu COM3

try:
    # Připojení ke klientovi
    if client.connect():
        # Čtení registrů
        result = client.read_holding_registers(40001, count=2, unit=1)

        if result is None:
            print("Chyba: Nebyla přijata žádná odpověď z Modbus zařízení.")
        # Zkontrolujte, zda nejsou data prázdná a nedošlo k žádné chybě
        elif not result.isError():  # Kontrola, zda neproběhla chyba
            print(f"Data z registrů: {result.registers}")
        else:
            print(f"Chyba: {result}")
    else:
        print("Chyba: Nepodařilo se připojit k Modbus klientovi.")

except ModbusIOException as e:
    print(f"Chyba při komunikaci s Modbus zařízením (ModbusIOException): {str(e)}")

except ModbusException as e:
    print(f"Obecná chyba Modbus (ModbusException): {str(e)}")

except Exception as e:
    print(f"Neznámá chyba: {str(e)}")

finally:
    client.close()


#Port: Ujistěte se, že používáte správný sériový port, např. /dev/ttyUSB0 na Linuxu nebo COM3 na Windows.
#Baudrate, Parity, Stopbits, Byte Size: Tyto parametry musí odpovídat nastavení invertoru. Například běžné nastavení může být:
#Baudrate: 9600, 19200, nebo jiné, podle zařízení.
#Parity: 'N' (žádná), 'E' (sudá), nebo 'O' (lichá).
#Stopbits: 1 nebo 2.
#Bytesize: 8 (nejběžnější).
