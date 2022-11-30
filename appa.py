from cs50 import SQL

db = SQL("sqlite:///cipher.db")

def main():
    data = db.execute("SELECT d_key FROM cipherData WHERE user_id = ?", 1)
    data = data[0]['d_key']
    print(data)





if __name__ == "__main__":
    main()