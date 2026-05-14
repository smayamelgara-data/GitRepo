import random 
import math 
import statistics 

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randit(3,10)
pi = math.pi 

#Sample Values Calculations 
value_sum = sum(vals_sample)
value_avg = statistic.mean(vals_sample)
value_median = statistic.median(val_sample)

#200 Choice Value Calculations
choice_avg = statistic.mean(vals_choices)
choice_median = statistic.median(val_choices)
choice_stdev= statistic.stdev(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_variance = statistics.variance(vals_choices)

# Circle area calculations
circle_area = pi * radius ** 2
area_rounded_up = math.ceil(circle_area)
area_rounded_down = math.floor(circle_area)

# Final output
print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", value_sum)
print("Average of 75 sample values:", value_avg)
print("Median of 75 sample values:", value_median)

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", choices_avg)
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", choices_stdev)
print("Variance of 200 values:", choices_variance)

print('\n')

print("_Modeling a random circle:")
print("Radius =", radius, ", area =", area_rounded_up, "(rounded up to the nearest integer)")
print("Radius =", radius, ", area =", area_rounded_down, "(rounded down to the nearest integer)")