import octoprint.plugin
import serial

class OnlinePrinter(octoprint.plugin.BlueprintPlugin, octoprint.plugin.StartupPlugin):
    ser = None

    @octoprint.plugin.BlueprintPlugin.route("/ledon", methods=["GET"])
    def ledON(self):
        if self.ser:
            print("[OnlinePrinterPlugin] Turning LED on")
            self.ser.write(b'LED_ON')
            return "OK", 200
        else:
            return "Failed to initilize serial connection", 500
    
    @octoprint.plugin.BlueprintPlugin.route("/ledoff", methods=["GET"])
    def ledOFF(self):
        if self.ser:
            print("[OnlinePrinterPlugin] Turning LED off")
            self.ser.write(b'LED_OFF')
            return "OK", 200
        else:
            return "Failed to initilize serial connection", 500
    
    @octoprint.plugin.BlueprintPlugin.route("/unlock", methods=["GET"])
    def unlock(self):
        if self.ser:
            print("[OnlinePrinterPlugin] Unlocking")
            print(self.ser)
            self.ser.write(b'UNLOCK')
            return "OK", 200
        else:
            return "Failed to initilize serial connection", 500
    
    def on_startup(self, *args, **kwargs):
        print("[OnlinePrinterPlugin] Starting OnlinePrinterPlugin...")
        try:
            self.ser = serial.Serial('COM1')
        except Exception as e:
            print("[OnlinePrinterPlugin] Failed to initilize COM port")
            print(e)
            return None
        print("[OnlinePrinterPlugin] Successfully initilized COM port")
        print("[OnlinePrinterPlugin] OnlinePrinterPlugin has successfully started.")

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OnlinePrinter()