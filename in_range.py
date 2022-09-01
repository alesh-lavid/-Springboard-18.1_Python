def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    if lowest >= nums[0]:
      print(f"{lowest} fits")
    else:
      print(f"{lowest} doesn't fit")

    if highest <= nums[-1]:
      print(f"{highest} fits")
    else:
      print(f"{highest} doesn't fit")


in_range([10, 20, 30, 40, 50], 15, 30)            
