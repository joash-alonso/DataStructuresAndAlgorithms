# %%
import time
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## What is big O notation?
# A method to allow measurement of scalability of code
#
# ### What is good code?
# + Readable: easy to understand and read
# + Scalable: robust. Speed and memory.

# %%
# Helper Function - Plotting Decorator
def plot(func):
    def wrapper(*args, **kwargs):
        elements, time_array = func(*args, **kwargs)
        plt.plot(elements, time_array)
        plt.ylabel("Time (s)")
        plt.xlabel("Elements")
        plt.show()

    return wrapper


# %% [markdown]
# # O(n) - Linear Time

# %%
@plot
def find_nemo(elements=[1, 10, 100, 1000, 10000]):
    time_array = []
    for element in elements:
        nemo_array = ["nemo"] * element
        time_start = time.time()
        counter = 0
        for item in nemo_array:
            if item == "nemo":
                counter += 1
        time_end = time.time()
        print(f"Call to find Nemo took: {time_end - time_start}s")
        time_taken = time_end - time_start
        time_array.append(time_taken)
    return elements, time_array


# %%
# Test with different size arrays

find_nemo()

# %% [markdown]
# finding_nemo function is O(n). It is linear time since it has to access all n elements in the array.

# %% [markdown]
# # O(1) - Constant Time
#
# ```python
#
# boxes = ['amazon', 'best buy', 'walmart']
#
# def compress_first_box(boxes):
#     time_start = time.time()
#     print(boxes[0])
#     time_end = time.time()
#     return time_end - time_start
# ```
#
# This is classed as constant time since it only has to do one operation regardless of the size of the input.

# %%
@plot
def compress_first_box(elements=[1, 10, 100, 1000, 10000]):
    time_array = []
    for element in elements:
        box_array = ["box"] * element
        time_start = time.time()
        box = box_array[0]
        time_end = time.time()
        print(f"Call to find Nemo took: {time_end - time_start}s")
        time_taken = time_end - time_start
        time_array.append(time_taken)
    return elements, time_array


# %% [markdown]
# What is the time complexity?
# ```python
# def another_function():
#     pass
#
# def fun_challenge(input):
#     a = 10 # O(1)
#     a = 50+3 # O(1)
#
#     for index in range(len(input)): #0(n)
#         another_function() #O(n)
#         stranger = True #O(n)
#         a += 1 #O(n)
#
#     return a #O(1)
# ```
# Solution: Time complexity is O(n) since we need to iterate through each input, O(3n+4) -> essentially O(n)

# %% [markdown]
# What is the time complexity for this?
#
# ```javascript
# function anotherFunChallenge(input) {
#   let a = 5; // O(1)
#   let b = 10; // O(1)
#   let c = 50; // O(1)
#   for (let i = 0; i < input; i++) { // O(n)
#     let x = i + 1; // O(n)
#     let y = i + 2; // O(n)
#     let z = i + 3; // O(n)
#
#   }
#   for (let j = 0; j < input; j++) { // O(n)
#     let p = j * 2; // O(n)
#     let q = j * 2; // O(n)
#   }
#   let whoAmI = "I don't know"; // O(1)
# }
# ```
#
#
# Solution: Time complexity is O(n) <-- O(7n+4)

# %% [markdown]
# ## 4 Rules of Big O
#
# + **Rule** 1: Worst Case
# Assume the worst case scenario. In the finding_nemo example, what happens if nemo was the final element in the array?
# This means that when iterating through the list, you still have to go through all items in the list
#
# + **Rule 2**: Remove Constants
# Remove any constant terms, O(1) operations, as this does not contribute to efficiency
#
# + **Rule 3**: Different terms for inputs
# Assign different variables if different, inputs
#     ```javascript
#     function func(input_a, input_b) {
#         input_a.forEach(function(input)) {
#             console.log(input)
#         });
#
#         input_b.forEach(function(input)) {
#             console.log(input)
#         });
#     }
#     ```
#
#     Solution: O(n+m), if loops are nested, then O(nm)
#
# + **Rule 4**: Drop Non Dominants
# Drop the lowest order. If the time complexity is O(n + n^2) --> O(n)
#

# %% [markdown]
# # O(n^2): Quadratic Time

# %%


@plot
def log_all_pairs_of_array(
    elements=[
        1,
        10,
        100,
        200,
        300,
        400,
        500,
        600,
        700,
        800,
        900,
        1000,
        1500,
        2000,
        2500,
        3000,
        3500,
        4000,
        4500,
        5000,
        10000,
        100000,
    ]
):
    time_array = []
    for element in elements:
        array = np.arange(0, element, 1)
        print(len(array))
        start = time.time()
        for number_a in array:
            for number_b in array:
                continue
        end = time.time()
        time_taken = end - start
        time_array.append(time_taken)
    return elements, time_array


log_all_pairs_of_array()


# %% [markdown]
# ## Big O Cheatsheet
#
# + **O(1)** - constant, no loops
# + **O(log n)** - logarithmic, usually searching algorithms if sored
# + **O(n)** - linear, for/while lkoops
# + **O(n log n)** - log linear, usually sorting operations
# + **O(n^2)** - quadratic, nested loops, every element in a collection needs to be compared to every other element
# + **O(2^n)** - exponential, recursive algorithms that solve a problem of size n
# + **O(n!)** - adding a loop for every element
#
# + Iterating through half a collection is still O(n)
# + Two Separate coolections: O(a*b)
#
# ### What can cause time in a function?
# + Operations
# + Comparisons
# + Looping
# + Outside Function Call
#
# ### What causes Space complexity?
# + **Variables**
# + **Data Structures**
# + **Function Call**
# + **Allocations**

# %% [markdown]
# ## Space Complexity:
#
# + **Heap**: Where variables are stored
# + **Stack**: Where we keep track of function calls

# %%
# What is the space and time complexity for this function:


def boo(n):
    for i in range(len(n)):
        print("Boo!")


boo([1, 2, 3, 4, 5])

# Time Complexity: O(n)
# Space Complexity: O(1)


def array_of_hi_n_time(n):
    hi_array = []
    for item in n:
        hi_array.append("Hi!")
    return hi_array


array_of_hi_n_time([1, 2, 3, 4, 5])

# Time Complexity: O(n)
# Space Complexity: O(n)

# %%
