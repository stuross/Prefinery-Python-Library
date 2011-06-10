from django.test import TestCase
import prefinery_lib

class BetaTest(TestCase):
	def setUp(self):
		self.tester_email = 'test@example.com'
		resp = utils.create_tester(self.tester_email, 'invited')
		self.tester_id = utils.get_tester_id_by_email(self.tester_email)
		self.assertTrue(self.tester_id)
		self.assertEqual(resp.status, 201)

	def tearDown(self):
		resp = utils.delete_tester(self.tester_id)
		self.assertEqual(resp.status, 200)

	def test_get_code(self):
		code = utils.get_tester_code(self.tester_id)
		self.assertTrue(code)
		
	def test_check_code_of_tester(self):
		code = utils.get_tester_code(self.tester_id)
		resp = utils.verify_code(self.tester_id, code)
		self.assertTrue(resp)

	def test_check_fake_code_of_tester(self):
		resp = utils.verify_code(self.tester_id, 'aasdfadsf')
		self.assertFalse(resp)

	def test_activate_user(self):
		resp = utils.set_tester_status(self.tester_id, 'active')
		self.assertTrue(resp)

