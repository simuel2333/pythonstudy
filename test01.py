def f(first_name, last_name, **user_info):
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	for k,v in user_info.items():
		profile[k] = v
	return profile
ss = f('a', 'b', k = 'v1', k2 = 'v2')
print(ss)