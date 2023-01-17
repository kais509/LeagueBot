from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'shhh its a secret'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'kai509')
print(me)
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)


def getLastMach():
    my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

    # fetch last match detail
    last_match = my_matches['matches'][0]
    match_detail = watcher.match.by_id(my_region, last_match['gameId'])

    clashT = watcher.clash.tournaments(my_region)
    clashM = watcher.clash.by_summoner(my_region,me['id'])
    print(clashM)





    participants = []
    for row in match_detail['participants']:
        participants_row = {}
        participants_row['champion'] = row['championId']
        participants_row['spell1'] = row['spell1Id']
        participants_row['spell2'] = row['spell2Id']
        participants_row['win'] = row['stats']['win']
        participants_row['kills'] = row['stats']['kills']
        participants_row['deaths'] = row['stats']['deaths']
        participants_row['assists'] = row['stats']['assists']
        participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        participants_row['goldEarned'] = row['stats']['goldEarned']
        participants_row['champLevel'] = row['stats']['champLevel']
        participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
        participants_row['item0'] = row['stats']['item0']
        participants_row['item1'] = row['stats']['item1']
        participants.append(participants_row)

    # check league's latest version
    latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
    # Lets get some champions static information
    static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

    # champ static list data to dict for looking up
    champ_dict = {}
    for key in static_champ_list['data']:
        row = static_champ_list['data'][key]
        champ_dict[row['key']] = row['id']
    for row in participants:
        
        row['championName'] = champ_dict[str(row['champion'])]
        row['champion']= row['championName']




    df = pd.DataFrame(participants)
    #print(df)

def jasonTFT():
    jayson = watcher.summoner.by_name('na1',"cosmowaffles")
    print(jayson)



jasonTFT()
