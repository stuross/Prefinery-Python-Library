import httplib2
from xml.dom.minidom import parseString

PRE_URL = ''
PRE_KEY = ''
PRE_BETA_ID = ''



def create_tester(email, status):
	xml = '<?xml version="1.0" encoding="UTF-8"?><tester><email>'+email+'</email><status>'+status+'</status></tester>'
	h = httplib2.Http()
	url = PRE_URL+'betas/'+PRE_BETA_ID+'/testers.xml?api_key='+PRE_KEY
	headers = {'Content-type': 'text/xml'}
	resp, content = h.request(url, 'POST', headers=headers, body=xml) 
	return resp

def delete_tester(id):
	h = httplib2.Http()
	url = PRE_URL+'betas/'+PRE_BETA_ID+'/testers/'+id+'.xml?api_key='+PRE_KEY
	resp, content = h.request(url, 'DELETE') 
	return resp

def get_tester_id_by_email(tester_email):
	h = httplib2.Http()
	url = PRE_URL+'betas/'+PRE_BETA_ID+'/testers.xml?api_key='+PRE_KEY+'&email='+tester_email
	resp, content = h.request(url) 
	try:
		xml = parseString(content)
		id = xml.getElementsByTagName('id')[0]
		for node in id.childNodes:
			if node.data:
				return node.data
	except Exception as e:
		return None

def get_tester_code(tester_id):
	h = httplib2.Http()
	url = PRE_URL+'betas/'+PRE_BETA_ID+'/testers/'+tester_id+'.xml?api_key='+PRE_KEY
	resp, content = h.request(url) 
	try:
		xml = parseString(content)
		id = xml.getElementsByTagName('invitation-code')[0]
		for node in id.childNodes:
			if node.data:
				return node.data
	except Exception as e:
		return None


def verify_code(tester_id, code):
	h = httplib2.Http()
	url = PRE_URL+'betas/'+PRE_BETA_ID+'/testers/'+tester_id+'/verify.xml?api_key='+PRE_KEY+'&invitation_code='+code
	resp, content = h.request(url) 
	if resp.status == 200:
		return True
	else:
		return False

def set_tester_status(tester_id, status):
	xml = '<?xml version="1.0" encoding="UTF-8"?><tester><status>'+status+'</status></tester>'
	h = httplib2.Http()
	url = PRE_URL+'betas/'+PRE_BETA_ID+'/testers/'+tester_id+'.xml?api_key='+PRE_KEY
	headers = {'Content-type': 'text/xml'}
	resp, content = h.request(url, 'PUT', headers=headers, body=xml) 
	if resp.status == 200:
		return True
	else:
		return False

