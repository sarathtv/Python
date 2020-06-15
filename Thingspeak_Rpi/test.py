from thingspeakapi import Write_To_thingspeak,Read_From_Thingspeak
import time
global write_key
id=1081891
read_key='0BKKV98L988NHB5D'
write_key="F3YI98GV8UH1HO6B"
data=[500,400,100,200,500,600]

Write_To_thingspeak(data,write_key)
time.sleep(1)
rcv_buf=Read_From_Thingspeak(id,read_key)
print(rcv_buf)