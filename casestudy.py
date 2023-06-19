import xmlrpc.client

url = "http://localhost:8069"
db = "tco"
user, password = "admin", "admin"

# Getting the user ID of the login
uid = xmlrpc.client.ServerProxy(url + "/xmlrpc/2/common").authenticate(db, user, password, {})
model = xmlrpc.client.ServerProxy(url + "/xmlrpc/2/object")


books = model.execute_kw(db, uid, password, 'library.book', 'search_read', [[], ['name', 'isbn']])
print(books)
