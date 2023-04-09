import psycopg2

conn = psycopg2.connect("dbname=dblp user=postgres password=Sahana15! host=localhost port=5432")
cur = conn.cursor()

def getJournalID(journal):
    cur.execute("SELECT id FROM journal WHERE name = %s",(journal,))
    if cur.rowcount > 0:
        return cur.fetchone()[0]
    else:
        return None
    
def getAuthorID(author):
    cur.execute("SELECT id FROM author WHERE name = %s",(author,))
    if cur.rowcount > 0:
        return cur.fetchone()[0]
    else:
        return None