class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a = set()
        for email in emails:
            first, last = email.split('@')
            if '+' in first:
                first = first[:first.index('+')]
            a.add(first.replace('.', '') + '@' + last)
        return len(a)
