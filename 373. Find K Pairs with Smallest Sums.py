class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = [[nums1[0], nums2[0]]]
        if len(nums1) == 1:
            i = 1
            while len(pairs) < k:
                pairs.append([nums1[0], nums2[i]])
                i += 1
        elif len(nums2) == 1:
            i = 1
            while len(pairs) < k:
                pairs.append([nums1[i], nums2[0]])
                i += 1
        else:
            inds = [[0, 1], [1, 0]]
            sums = [nums1[0]+nums2[1], nums1[1]+nums2[0]]
            while len(pairs) < k:
                i = sums.index(min(sums))
                pairs.append([nums1[inds[i][0]], nums2[inds[i][1]]])
                if inds[i][0] + 1 < len(nums1):
                    new = [inds[i][0]+1, inds[i][1]]
                    if new not in inds:
                        inds.append(new)
                        sums.append(nums1[new[0]] + nums2[new[1]])
                if inds[i][1] + 1 < len(nums2):
                    new = [inds[i][0], inds[i][1]+1]
                    if new not in inds:
                        inds.append(new)
                        sums.append(nums1[new[0]] + nums2[new[1]])
                inds.pop(i)
                sums.pop(i)
        return pairs