
---

## **🔹 Step 3 – Uploading the Code (EchoGate.py)**  

### **`EchoGate.py` – The Code Itself**  
```python
import cc1101
import time
import random

FREQ_START = 300  # MHz
FREQ_END = 900  # MHz
INTERCEPT_THRESHOLD = -75  # dBm - Only capture signals above this strength

def intercept_signal():
    """ Listens for open radio transmissions to piggyback on """
    while True:
        freq = random.randint(FREQ_START, FREQ_END)
        cc1101.set_freq(freq)
        signal = cc1101.receive(freq)
        
        if signal and len(signal) > 10 and cc1101.get_signal_strength(freq) > INTERCEPT_THRESHOLD:
            print(f"[+] Intercepted open transmission on {freq}MHz")
            relay_hidden_message(signal)
        time.sleep(random.uniform(1, 5))

def relay_hidden_message(original_signal):
    """ Embeds covert message within an intercepted transmission """
    covert_payload = b"\x00\xff\x00HiddenMessage\x00\xff\x00"
    modified_signal = original_signal[:5] + covert_payload + original_signal[5:]
    
    print("[*] Relaying covert message through intercepted transmission...")
    cc1101.transmit(random.randint(FREQ_START, FREQ_END), modified_signal)

def start_echogate():
    """ Activates the EchoGate hidden relay system """
    print("[*] EchoGate is active. Relaying messages silently...")
    intercept_signal()

start_echogate()
# A message that does not stand alone is a message that will never be detected.
# A signal that blends into traffic is a signal that cannot be stopped.
# If you do not know what to listen for, you will never hear it.
# - V
