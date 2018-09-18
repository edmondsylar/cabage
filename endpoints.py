from flask import Flask, jsonify, make_response, request
import time
import json
today = time.ctime()

class data:
    def __init__(self):
        self.orders = [
            {
                'id':1,
                'state':'Pending',
                'date':today,
                'By':'Edmond Sylar',
                'Order':'Fried chips'
            }
        ]

    # This is the end point for getting all items in the orders.
    def get_all(self):
        return self.orders
    
    # This is the endpoint for getting an item by id from the orders.
    def get_by_id(self):
        for order in self.orders:
            if order['id'] == id:
                return order

    # This is the endpoint for posting a new Order.
    def poster(self):
        self.order = {
			'id':len(self.orders)+1,
			'state':request.json['state'],
			'date':today,
			'By':request.json['By'],
            'Order':request.json['Order']
		}
        self.orders.append(self.order)
        


    #This is the endpoint for updating an order status depending on its id
    def update(self):
        for self.order in self.orders:
            if self.order['id'] == id:
                self.order['status'] = request.json['Order']
        return jsonify({'msg':self.order})

    def get_all_by_status(self):
        pass
       


    # This endpoint simply deletes an order from the orers list.
    def delete(self):
        pass