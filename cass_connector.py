from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time


auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(contact_points=['35.194.33.244'], port=9042, metrics_enabled=True, auth_provider=auth_provider)
session = cluster.connect()
session.set_keyspace('graph')

name = 'wood'
unique_name = name + '_0'
craftable = True
rarity = 'common'
requirements = {'tree': 1}
#query = session.execute(f'''CREATE TABLE items(
#   id uuid,
#   name text,
#   unique_name text,
#   craftable boolean,
#   rarity text,
#   requirements map<text, int>,
#   creation_time timestamp,
#   PRIMARY KEY (id, unique_name)
#)''')

#query = session.execute(
#    '''INSERT INTO items (
#    id, name, unique_name, craftable, rarity, requirements, creation_time
#    )
#    VALUES (
#    uuid(), %(name)s, %(unique_name)s, %(craftable)s, %(rarity)s, %(requirements)s, toTimestamp(now())
#    )''',
#    {
#        'name': name,
#        'unique_name': unique_name,
#        'craftable': craftable,
#        'rarity': rarity,
#        'requirements': requirements
#     }
#)
query = session.execute()
cluster.shutdown()

print(time.perf_counter())
