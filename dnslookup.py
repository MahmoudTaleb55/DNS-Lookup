import dns.resolver

def dns_lookup(subdomains, domain):
    results = {}
    for subdomain in subdomains:
        fqdn = f"{subdomain}.{domain}"
        try:
            answers = dns.resolver.resolve(fqdn, 'A')
            results[fqdn] = [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            results[fqdn] = []
        except dns.resolver.NXDOMAIN:
            results[fqdn] = None
        except Exception as e:
            results[fqdn] = str(e)
    return results

if __name__ == "__main__":
    subdomains = ["www", "mail", "ftp", "blog"]
    domain = "example.com"
    lookup_results = dns_lookup(subdomains, domain)
    
    for subdomain, ips in lookup_results.items():
        if ips is None:
            print(f"{subdomain}: No such domain")
        elif not ips:
            print(f"{subdomain}: No A record found")
        else:
            print(f"{subdomain}: {', '.join(ips)}")