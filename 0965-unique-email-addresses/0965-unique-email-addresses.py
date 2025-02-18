class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for i in range(0, len(emails)):
            local, domain = emails[i].split('@')
            local = local.split('+')[0]
            local = local.replace('.', "")
            unique.add((local, domain))
            
        return len(unique)
        
        