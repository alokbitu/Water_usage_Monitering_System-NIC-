# Global Variables
parameters = ["flow", "qty", "roll"]
units = ["m3/hr", "m3/hr", "m3/hr"]
analyzers = ["analyzer_264","analyzer_264","analyzer_264"]
MinMa = [4, 4, 4]
MaxMa= [20, 20, 20]
channels = [0, 1, 2]
maxAbs = [3000, 80, 50]
multiplyFactors = [1, 1, 1]

radius = 800
roll = 1

site_id = "site_9991"
plant_name = "National Informatics Centre"
plant_address1 = "Angul Anugul"
plant_address2 = "759145 Odhisa"
plant_country = "India"
version = "ver1.0"

station_name = "SENDEV-00069-1"
iso_latitude = "20.8653"
iso_longtitude = "85.1842"
fsw = site_id+"_"+station_name+"_"
comport = "/dev/ttyAMA4"

# Grewal AES key
AES256_KEY = "c2l0ZV8yOTgyXnZlcl8xLjBeT1NQQ0Je"

# Site Sunjray Public Key
site_public_key = "MEgCQQCJNEhkm8h3Amcq8MtGM8YalBFP4jA0H1UP/KmnnGzTvwxScHMR2oYveZmP\n4vtCMqIXqLSVifRFZNhdSlGBPd4RAgMBAAE="

# OSPCB Server Public Key
server_public_key = "MEgCQQCcADcRmHrTtDWsknzx5D64iNdwYscWi0+fI8nh9cO26HtRSeXBnSJuMlJK\nis7qn+lznsbi3DRwYOdM4w/7Z8bhAgMBAAE="

# Site private key
site_private_key = "MIIBPQIBAAJBAIk0SGSbyHcCZyrwy0YzxhqUEU/iMDQfVQ/8qaecbNO/DFJwcxHa\nhi95mY/i+0IyoheotJWJ9EVk2F1KUYE93hECAwEAAQJAblm0l+aLltxB6dF9TFs7\nzAim298J8gH5QkBumzY+By7HE2XYghGaVMlJKf76fVQJDuatKEfssOObVPKA3puu\n2QIjAI2hUFJhDMwxtKQ2Fzld9vAGUA/8AYte1FCchjUTVpw6mzcCHwD4AASqa1iZ\njUJr7ydadTK3brrDzB1iM5h8CM8ExPcCIwCLFZqSe7ocoMd7556g+JTzG8/uEpXV\nrzejPkNRxf7tB2S7Ah8AirIX6edXCalCuHJro99fmc7HjLEezcjlQpj6jkRJAiIs\n9kz5PqUTfoDFHUxf97zBqdP98pWofldeWOFjw1M/7yZE"

# IP Addresses
sunjray_hostAddress = "192.168.0.12:9899"

# Sunjray Realtime and Delayed urls
sunjray_realtime_url = "http://103.112.26.250:9899/sunjrayServer/realtimeUpload"
sunjray_delayed_url = "http://103.112.26.250:9899/sunjrayServer/delayedUpload"


# Required directories for project functioning
bkpdir = "BKPFLD"
sunjraydir = "SUNJRAY"
rddir = "RAWDATA"

# Required directories in SUNJRAY  for zipfile storing
rtdir = "Realtime"
dlydir = "Delayed"
