# print("\n##### DATA STRUCTURES #####\n")
# print("Linked List:")
# from data_structures import linked_list_implementation

# print("\nDouble linked list:")
# from data_structures import double_linked_list_implementation

# print("\nStack:")
# from data_structures import stack_implementation

# print("\nQueue:")
# from data_structures import queue_implementation

# print("\nBinary search tree:")
# from data_structures import binary_search_tree_implementation

print("\nGraph:")
from data_structures import graph_implementation

# print("\n##### ALGORITHMS #####\n")
# print("## SORTING ##")
# print("\nBubble sort:")
# from algorithms.sorting import bubble_sort

# print("\nSelection sort:")
# from algorithms.sorting import selection_sort

# print("\nInsertion sort:")
# from algorithms.sorting import insertion_sort

# print("\nMerge sort:")
# from algorithms.sorting import merge_sort

# print("## SEARCHING ##")
# print("\nBreadth first search (BST):")
# from algorithms.searching import breadth_first_search

# print("\nDeep first search (BST):")

# print("## MATHEMATICS ##")
# print("\nCount digits:")
# from algorithms.mathematics import count_digits

# print("\nPalindrome numbers:")
# from algorithms.mathematics import palindrome_number

# print("\nFactorial of a number:")
# from algorithms.mathematics import factorial_of_number

# print("\nTrailing zeros in factorial:")
# from algorithms.mathematics import trailing_zeros_in_factorial

# print("\nGreatest Common Divider:")
# from algorithms.mathematics.greatest_common_divider import greatest_common_divider_optimized
# print(greatest_common_divider_optimized(4, 6))

# print("\nLeast common multiple:")
# from algorithms.mathematics.least_common_multiple import least_common_multiple
# print(least_common_multiple(12, 15))

# print("\nCheck of prime:")
# from algorithms.mathematics.check_for_prime import check_for_prime_optimized
# print(check_for_prime_optimized(7))

# print("\nPrime factors:")
# from algorithms.mathematics.prime_factors import prime_factors_optimized
# prime_factors_optimized(12)

# print("\nAll divisors of a number:")
# from algorithms.mathematics.all_divisors_of_a_number import all_divisors_of_a_number_ordered
# all_divisors_of_a_number_ordered(100)

# print("\nSieve of Erastosthenes:")
# from algorithms.mathematics.sieve_of_eratosthenes import sieve_of_eratosthenes_optimized
# sieve_of_eratosthenes_optimized(25)

# print("\nComputing power:")
# from algorithms.mathematics.computing_power import computing_power_iterative
# print(computing_power_iterative(3, 4))

# from algorithms.bit_magic.check_kth_is_set import check_kth_is_set
# print("## Bit magic ##")
# check_kth_is_set(5, 3)

# from algorithms.bit_magic.count_set_bits import lookup_table
# print("\nCount set bits:")
# print(lookup_table(13))

# from algorithms.bit_magic.is_power_of_two import is_power_of_two
# print("\nPower of two:")
# print(is_power_of_two(2))

# from algorithms.bit_magic.one_odd_occurring import get_one_odd_occurring
# print("\nOne odd occurring:")
# print(get_one_odd_occurring([4, 3, 4, 4, 4, 5, 5]))

# from algorithms.bit_magic.one_odd_occurring import find_missing_no
# print("\nFind missing no:")
# print(find_missing_no([1, 5, 3, 2]))

# from algorithms.bit_magic.two_odd_ocurring import get_two_odd_ocurring
# print("\nTwo odd ocurring:")
# print(get_two_odd_ocurring([3, 4, 3, 4, 8, 4, 4, 32, 7, 7]))

# from algorithms.bit_magic.power_set_using_bitwise import get_string_subsets
# print("\nString subsets:")
# print(get_string_subsets('abc'))

# print("## RECURSION ##")
# print("\nBinary representation:")
# from algorithms.recursion.binary_representation import binary_representation
# binary_representation(7)

# print("\nLogN2:")
# from algorithms.recursion.logN2 import logN2
# print(logN2(16))

# print("\nFactorials:")
# from algorithms.recursion.factorials import findFactorialRecursive
# print(findFactorialRecursive(5))

# print("\nFibbonacci:")
# from algorithms.recursion.fibonacci import fibonacciRecursive
# print(fibonacciRecursive(7))

# print("\nPalindrome check:")
# from algorithms.recursion.palindrome_check import palindrome_check
# print(palindrome_check("abba"))

# print("\nSum of digits:")
# from algorithms.recursion.sum_of_digits import sum_of_digits
# print(sum_of_digits(10))

# print("\nRope cutting problem:")
# from algorithms.recursion.rope_cuttting_problem import rope_cutting_problem
# print(rope_cutting_problem(23, 11, 9, 12))

# print("\nGenerate subsets:")
# from algorithms.recursion.generate_subsets import generate_subsets
# generate_subsets("AB", "")

# print("\nGenerate subsets:")
# from algorithms.recursion.tower_of_hanoi import tower_of_hanoi
# tower_of_hanoi(3,"A", "B", "C")

# print("\nJosephus problem:")
# from algorithms.recursion.josephus_problem import josephus_problem
# print(josephus_problem(5, 3))

# print("\nSubset sum:")
# from algorithms.recursion.subset_sum import subset_sum
# print(subset_sum([10, 20, 25], 3, 25))

# print("\nPrint permutations:")
# from algorithms.recursion.print_permutations import print_permutations
# print_permutations(["A", "B", "C"])

# print("## ARRAYS ##")

# print("\nLinear search:")
# from algorithms.arrays.linear_search import linear_search
# print(linear_search([3,5,7], 7))

# print("\nInsert:")
# from algorithms.arrays.insert import insert
# print(insert([3,5,7,8,9,None, None, None], 7, 8))

# print("\nDelete:")
# from algorithms.arrays.delete import delete
# print(delete([3,5,7,8,9],5, 5))

# print("\nLargest element:")
# from algorithms.arrays.largest_element import largest_element
# print(largest_element([10,5,20,8]))

# print("\nSecond largest element:")
# from algorithms.arrays.second_largest_element import second_largest_element
# print(second_largest_element([20,10,20,8,12]))

# print("\nCheck array sorted:")
# from algorithms.arrays.check_array_sorted import check_array_sorted
# print(check_array_sorted([2, 2, 3]))

# print("\nReverse an array:")
# from algorithms.arrays.reverse_array import reverse_array
# print(reverse_array([1, 2, 2, 3]))

# print("\nRemove duplicates in sorted array:")
# from algorithms.arrays.remove_duplicates_sorted_array import remove_duplicates_sorted_array
# print(remove_duplicates_sorted_array([1, 2, 2, 3, 3, 3, 3]))

# print("\nMove zeros to end:")
# from algorithms.arrays.move_zeros_to_end import move_zeros_to_end
# print(move_zeros_to_end([10, 5, 0, 0, 8, 0, 9, 0]))

# print("\nLeft rotate array by one:")
# from algorithms.arrays.left_rotate_array_by_one import left_rotate_array_by_one
# print(left_rotate_array_by_one([10, 5, 0, 0, 8, 0, 9, 0]))

# print("\nLeft rotate array by d:")
# from algorithms.arrays.left_rotate_array_by_d import left_rotate_array_by_d
# print(left_rotate_array_by_d([1, 2, 3, 4, 5], 2))

# print("\nLeaders in an array:")
# from algorithms.arrays.leaders_in_array import leaders_in_array
# leaders_in_array([7, 10, 4, 10, 6 , 5, 2])

# print("\nMaximum difference:")
# from algorithms.arrays.maximum_difference import maximun_difference
# print(maximun_difference([30, 10, 8, 2]))

# print("\nFrequencies in sorted array:")
# from algorithms.arrays.frequencies_in_sorted_array import frequencies_in_sorted_array
# frequencies_in_sorted_array([10, 10, 10, 25, 30, 30, 15, 15, 17])

# print("\nBuy and sell problem:")
# from algorithms.arrays.buy_and_sell_problem import buy_and_sell_problem
# print(buy_and_sell_problem([1,5,3,8,12]))

# print("\nTrapping rain water:")
# from algorithms.arrays.trapping_rain_water import trapping_rain_water
# print(trapping_rain_water([5,0,6,2,3]))

# print("\nTrapping rain water:")
# from algorithms.arrays.max_consecutive_1s import max_consecutive_1s
# print(max_consecutive_1s([1,0,1,1,1,1,0,1,1]))

# print("\nMaximum subarray sum:")
# from algorithms.arrays.maximum_subarray_sum import maximum_subarray_sum
# print(maximum_subarray_sum([2,3,-8,7,-1,2,3]))

# print("\nLonges even odd subarray:")
# from algorithms.arrays.longest_even_odd_subarray import longest_even_odd_subarray
# print(longest_even_odd_subarray([10,12,14,7,8]))

print("\nMaximum circularsubarray sum:")
from algorithms.arrays.maximum_circular_sum_subarray import maximum_circular_sum_subarray
print(maximum_circular_sum_subarray([5,-2,3,4]))

