from rflib import RfCat, MOD_ASK_OOK
import bitstring

FREQUENCY = 433906000 #The frequency in Hz
data = '10000000000000000000001101001001001001001101001001001101001001101001001101101101101101001001001000000000000000000000000000000' #Raw binary data
rf_data = bitstring.BitArray(bin=data).tobytes() #Binary data converted to use with YARD Stick One

d = RfCat()

#Setting up the dongle
d.setMdmModulation(MOD_ASK_OOK)
d.setFreq(FREQUENCY)
d.setMdmDRate(2450)
d.setMdmSyncMode(0)

#Transmitting the pattern 10 times
for i in range(10):
    d.RFxmit(rf_data)

d.setModeIDLE()