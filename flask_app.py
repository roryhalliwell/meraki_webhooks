
# A very simple Flask Hello World app for you to get started with...

import requests
import json
import webex_post
import config
import final_message
import meraki_time
from flask import Flask
from flask import request
import waitress
import meraki
# Application input
from config import API_KEY, url_guest_ssid

dashboard = meraki.DashboardAPI(api_key=API_KEY, output_log=False, print_console=False)
my_orgs = dashboard.organizations.getOrganizations()
orgId = my_orgs[0]["id"]
networks = dashboard.organizations.getOrganizationNetworks(orgId)
networkid = networks[0]["id"]

app = Flask(__name__)

# Parse a webhook and send API call to disable raspberrypi
@app.route('/shut_pi',methods=["POST"])
def shut_pi():
    for x in dashboard.networks.getNetworkDevices(networkid):
        if x["name"] == "Switch":
            swserial = x["serial"]
    dashboard.switch.updateDeviceSwitchPort(serial=swserial, portId="8", enabled=False)
    return "shut"

# Parse a webhook and send API call to enable raspberrypi
@app.route('/enable_pi',methods=["POST"])
def enable_pi():
    for x in dashboard.networks.getNetworkDevices(networkid):
        if x["name"] == "Switch":
            swserial = x["serial"]
    dashboard.switch.updateDeviceSwitchPort(serial=swserial, portId="8", enabled=True)
    return "open"

@app.route('/meraki', methods=["POST"])
def get_webhook_json():
    global webhook
    # Webhook Receiver
    webhook = request.json
    # Return success message
    meraki_time.time_test(webhook)
    return "WebHook POST Received"