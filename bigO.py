# %% [markdown]
# import time
# import numpy as np
# import matplotlib.pyplot as plt

# %% [markdown]
# ## What is big O notation?
# A method to allow measurement of scalability of code
#
# ### What is good code?
# + Readable: easy to understand and read
# + Scalable: robust

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


# %%
elements = np.array([1, 10, 100, 1000, 10000])
time_results = np.array(
    [results_1, results_10, results_100, results_1000, results_10000]
)

plt.plot(elements, time_results)
plt.ylabel("Time (s)")
plt.xlabel("Number of Elements")
plt.show()

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
#
