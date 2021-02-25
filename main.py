from lcu_driver import Connector

connector = Connector()

async def boost(connection):
    tboost = await connection.request('post', '/lol-lobby-team-builder/champ-select/v1/team-boost/purchase')
    print(tboost)

@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    if summoner.status == 200:
        await boost(connection)

@connector.close
async def disconnect(_):
    print('')

connector.start()
