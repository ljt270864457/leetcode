#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 2:57 下午
# @Author  : liujiatian
# @File    : 10.三数之和.py

class Solution:
    def threeSum(self, nums):
        '''
        1.升序排序 固定头元素，然后头元素的下一个是left指针，最后一个元素是right指针
        while current<=0:
            if left==right
            left = position[current]+1
            right = n-1
            if left+current+right>0:
                position[right]-=1
            elif left+current+right<0:
                position[left]+=1
            else:
                result.append([target,left,right])
        2.去重
        '''
        result = []
        length = len(nums)
        nums.sort()
        cur = 0
        # cur 是当前固定指针，每次右移一个单位
        while cur < length - 2:
            if nums[cur] > 0:
                break
            # print(f'==外层第{cur}轮==')

            left = cur + 1
            right = length - 1
            while left < right:
                # print(nums[cur], nums[left], nums[right], nums[cur] + nums[left] + nums[right])
                if nums[cur] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[cur] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    if [nums[cur], nums[left], nums[right]] not in result:
                        result.append([nums[cur], nums[left], nums[right]])
                    left += 1
                    right -= 1
            cur += 1
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
