import re

f = open("output/raw/042_c.txt","r")
s = f.read()

re_service = re.compile("POST.*/([^/]+) HTTP*")
re_service_results = re_service.findall(s)

re_action = re.compile("SOAPAction.*/([^/]+)\"")
re_action_results = re_action.findall(s)

re_post_body = re.compile("\r\n\r\n([^\r\n]*)")
re_post_body_results = re_post_body.findall(s)


print re_service_results
print re_action_results
print re_post_body_results





#print s
