#ranking algorithm for now. very flawed, will update later
import MySQLdb

def get_player_id(season):
    temp_list = []
    cur.execute("SELECT * FROM id_player WHERE to_year=" + str(season) + " AND from_year<" + str(season) + ";")
    for row in cur:
        temp_list.append(int(row[0]))
    return temp_list

db = MySQLdb.connect(host="localhost",  user="fred",  db="nba_analysis")
cur = db.cursor()
avg = []
std = []
id_list = []

##Get Averages and Standard Deviations
query = ("SELECT AVG(games_played), AVG(min), AVG(fgm),"
            "AVG(fga), AVG(fg_pct), AVG(fg3m), AVG(fg3a),"
            "AVG(fg3_pct),AVG(ftm),AVG(fta), AVG(ft_pct),"
            "AVG(oreb), AVG(dreb), AVG(reb), AVG(ast), AVG(stl), AVG(blk),"
            "AVG(tov), AVG(atr), AVG(pts)"
            " FROM avg_2015"
             ";")
cur.execute(query)
db_get = cur.fetchone()
for i in range(0, len(db_get)):
    avg.append(float(db_get[i]))

query = ("SELECT STDDEV(games_played), STDDEV(min), STDDEV(fgm),"
            "STDDEV(fga), STDDEV(fg_pct), STDDEV(fg3m), STDDEV(fg3a),"
            "STDDEV(fg3_pct),STDDEV(ftm),STDDEV(fta), STDDEV(ft_pct),"
            "STDDEV(oreb), STDDEV(dreb), STDDEV(reb),  STDDEV(ast), STDDEV(stl), STDDEV(blk),"
            "STDDEV(tov), STDDEV(atr), STDDEV(pts)"
            " FROM avg_2015"
             ";")
cur.execute(query)
db_get = cur.fetchone()
for i in range(0, len(db_get)):
    std.append(float(db_get[i]))

id_list = get_player_id(2015)


for id in id_list:
    player_avg=[]
    dist = []
    insert_string = "INSERT INTO fantasy_stdev_2015 VALUES(" + str(id) + ", "
    cur.execute("SELECT first_name, last_name "
                                "FROM id_player "
                                "WHERE id=" + str(id) + ";")
    db_read = cur.fetchone()
    print(db_read)

    for name in range(0, len(db_read)):
        insert_string += "\"" + str(db_read[name]) + "\", "

    query = ("SELECT games_played, min, fgm,"
            "fga, fg_pct, fg3m, fg3a,"
            "fg3_pct, ftm, fta, ft_pct,"
            "oreb, dreb, reb, ast, stl, blk,"
            "tov, atr, pts"
            " FROM avg_2015 "
             "WHERE player_id=" + str(id) + ";")

    cur.execute(query)
    db_get = cur.fetchone()
    for num in db_get:
        player_avg.append(float(num))

    for i in range(0, len(player_avg)):
        temp = float((float(player_avg[i]) - avg[i])/std[i])
        if i == 17:
            temp *= -1
        dist.append(temp)
    print(dist)

    for stat in range(0, len(dist)):
        if stat != len(dist) - 1:
            if str(dist[stat]) == 'None':
                insert_string += '0.0000' + ", "
            else:
                insert_string += str(dist[stat]) + ", "
        else:
            if str(dist[stat]) == 'None':
                insert_string += '0.0000' + ")"
            else:
                insert_string += str(dist[stat]) + ");"

    print(insert_string)
    cur.execute(insert_string)
    db.commit()
