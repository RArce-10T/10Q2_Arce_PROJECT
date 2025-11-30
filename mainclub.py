# Dictionaries
from pyscript import display, document #type:ignore



def club1(e):
    club1 = {
        "name": "Greek Council",
        "description": "The most popular club in Monsters University, the Greek Council hosts the annual Scare Games, and do all things scary",
        "meeting_time":"Every wednesdays at 2:30 PM",
        "location":"Scaring School Floor 104",
        "club_moderator": "Ms. Claire Wheeler",
        "number_of_monsters": 889,
    }

# clears all entries
    document.getElementById('output').innerHTML = ""
    document.getElementById('info').innerHTML = ""

     # Displays club information using strings
    display(f'Club name: ', target="info")
    display(f'description: ', target="info")
    display(f'meeting Time: ', target="info")
    display(f'location: ', target="info")
    display(f'Club moderator : ', target="info")
    display(f'# of monsters: ', target="info")

    display(f'{club1['name']}', target="output")
    display(f'{club1['description']}', target="output")
    display(f'{club1['meeting_time']}', target="output")
    display(f'{club1['location']}', target="output")
    display(f'{club1['club_moderator']}', target="output")
    display(f'{club1['number_of_monsters']}', target="output")

def club2(e):
    club2 = {
        "name": "Debate Club",
        "description": "Debate with monsters and compete for the power of knowledge and intelligence!",
        "meeting_time":"Every Monday at 4:30 PM",
        "location":"Liberal Arts School Floor 304",
        "club_moderator": "Mr. Snowpiercer",
        "number_of_monsters": 676,
    }

    # clears all entries
    document.getElementById('output').innerHTML = ""
    document.getElementById('info').innerHTML = ""

    display(f'Club name: ', target="info")
    display(f'description: ', target="info")
    display(f'meeting Time: ', target="info")
    display(f'location: ', target="info")
    display(f'Club moderator : ', target="info")
    display(f'# of monsters: ', target="info")

    display(f'{club2['name']}', target="output")
    display(f'{club2['description']}', target="output")
    display(f'{club2['meeting_time']}', target="output")
    display(f'{club2['location']}', target="output")
    display(f'{club2['club_moderator']}', target="output")
    display(f'{club2['number_of_monsters']}', target="output")

def club3(e):
    club3 = {
        "name": "Arts Club",
        "description": "Showcase your creativity and spirit through the beautiful aspects of art!",
        "meeting_time":"Every Monday at 3:00 PM",
        "location":"Scaring School Floor 203",
        "club_moderator": "Ms. Chroma",
        "number_of_monsters": 754,
    }

    # clears all entries
    document.getElementById('output').innerHTML = ""
    document.getElementById('info').innerHTML = ""

    display(f'Club name: ', target="info")
    display(f'description: ', target="info")
    display(f'meeting Time: ', target="info")
    display(f'location: ', target="info")
    display(f'Club moderator : ', target="info")
    display(f'# of monsters: ', target="info")

    display(f'{club3['name']}', target="output")
    display(f'{club3['description']}', target="output")
    display(f'{club3['meeting_time']}', target="output")
    display(f'{club3['location']}', target="output")
    display(f'{club3['club_moderator']}', target="output")
    display(f'{club3['number_of_monsters']}', target="output")


