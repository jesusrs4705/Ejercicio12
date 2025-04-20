{
    'name': 'Sale Delivery Notes',
    'version': '1.0',
    'summary': 'Add notes in sales orders and delivery orders',
    'author': 'Jesus',
    'depends': ['sale_stock'],
    'data': [
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'report/sale_report_templates.xml',
        'report/stock_report_templates.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}