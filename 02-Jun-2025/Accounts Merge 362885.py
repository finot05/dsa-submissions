# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)

        roots = defaultdict(list)
        for email in parent:
            root = find(email)
            roots[root].append(email)
        res = []
        for root_email, emails in roots.items():
            name = email_to_name[root_email]
            res.append([name] + sorted(emails))
        return res

