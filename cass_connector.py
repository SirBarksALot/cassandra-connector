from cassandra.cluster import Cluster
from horology import timed


@timed
def insert_item(connection_object, var):
    name = 'wood'
    unique_name = name + f'_{var}'
    craftable = True
    rarity = 'common'
    requirements = {'tree': 1}
    connection_object.execute(
        '''INSERT INTO items (
    id, name, unique_name, craftable, rarity, requirements, creation_time
    )
    VALUES (
    uuid(), %(name)s, %(unique_name)s, %(craftable)s, %(rarity)s, %(requirements)s, toTimestamp(now())
    )''',
        {
            'name': name,
            'unique_name': unique_name,
            'craftable': craftable,
            'rarity': rarity,
            'requirements': requirements
         }
    )


@timed
def insert_items(connection_object):
    amount_to_insert = 15000
    for i in range(amount_to_insert):
        insert_item(connection_object, i)


@timed
def connection_handler():
    cluster = Cluster(contact_points=['35.195.24.202'], port=9042, metrics_enabled=True)
    session = cluster.connect()
    session.set_keyspace('logs')
    insert_items(session)
    cluster.shutdown()


connection_handler()

# query = session.execute(f'''CREATE TABLE items(
#   id uuid,
#   name text,
#   unique_name text,
#   craftable boolean,
#   rarity text,
#   requirements map<text, int>,
#   creation_time timestamp,
#   PRIMARY KEY (id, unique_name)
# )''')
