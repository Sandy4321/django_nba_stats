import requests
import MySQLdb

db = MySQLdb.connect(host="localhost",  user="fred",  db="nba_analysis")
cur = db.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS id_player("
#             "id INTEGER PRIMARY KEY,"
#             "first_name text,"
#             "middle_name text,"
#             "last_name text,"
#             "from_year INTEGER,"
#             "to_year INTEGER);")

###########################
#SCRAPE PLAYER/ ID AND POPULATE MySQL#
###########################
player_id_url = 'http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2014-15'
player_id_json = requests.get(player_id_url).json()
player_id_index = {}

for i  in range(0, len(player_id_json['resultSets'][0]['rowSet'])):
    full_name = str(player_id_json['resultSets'][0]['rowSet'][i][5]).split('_')
    print(full_name)

    if full_name[0] == 'HISTADD':
        if len(full_name) < 3:
            first_name = full_name[1]
            middle_name = "NULL"
            last_name = "NULL"
        elif len(full_name) > 3:
            first_name = full_name[1]
            middle_name = full_name[2]
            last_name = full_name[3]
        else:
            first_name = full_name[1]
            middle_name = "NULL"
            last_name = full_name[2]

    else:
        if len(full_name) < 2:
            first_name = full_name[0]
            middle_name = "NULL"
            last_name = "NULL"
        elif len(full_name) > 2:
            first_name = full_name[0]
            middle_name = full_name[1]
            last_name = full_name[2]
        else:
            first_name = full_name[0]
            middle_name = "NULL"
            last_name = full_name[1]

    id =player_id_json['resultSets'][0]['rowSet'][i][0]
    from_year = player_id_json['resultSets'][0]['rowSet'][i][3]
    to_year = player_id_json['resultSets'][0]['rowSet'][i][4]
    try:
        cur.execute("INSERT INTO id_player VALUES( %s , %s, %s, %s, %s, %s);",  (str(id), first_name, middle_name, last_name,str( from_year), str(to_year)))
        db.commit()
    except:
        print("Player already in DB")
    player_id_index[i] =id

###########################
#SCRAPE GAME LOG AND POPULATE MySQL#
###########################
id_list = []
cur.execute("SELECT * FROM id_player WHERE to_year = 2015 && from_year < 2015;")
for row in cur:
    id_list.append(int(row[0]))

#OBTAIN PLAYERS GAME LOGS AND STORE TO MYSQL
for players in range(0, len(id_list)):
    game_log_url = 'http://stats.nba.com/stats/playergamelog?' \
             'LeagueID=00&' \
             'PlayerID=' + str(id_list[players]) + '&' \
             'Season=ALL&' \
             'SeasonType=Regular+Season'
    game_log_json = requests.get(game_log_url).json()
    game_log_result = game_log_json['resultSets'][0]['rowSet']

    for i in range(0,  len(game_log_result)):
        print(str(players) + "," + str(i))
        #Season,Game,Player IDs
        season_id = str(game_log_result[i][0])
        player_id = str(game_log_result[i][1])
        game_id = str(game_log_result[i][2])

        #Date Played
        date = str(game_log_result[i][3]).replace("," , "").split(" ")
        game_month = date[0]
        game_day = date[1]
        game_year = date[2]

        #Teams involved
        teams = str(game_log_result[i][4]).split(" ")
        home_away = 1 #1 == home, 0 == away
        if teams[1] == '@':
            home_away = 0
        team = teams[0]
        opp_team  = teams[2]

        #Win/Loss
        game_result =str(game_log_result[i][5])
        win_loss = '1'
        if game_result == 'L':
            win_loss = '0'

        #In-Game Stats
        minutes =str(game_log_result[i][6])
        fgm = str(game_log_result[i][7])
        fga = str(game_log_result[i][8])
        fg_pct = str(game_log_result[i][9])
        fg3m = str(game_log_result[i][10])
        fg3a = str(game_log_result[i][11])
        fg3_pct = str(game_log_result[i][12])
        ftm = str(game_log_result[i][13])
        fta = str(game_log_result[i][14])
        ft_pct = str(game_log_result[i][15])
        if fta == "0":
            ft_pct = "NULL"
        oreb = str(game_log_result[i][16])
        dreb = str(game_log_result[i][17])
        reb = str(game_log_result[i][18])
        ast = str(game_log_result[i][19])
        stl = str(game_log_result[i][20])
        blk = str(game_log_result[i][21])
        tov = str(game_log_result[i][22])
        foul = str(game_log_result[i][23])
        pts = str(game_log_result[i][24])
        plus_minus = str(game_log_result[i][25])

        cur.execute("INSERT INTO GAME_LOG VALUES("
                    "%s, %s, %s, %s, %s, %s,"
                    " %s, %s, %s, %s, %s, %s,"
                    " %s, %s, %s, %s, %s, %s,"
                    " %s, %s, %s, %s, %s, %s,"
                    " %s, %s, %s, %s, %s, %s);",
                    (season_id, player_id, game_id, game_month, game_day, game_year,
                     home_away, team, opp_team, win_loss, minutes, fgm,
                     fga, fg_pct, fg3m, fg3a, fg3_pct, ftm,
                     fta,  ft_pct, oreb,dreb, reb, ast,
                     stl, blk, tov, foul, pts, plus_minus))
        db.commit()
