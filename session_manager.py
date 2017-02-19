

class SessionManager:

	'''
		Persist session data while program runs
	'''

	def __init__(self):
		self.customerId = None
		self.paymentId = None
		self.active_customer = False
		self.orderId = None

	def set_active_customer(self):
		self.active_customer = True

	def deactivate_customer(self):
		self.customerId = None
		self.paymentId = None
		self.active_customer = False
		self.orderId = None

	def active_customer(self):
		return self.active_customer

	def set_active_customerId(self, customerId):
		self.customerId = customerId

	def get_active_customerId(self):
		return self.customerId

	def set_active_paymentId(self, paymentId):
		self.paymentId = paymentId

	def get_active_paymentId(self):
		return self.paymentId

	def get_active_orderId(self):
		return self.orderId

	def set_active_orderId(self, orderId):
		self.orderId = orderId