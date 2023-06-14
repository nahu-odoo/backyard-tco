{
    'name': 'Library App',
    'summary': 'Library app for book management',
    "depends": ['contacts'],
    'data': [
        "security/ir.model.access.csv",
        # The order of file being loaded is ipmortant
        "views/library_book_views.xml",
        "views/library_rental_views.xml",
        "views/library_magazine.xml",
        "views/book_search_wizard.xml",
        "views/res_partner.xml",
        "views/menu.xml",
        "views/report_library_rental.xml",
    ],
}
