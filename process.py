
import pandas as pd
import datetime 


#from datetime import datetime
#start = datetime(2026, 6, 1)
#end = datetime(2026, 6, 10)
#difference = end - start

#print(difference.days)

#Last Cams Data
def Cam_Data():
    # Read in the data
    cms = pd.read_excel('Cam Data.xlsx')
    #convert the LAST CAMS Position column to datetime
    cms["Last CAMS Position"] = pd.to_datetime(cms["Last CAMS Position"])
    
    # Convert date column to datetime
    cms['Fleet Last Event'] = pd.to_datetime(cms['Fleet Last Event'])
    #Fleet Last Comms
    cms['Fleet Last Comms'] = pd.to_datetime(cms['Fleet Last Comms'])
    #Fleet Last Ignition to datetime
    cms['Fleet Last Ignition'] = pd.to_datetime(cms['Fleet Last Ignition'])
    #Fleet last GPS to datetime
    cms['Fleet Last GPS'] = pd.to_datetime(cms['Fleet Last GPS'])
    #Last GPRS ONfp to datetime
    cms['Last GPRS Info'] = pd.to_datetime(cms['Last GPRS Info'])




    return cms


def Camera_Stat():
    #importing the last online data
    lso = pd.read_excel('Camera_Status_Report.xlsx')
    
    # Convert date column to datetime
    lso['Last Online'] = pd.to_datetime(lso['Last Online'])
    #Last Download to datetime
    lso['Last Download'] = pd.to_datetime(lso['Last Download'])
    
    return lso


def compared_dates(lso,cms,capdata):
    #Last online to last CAMS position
    cms["Last_CAM_Pos"]=(lso['Last Online']-cms['Last CAMS Position']).dt.days

    #Last online to Fleet Last Event
    cms["FLEET_LAST_EVENT"]=(lso['Last Online']-cms['Fleet Last Event']).dt.days

    #Last online to Fleet Last Comms
    cms["FLEET_COMMS"]=(lso['Last Online']-cms['Fleet Last Comms']).dt.days

    #Last online to Fleet Last Ignition
    cms["FLEET_IGNITION"]=(lso['Last Online']-cms['Fleet Last Ignition']).dt.days

    #Last online to Fleet Last GPS
    cms["FLEET_GPS"]=(lso['Last Online']-cms['Fleet Last GPS']).dt.days

    #Last online to Last GPRS Info
    cms["GPRS_INFO"]=(lso['Last Online']-cms['Last GPRS Info']).dt.days


    return cms["Last_CAM_Pos"], cms["FLEET_LAST_EVENT"], cms["FLEET_COMMS"], cms["FLEET_IGNITION"], cms["FLEET_GPS"], cms["GPRS_INFO"]

def logic(lso,cms):
    #working with greater than 2 days
    if cms["Last_CAM_Pos"] > 2:
        print("CaAMS Position is worrysome check the values")
    else:
        print("Last Online is good")

    #Last Fleet Event to Last Online
    if cms["FLEET_LAST_EVENT"] > 2:
        print("Fleet Last Event is worrysome check the values")
    else:
        print("Last Online is good")

   #Last online to Fleet Last Comms 
    if cms["FLEET_COMMS"] > 2:
        print("Fleet Last Comms is worrysome check the values")
    else:
        print("Last Online is good")
    
    #Last online to Fleet Last Ignition
    if cms["FLEET_IGNITION"] > 2:
        print("Fleet Last Ignition is worrysome check the values")
    else:
        print("Last Online is good")
    
    #Last online to Fleet Last GPS
    if cms["FLEET_GPS"] > 2:
        print("Fleet Last GPS is worrysome check the values")
    else:
        print("Last Online is good")
    
    #Last online to Last GPRS Info
    if cms["GPRS_INFO"] > 2:
        print("Last GPRS Info is worrysome check the values")
    else:
        print("Last Online is good")
    
