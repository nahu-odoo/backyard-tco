import xmlrpc.client
import pprint

url = "http://localhost:8069"
# url = "https://bmd-albert-odoo-training-nni-day1-8634217.dev.odoo.com/"
db = "training"
# db = "bmd-albert-odoo-training-nni-day1-8634217"
username, password = "admin", "admin"

uid = xmlrpc.client.ServerProxy(url + "/xmlrpc/2/common").authenticate(db, username, password, {})  # user id
model = xmlrpc.client.ServerProxy(url + "/xmlrpc/2/object")  # to fetch the data

# do the first search
# res = model.execute_kw(db, uid, password, 'sale.order', 'search', [[]])
# print(res)

# search_read: shows the data
# res_search_read = model.execute_kw(db, uid, password, 'res.partner', 'search_read', [[], ['name', 'country_id']])
# pprint.pprint(res_search_read)

# create
# res_create = model.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': 'New Partner'}])

# update
# updating = model.execute_kw(db, uid, password, 'res.partner', 'write', [48, {'name': "ABCDEF"}])

# EXERCISE
# res = model.execute_kw(db, uid, password, 'res.partner', 'search_read', [[('is_company', '=', True)], ['name', 'country_id']])
# pprint.pprint(res)

# for contact in res:
#     new_email = 'hr@' + contact['name'].lower().replace(' ', '_') + '.com'
#     model.execute_kw(db, uid, password, 'res.partner', 'write', [[contact['id']], {'email': new_email}])

model.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "Nigel", 'phone': "123456"}])
