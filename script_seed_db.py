if __name__ == "__main__":
    """Seed the database with brazilian postal_codes"""
    from app.models.address import db, Address
    import csv

    db.create_all()
    sourcefile = './ceps_raw.txt'
    with open(sourcefile) as source:
        # for line in source:
        #     fields = line.split('\t')
        reader = csv.reader(source, delimiter="\t")
        rows = list(reader)

    turns = 0
    for row in rows:
        if not Address.query.filter_by(postal_code=row[0]).first():
            obj = Address(row[0], row[3], row[2], row[1].split('/')[0], row[1].split('/')[1])
            db.session.add(obj)
            print(obj)
            turns+=1
            if turns == 1000:
                db.session.commit()
                turns = 0

    print('done')