import json
# Import database module.
from firebase_admin import db

# Get a database reference to our blog.
ref = db.reference('server/saving-data/fireblog')

posts_ref = ref.child('ct-lottery')


# Opening JSON file
f = open('*.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['ct-lottery']:
    posts_ref.push(i)

 
# Closing file
f.close()