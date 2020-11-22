import requests



def get_simple_url(origin, dest):
    base_url = 'https://www.google.com/maps/dir/'
    params = {
        "origin": origin, # 59.945851,+30.239241
        "destination": dest} # 59.944623959247785,+30.237818894104013
    base_url += f"{params['destination']}/{params['origin']}" # 59.944623959247785,+30.237818894104013
    return base_url
