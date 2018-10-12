import requests
import xml.etree.ElementTree as ET


querey_url = "https://www.dcstreetcar.com/nextbus/nextbusproxy-3.php?%s"%("command=predictions&a=dc-streetcar&r=h_route&s=ben15west")
prediction_at_stop_url = "https://www.dcstreetcar.com/nextbus/nextbusproxy-3.php?command=predictions&a=dc-streetcar&r=h_route&s=%s"%("ben15west")

wb_stops_list = ["benspurw",
                "benspure",
                "benoakwest",
                "ben19west",
                "ben15west",
                "h13west",
                "h8west",
                "h5west",
                "h3west"]
eb_stops_list = ["benoakeast",
                "ben19east",
                "ben15east",
                "h13east",
                "h8east",
                "h5east",
                "h3east",
                "hunion"]
