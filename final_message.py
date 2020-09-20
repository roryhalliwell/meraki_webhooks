import requests
import json
import webex_post
import config

def final_post(webhook):
    #check if the dictionary exists. Bool will reutrn false if a key is found and true if empty.
    if bool(webhook["alertData"]) is True:
      if 'clientName' in webhook["alertData"]:
        message = "Rory an issue occured!\nDevice Name: "+webhook["deviceName"]+"\nAlert : "+webhook["alertType"]+"\nClient is: "+webhook["alertData"].get("clientName")+"\nMac: "+webhook["alertData"].get("mac")+"\nIP Address: "+webhook["alertData"].get("ip")
        webex_post.post_room_message('Meraki Home', message)
      else:
        message = "Rory an issue occured!\nDevice Name: "+webhook["deviceName"]+"\nAlert is: "+webhook["alertType"]
        webex_post.post_room_message('Meraki Home', message)
    else:
      message = "Rory an issue occured!\nDevice Name: "+webhook["deviceName"]+"\nAlert is: "+webhook["alertType"]
      webex_post.post_room_message('Meraki Home', message)
    return True