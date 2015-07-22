##Averages Table Schema:
import MySQLdb

def calc_and_store_averages(season):
    db = MySQLdb.connect(host="localhost",  user="fred",  db="nba_analysis")
    cur = db.cursor()
    id_list = []

    season_string = '2' + str(season-1)
    cur.execute("SELECT * FROM id_player WHERE to_year=" + str(season) + " AND from_year<" + str(season) + ";")
    for row in cur:
        id_list.append(int(row[1]))

    for players in range(0, len(id_list)):
        insert_string = "INSERT INTO avg_2015 VALUES(" + str(id_list[players]) + ", "

        ## GET THE NAME OF THE PLAYER
        cur.execute("SELECT first_name, last_name "
                            "FROM id_player "
                            "WHERE id=" + str(id_list[players]) + ";")
        db_read = cur.fetchone()
        print(str(db_read[0]) +  " " +str(db_read[1]))
        for i in range(0, len(db_read)):
            insert_string += "\"" + str(db_read[i]) + "\", "


        ## GET THE STATS OF THE PLAYER
        cur.execute("SELECT COUNT(*), AVG(min), AVG(fgm), AVG(fga), SUM(fgm)/SUM(fga), "
                    "AVG(fg3m), AVG(fg3a), SUM(fg3m)/SUM(fg3a), AVG(ftm), AVG(fta), SUM(ftm)/SUM(fta), "
                    "AVG(oreb), AVG(dreb), AVG(reb), AVG(ast), AVG(stl), AVG(blk),"
                    "AVG(tov), AVG(foul), AVG(pts), AVG(plus_minus) "
                    "FROM game_log_2015 "
                    "WHERE season_id=" + season_string + " AND player_id=" + str(id_list[players]) + ";")
        db_read = cur.fetchone()

        for i in range(0, len(db_read)):
            if i != len(db_read) - 1:
                insert_string += str(db_read[i]) + ", "
            else:
                insert_string += str(db_read[i]) + ")"

        print(insert_string)
        try:
            cur.execute(insert_string)
            db.commit()
        except:
            print("Some Shit Happend")

calc_and_store_averages(2015)
