class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
from typing import List


class Solution:

  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    toNum = {}
    n = len(accounts)
    par = list(range(n))
    rank = [0] * n

    def find(node):
      cur = node
      while cur != par[cur]:
        par[cur] = par[par[cur]]  # FIXED: Correct path halving syntax
        cur = par[cur]  # FIXED: Advance cur
      return cur

    def union(n1, n2):
      r1 = find(n1)
      r2 = find(n2)
      if r1 != r2:
        if rank[r1] > rank[r2]:
          par[r2] = r1
        elif rank[r1] < rank[r2]:
          par[r1] = r2
        else:
          par[r2] = r1
          rank[r1] += 1  # FIXED: Increment rank ONLY on equal tree heights

    # 1. Build email mapping and union connected accounts
    for i in range(n):
      for eml in accounts[i][1:]:
        if eml in toNum:
          union(i, toNum[eml])
        else:
          toNum[eml] = i  # FIXED: Save email index

    # 2. Group emails by canonical root using find(i)
    groups = defaultdict(set)
    for i in range(n):
      root = find(i)  # FIXED: Must call find(i) to resolve full chain
      for eml in accounts[i][1:]:
        groups[root].add(eml)

    # 3. Format result: [Name, sorted_emails...]
    return [
        [accounts[root][0]] + sorted(emails) for root, emails in groups.items()
    ]