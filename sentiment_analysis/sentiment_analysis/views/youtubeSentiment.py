import requests


def youtubeSentiment(request, video_id):
    # if something goes wrong you have to do something
    response = requests.post(f'http://localhost:8000/api/v1/elt/{video_id}')
    # after you sent the request, the data will be in the database 
    # get all the data from the database the perform sentiment analsis
    # returning back how much were positive and negative, we need a ratio
    # we need to get sample data entries (9-12) 
    # after we get all that then we can delete everything in the database
    # return back with number of postives and number of negatives, return sample data entries from the database