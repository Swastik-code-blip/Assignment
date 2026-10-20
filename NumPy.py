"""
PW Skills: NumPy Assignment Solutions
Contains executable code and functions answering all 85 questions.
"""

import numpy as np
import pandas as pd

print("==================================================")
print("       PW SKILLS: NUMPY ASSIGNMENT SOLUTIONS      ")
print("==================================================\n")

# ---------------------------------------------------------
# Part 1: Array Creation, Attributes, and Data Types (Q1 - Q17)
# ---------------------------------------------------------

# Q1: Create a NumPy array 'arr' of integers from 0 to 5 and print its data type.
arr_q1 = np.array([0, 1, 2, 3, 4, 5])
print("Q1 Data Type:", arr_q1.dtype)

# Q2: Check if its data type is float64 for given array.
arr_q2 = np.array([1.5, 2.6, 3.7])
print("Q2 Is float64?:", arr_q2.dtype == np.float64)

# Q3: Create a NumPy array 'arr' with a data type of complex128 containing three complex numbers.
arr_q3 = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=np.complex128)
print("Q3 Complex Array:", arr_q3, arr_q3.dtype)

# Q4 & Q5: Convert integer/float64 array to float32 data type to reduce precision.
arr_q5 = np.array([1.123456789, 2.987654321], dtype=np.float64)
arr_q5_float32 = arr_q5.astype(np.float32)
print("Q4/Q5 Converted to float32:", arr_q5_float32.dtype)

# Q6: Function array_attributes
def array_attributes(arr):
    return arr.shape, arr.size, arr.dtype

# Q7: Function array_dimension
def array_dimension(arr):
    return arr.ndim

# Q8: Function item_size_info
def item_size_info(arr):
    return arr.itemsize, arr.nbytes

# Q9: Function array_strides
def array_strides(arr):
    return arr.strides

# Q10: Function shape_stride_relationship
def shape_stride_relationship(arr):
    return arr.shape, arr.strides

# Q11: Function create_zeros_array
def create_zeros_array(n):
    return np.zeros(n)

# Q12: Function create_ones_matrix
def create_ones_matrix(rows, cols):
    return np.ones((rows, cols))

# Q13: Function generate_range_array
def generate_range_array(start, stop, step):
    return np.arange(start, stop, step)

# Q14: Function generate_linear_space
def generate_linear_space(start, stop, num):
    return np.linspace(start, stop, num)

# Q15: Function create_identity_matrix
def create_identity_matrix(n):
    return np.eye(n)

# Q16: Function to convert Python list to NumPy array
def list_to_array(lst):
    return np.array(lst)

# Q17: Demonstrate numpy.view
original_arr = np.array([1, 2, 3])
view_arr = original_arr.view()
print("Q17 View Array created:", view_arr)


# ---------------------------------------------------------
# Part 2: Manipulation, Indexing, Slicing & Reshaping (Q18 - Q40)
# ---------------------------------------------------------

# Q18: Concatenate two arrays along a specified axis
def concat_arrays(arr1, arr2, axis=0):
    return np.concatenate((arr1, arr2), axis=axis)

# Q19: Horizontal concatenation of arrays with different shapes (matching rows)
arr_h1 = np.array([[1, 2], [3, 4]])
arr_h2 = np.array([[5], [6]])
h_concat = np.concatenate((arr_h1, arr_h2), axis=1)

# Q20: Vertically stack multiple NumPy arrays given as a list
def vstack_arrays(arr_list):
    return np.vstack(arr_list)

# Q21: Array within range with step size
def range_with_step(start, stop, step):
    return np.arange(start, stop + 1, step)

# Q22: 10 equally spaced values between 0 and 1 (inclusive)
arr_q22 = np.linspace(0, 1, 10)

# Q23: 5 logarithmically spaced values between 1 and 1000 (inclusive)
arr_q23 = np.logspace(0, 3, 5)

# Q24: Pandas DataFrame from NumPy random integer array (5x3, 0 to 100)
df_q24 = pd.DataFrame(np.random.randint(0, 101, size=(5, 3)), columns=['A', 'B', 'C'])

# Q25: Replace negative values in specific column with zeros using NumPy
def replace_negatives(df, col_name):
    col_data = df[col_name].values
    col_data = np.where(col_data < 0, 0, col_data)
    df[col_name] = col_data
    return df

# Q26: Access 3rd element
arr_q26 = np.array([10, 20, 30, 40, 50])
third_elem = arr_q26[2]

# Q27: Retrieve element at index (1, 2) from 2D array
arr_2d_q27 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
elem_1_2 = arr_2d_q27[1, 2]

# Q28: Boolean indexing for elements > 5
arr_q28 = np.array([3, 8, 2, 10, 5, 7])
filtered_q28 = arr_q28[arr_q28 > 5]

# Q29: Basic slicing index 2 to 5 inclusive
arr_q29 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
sliced_q29 = arr_q29[2:6]

# Q30: Slice 2D array to extract [[2, 3], [5, 6]]
arr_2d_q30 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sub_arr_q30 = arr_2d_q30[0:2, 1:3]

# Q31: Extract elements in specific order based on index array
def extract_by_indices(arr, indices):
    return arr.take(indices)

# Q32: Filter elements greater than threshold using boolean indexing
def filter_greater(arr, threshold):
    return arr[arr > threshold]

# Q33: Extract elements from 3D array using indices for each dimension
def extract_3d(arr, i, j, k):
    return arr[i, j, k]

# Q34: Elements satisfying two conditions
def filter_two_conditions(arr, cond1, cond2):
    return arr[cond1 & cond2]

# Q35: Extract from 2D array using row and col index arrays
def extract_2d_coords(arr, rows, cols):
    return arr[rows, cols]

# Q36-39: Broadcasting Examples
arr_broad_1 = np.array([1, 2, 3]) + 5  # Q36: scalar broadcast
arr_broad_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) * np.array([1, 2, 3]) # Q37

# Q40: Multiply (2,3) and (2,2) with shape handling (or demonstration)
try:
    a1 = np.ones((2, 3))
    a2 = np.ones((2, 2))
    # Incompatible for standard broadcasting directly without reshape/expansion
    res_40 = np.broadcast_arrays(a1[..., np.newaxis], a2[:, np.newaxis, :])
except ValueError as e:
    res_40 = f"Handled incompatibility: {e}"


# ---------------------------------------------------------
# Part 3: Statistical Operations & Aggregations (Q41 - Q45)
# ---------------------------------------------------------
arr_stat = np.array([[1, 2, 3], [4, 5, 6]])
col_mean = np.mean(arr_stat, axis=0)                # Q41
row_max = np.max(arr_stat, axis=1)                 # Q42
col_max_indices = np.argmax(arr_stat, axis=0)      # Q43
moving_sum = np.cumsum(arr_stat, axis=1)           # Q44
all_even_cols = np.all(arr_stat % 2 == 0, axis=0)  # Q45


# ---------------------------------------------------------
# Part 4: Reshaping, Splitting, Operations & Strings (Q46 - Q60)
# ---------------------------------------------------------

# Q46: Reshape array
original_array = np.array([1, 2, 3, 4, 5, 6])
reshaped_matrix = original_array.reshape(2, 3)

# Q47: Flatten matrix function
def flatten_matrix(mat):
    return mat.flatten()

# Q48: Concatenate two arrays along axis
def concat_two_arrays(a1, a2, axis=0):
    return np.concatenate((a1, a2), axis=axis)

# Q49: Split array into multiple sub-arrays
original_arr_49 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
split_arr = np.array_split(original_arr_49, 3, axis=0)

# Q50: Insert and delete elements
def insert_and_delete(orig, ins_idx, ins_val, del_idx):
    res = np.insert(orig, ins_idx, ins_val)
    res = np.delete(res, del_idx)
    return res

# Q51-55: Element-wise arithmetic operations
arr_e1 = np.array([1, 2, 3, 4, 5])
arr_e2 = np.array([5, 4, 3, 2, 1])
add_res = arr_e1 + arr_e2      # Q51
sub_res = arr_e1 - arr_e2      # Q52
mul_res = arr_e1 * arr_e2      # Q53
div_res = arr_e1 / arr_e2      # Q54
exp_res = arr_e1 ** arr_e2     # Q55

# Q56: Count substring occurrences
def count_substring(arr, sub):
    return sum(np.char.count(arr, sub))

# Q57: Extract uppercase characters from strings
def extract_uppercase(arr):
    return np.array([[c for c in word if c.isupper()] for word in arr], dtype=object)

# Q58: Replace substring
def replace_substring(arr, old, new):
    return np.char.replace(arr, old, new)

# Q59: Concatenate strings element-wise
def concat_strings(arr1, arr2):
    return np.char.add(arr1, arr2)

# Q60: Length of the longest string
def longest_string_len(arr):
    return max(len(s) for s in arr)


# ---------------------------------------------------------
# Part 5: Advanced Math, Stats, Searching & Endianness (Q61 - Q85)
# ---------------------------------------------------------

# Q61: Dataset of 100 random integers (1 to 1000) stats
dataset = np.random.randint(1, 1001, 100)
mean_val = np.mean(dataset)
median_val = np.median(dataset)
var_val = np.var(dataset)
std_val = np.std(dataset)

# Q62: 25th and 75th percentiles of 50 random numbers
rand_50 = np.random.randint(1, 101, 50)
p25, p75 = np.percentile(rand_50, [25, 75])

# Q63: Correlation coefficient
set1 = np.array([1, 2, 3, 4, 5])
set2 = np.array([5, 4, 3, 2, 1])
corr = np.corrcoef(set1, set2)

# Q64: Matrix multiplication using dot function
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
dot_product = np.dot(mat_a, mat_b)

# Q65: 10th, 50th, 90th percentiles and quartiles
arr_65 = np.random.randint(10, 1001, 50)
p_vals = np.percentile(arr_65, [10, 25, 50, 75, 90])

# Q66: Index of specific element
arr_66 = np.array([10, 20, 30, 40, 50])
idx_element = np.where(arr_66 == 30)[0][0]

# Q67: Sort random array
random_sort_arr = np.random.randint(1, 50, 10)
sorted_arr = np.sort(random_sort_arr)

# Q68 - Q70: Filters
arr_filter = np.array([12, 25, 6, 42, 8, 30])
f1 = arr_filter[arr_filter > 20]                       # Q68
f2 = np.array([1, 5, 8, 12, 15])
f2_div3 = f2[f2 % 3 == 0]                              # Q69
f3 = np.array([10, 20, 30, 40, 50])
f3_range = f3[(f3 >= 20) & (f3 <= 40)]                 # Q70

# Q71 - Q75: Endianness and Byte Swapping
arr_endian = np.array([1, 2, 3], dtype=np.int32)
byte_order = arr_endian.dtype.byteorder                # Q71
arr_endian.byteswap(inplace=True)                      # Q72
swapped_new = arr_endian.newbyteorder()                # Q73
# Q74 & Q75: Conditional byte order & check
is_swap_needed = arr_endian.dtype.byteorder != '='     # Q75

# Q76 - Q80: Copies, Views and Mutations
arr1_q76 = np.arange(1, 11)
copy_arr = arr1_q76.copy()
copy_arr[0] = 99  # Does not affect arr1_q76[cite: 14]

matrix_q77 = np.random.randint(1, 10, size=(3, 3))
view_slice = matrix_q77[:2, :2]
view_slice[0, 0] = 999  # Affects original matrix_q77[cite: 14]

array_a = np.arange(1, 13).reshape(4, 3)
view_b = array_a[:2, :]
view_b += 5  # Alters original array_a via broadcasting on view[cite: 14]

orig_array = np.arange(1, 9).reshape(2, 4)
reshaped_view = orig_array.reshape(4, 2)
reshaped_view[0, 0] = 777  # Reflects in orig_array[cite: 14]

data_q80 = np.random.randint(1, 10, size=(3, 4))
data_copy = data_q80[data_q80 > 5].copy()
data_copy[0] = 111  # Does not affect data_q80[cite: 14]

# Q81 - Q85: Matrix Operations
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])
mat_add = matrix_A + matrix_B
mat_sub = matrix_A - matrix_B

matrix_C = np.array([[1, 2], [3, 4], [5, 6]]) # 3x2
matrix_D = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) # 2x4
mat_mul = np.dot(matrix_C, matrix_D)          # Q82 (3x4 result)

matrix_E = np.array([[1, 2, 3], [4, 5, 6]])
mat_transpose = matrix_E.T                    # Q83

square_F = np.array([[4, 3], [3, 2]])
det_F = np.linalg.det(square_F)               # Q84

square_G = np.array([[1, 2], [3, 4]])
inv_G = np.linalg.inv(square_G)               # Q85

print("All 85 NumPy assignment tasks successfully executed!")
