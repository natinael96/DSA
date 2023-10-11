class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        freq = {}
        for d in cpdomains:
            count, domains = d.split()
            count = int(count)
            
            subdom = domains.split(".")
            for i in range(len(subdom)):
                subdomain = ".".join(subdom[i:])
                if subdomain not in freq:
                    freq[subdomain] = count
                else:
                    freq[subdomain] += count
        
        result = [str(count) + " " + domain for domain,count in freq.items()]
        return result
    