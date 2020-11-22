
def get_simple_url():
    base_url = 'https://www.google.com/maps/dir/'
    params = {
        "origin": '59.945851,+30.239241',
        "destination": '59.944623959247785,+30.237818894104013'}
    base_url += f"{params['destination']}/{params['origin']}"
    return base_url
