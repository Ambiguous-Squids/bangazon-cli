

class SessionManager:

	'''
		Persist session data while program runs
	'''

	def __init__(self):
		self.customerId = None
		self.paymentId = None
		self.active_customer = False

	def set_active_customer(self):
		self.active_customer = True

	def get_active_customer(self):
		return self.active_customer

	def set_active_customerId(self, customerId):
		self.customerId = customerId

	def get_active_customerId(self):
		return self.customerId

	def set_active_paymentId(self, paymentId):
		self.paymentId = paymentId

	def get_active_paymentId(self):
		return self.paymentId