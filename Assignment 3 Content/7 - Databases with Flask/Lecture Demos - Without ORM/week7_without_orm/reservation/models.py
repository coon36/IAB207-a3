
from sqlite3 import Connection, connect

connection=None

class Hotel:
    #  
    def __init__(self, name=None, description=None, image=None):
        #initialize the object and set its connection
        self.name=name
        self.description = description
        self.image = image
        self.hotelid=-1
        self.rooms = dict()

    def set_id(self, id):
        self.hotelid=id

    def __repr__(self):
        s="Name: {}, Description: {}, Image: {}, Id: {}"
        s= s.format(self.name, self.description, self.image, self.hotelid)
        return s

class Room:

    def __init__(self, type=None, description=None, number_of_rooms=None, 
                price=None, hotelid=-1):
        self.type=type
        self.description=description
        self.number_of_rooms=number_of_rooms
        self.price=price
        self.hotelid=hotelid
        self.roomid=-1

    def set_id(self, id):
        self.roomid=id
    
    def __repr__(self):
        s="Type: {}, Description: {}, Number of rooms: {}, price: {}"
        s= s.format(self.type, self.description, self.number_of_rooms, self.price)
        return s


     
def _connect_db():
    # Create a connection to the database
    global connection
    connection = connect(database = './reservation/reservation.db')
    return connection


def create_hotel(hotel):
        # check if a db connect exists else connet
    global connection
    if(connection ==None):
        connection=_connect_db()

    cursor = connection.cursor()
    sql = "INSERT INTO HOTEL (name, description, image) values (?,?, ?)"
    cursor.execute(sql, (hotel.name,hotel.description,hotel.image))
    connection.commit()
    hotelid = cursor.lastrowid
    hotel.set_id(hotelid)
    cursor.close()
    return  hotelid # return the id of the hotel that was created
    


def add_room(hotelid,type, description,number_of_rooms,price ):
    global connection
    if(connection ==None):
        connection=_connect_db()

    cursor = connection.cursor()
    sql = "INSERT INTO ROOM ( type,description, num_rooms, price, hotelid) values (?,?, ?,?,?)"
    cursor.execute(sql, (type,description,number_of_rooms, price, hotelid))
    connection.commit()
    roomid = cursor.lastrowid
    cursor.close()
    return roomid

def get_hotels():
    global connection
    if(connection == None):
        connection=_connect_db()

    cursor = connection.cursor()
    sql = "SELECT hotelid, name,description,image from HOTEL"
    cursor.execute(sql)
    rows = cursor.fetchall()
    hotelList = list()
    for row in rows:
        hotelid=row[0]
        name = row[1]
        description = row[2]
        image = row[3]
        hotel =Hotel(name,description,image)
        hotel.set_id(hotelid)
        hotelList.append(hotel)
    return hotelList

  

def get_rooms(hotelid):
    room_dict=dict()
    global connection
    if(connection == None):
        connection=_connect_db()

    cursor = connection.cursor()
    sql = "SELECT type,description,price, num_rooms from ROOM where hotelid=?"
    cursor.execute(sql, (hotelid,))
    rows = cursor.fetchall()

    for row in rows:
        eRoom = Room()
        eRoom.type = row[0]
        eRoom.description = row[1]
        eRoom.price = row[2]
        eRoom.number_of_rooms = row[3]
        eRoom.hotelid = hotelid
        room_dict[type]=eRoom
    cursor.close()
    return room_dict


   
def close():
    global connection
    if(connection is not None):
        print('Closing the DB connection', connection)
        connection.close()



str=""" CREATE TABLE HOTEL ( 'name' text not null unique,
                                'description' text,
                                'image' text not null,
                                'hotelid' integer primary key autoincrement
                                )
    """

str = """CREATE TABLE room ( 'type' text not null,
                                'description' text,
                                'price' integer not null,
								'num_rooms' integer not null,
								'hotelid' integer not null,
                                'roomid' integer primary key autoincrement,
								foreign key (hotelid) REFERENCES HOTEL(hotelid)
                                )"""
    


