import requests
import json

#Custom function to write data to thingspeak
#Args -Data: payload that you want to transmit
#	   write_key : Write API key from thingspeak
# gives status of the get request

def Write_To_thingspeak(data,write_key):
	api_str="https://api.thingspeak.com/update?api_key="
	msg_buff=""
	#populate the API field for data from the arg list passed
	for i in range(len(data)):
		assert  len(data) <= 8,"Maximum 8 Fields Allowed in Thingspeak"
		msg_buff=msg_buff+"&field"+str(i+1)+ "=" +str(data[i])
	
	#Concatenate the string to form the GET request
	tx_buff=api_str+write_key+msg_buff
	response=requests.get(tx_buff)
	if response.status_code == 200:
		print('Success!')
	elif response.status_code == 404:
		print('Not Found.')

#Function to Read from a channel
#Args- channel_id :id of the channel in thingspeak
#read key :Read API key from thingspeak
#returns a dictionary of fields with values

def Read_From_Thingspeak(channel_id,read_key):
	recieved_data={}
	rqst="https://api.thingspeak.com/channels/"+str(channel_id)+"/feeds.json?api_key="+read_key+"&results=1" # 1 indicates the latest one reading from the channel. 
	response=requests.get(rqst)
	j_data=response.json() #convert it to dictionary
	num_field=len(j_data['feeds'][0])-2 # This finds the number of fields in the feed
	for i in range(num_field):
		recieved_data['field'+str(i+1)]=(j_data['feeds'][0]['field'+str(i+1)])  # copy the values to a dictionary and return that dictionary 
	return(recieved_data)



# Additional links
# https://realpython.com/python-requests/#the-response  