# https://leetcode.com/problems/two-sum
import pytest


class Solution:
    __slots__ = ()

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return self.twoSum_hash(nums, target)

    @staticmethod
    def twoSum_hash(nums: list[int], target: int) -> list[int]:
        num_map = dict()
        for i, num in enumerate(nums):
            if target - nums[i] in num_map:
                return [i, num_map[target - nums[i]]]
            num_map[num] = i

        return []

    @staticmethod
    def twoSum_bf(nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]

        return []

    @staticmethod
    def twoSum_hash_two_pass(nums: list[int], target: int) -> list[int]:
        number_map = {}
        length = len(nums)
        for i in range(length):
            number_map[nums[i]] = i

        for i in range(length):
            candidate = nums[i]
            wanted = target - candidate
            if wanted in number_map and number_map[wanted] != i:
                return [i, number_map[wanted]]
        return []

    @staticmethod
    def twoSum_hash_one_pass(nums: list[int], target: int) -> list[int]:
        number_map = {}

        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in number_map:
                return [number_map[candidate], i]
            else:
                number_map[nums[i]] = i
        return []


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        # 题目示例1
        ([2, 7, 11, 15], 9, [0, 1]),
        # 题目示例2
        ([3, 2, 4], 6, [1, 2]),
        # 题目示例3
        ([3, 3], 6, [0, 1]),
        # 包含负数的场景
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        # 正负混合的场景
        ([2, -1, 5, 3], 4, [1, 2]),
        # 包含0的场景
        ([0, 4, 3, 0], 0, [0, 3]),
        # 超大正数场景（边界值）
        ([10 ** 9, -10 ** 9, 5], 0, [0, 1]),
        # 超大负数场景（边界值）
        ([-10 ** 9, 10 ** 9, -5], 0, [0, 1]),
        # 最小长度数组（边界值）
        ([1, 1], 2, [0, 1]),
    ],
    ids=[
        "example1", "example2", "example3",
        "negative_numbers", "mixed_pos_neg", "zero_in_array",
        "large_pos_numbers", "large_neg_numbers", "min_length_array"
    ]
)
def test_two_sum_basic(nums, target, expected):
    result = Solution().twoSum(nums, target)
    assert set(result) == set(expected)


# ========== 最大边界值测试 ==========
def test_two_sum_max_length_array():
    """测试最大长度数组的边界场景（10^4个元素）"""
    nums = list(range(10 ** 4))
    target = nums[-2] + nums[-1]  # 取最后两个数的和作为目标值
    expected = [len(nums) - 2, len(nums) - 1]
    result = Solution().twoSum(nums, target)
    assert set(result) == set(expected)


# ========== 性能测试 ==========
def test_two_sum_performance(benchmark):
    """性能测试：验证算法在大数据量下的执行效率"""
    # 构造10^4个元素的数组
    nums = list(range(10 ** 4))
    target = nums[-2] + nums[-1]

    # 使用pytest-benchmark的benchmark装饰器测试性能
    result = benchmark(Solution().twoSum, nums, target)

    # 验证结果正确性（性能测试也要保证结果对）
    expected = [len(nums) - 2, len(nums) - 1]
    assert set(result) == set(expected)
