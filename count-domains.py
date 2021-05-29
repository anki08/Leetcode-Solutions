def subdomainVisits(cpdomains):
    subdomains_dict = {}
    for cpdomain in cpdomains:
        no_of_calls = cpdomain.split(' ')[0]
        sec_part = cpdomain.split(' ')[1]
        sub_domains = sec_part.split('.')
        arr = []
        for i in range(len(sub_domains)):
            str_res = sub_domains[i]
            for j in range(i+1, len(sub_domains)):
                str_res = str_res + "." + sub_domains[j]
            arr.append(str_res)
        sub_domains = arr
        for sub_domain in sub_domains:
            if sub_domain in subdomains_dict:
                subdomains_dict[sub_domain] += int(no_of_calls)
            else:
                subdomains_dict[sub_domain] = int(no_of_calls)

    print(subdomains_dict)
    res = []
    for k,v in subdomains_dict.items():
        s = str(v) + " " + k
        res.append(s)
    print(res)



if __name__ == '__main__':
    subdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    subdomainVisits(subdomains)
